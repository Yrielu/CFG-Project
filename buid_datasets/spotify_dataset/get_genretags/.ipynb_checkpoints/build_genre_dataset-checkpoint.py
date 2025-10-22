import requests
from time import sleep
import json
import pandas as pd

"""
Will now try to attach a genre tag to every song in a sample weekly chart dataset.
By first using AudioDB, if no tag found, Spotify API artist’s genre tag will be used,
if now tag available then Last.fm’s will be used.

1. AudioDB’s genre tags are used (associated to the track)
2. Problematic tags are replaced with `None` values. These include: `‘…’,’song writer’,’ ’`
3. Tracks where value for genre is None, SpotifyAPI’s fist genre tag is used (associated to artist)
4. Tracks that still have no genre tag, LastFm’s tag will be used. 
(issue: Inconsistent tags —>  possible solution: have a list of possible genre tags [rock,pop,rap,…],
 and use LastFM’s first tag that matches any of the possible genre tags, 
 if no tag is matched None is kept as genre)

"""

# Load chart data
chart = pd.read_csv('unique_tracks.csv')
track_details = chart[['artist', 'song_name']]

# Load Spotify token
with open('spotify_access_token.json', 'r') as file:
    token_data = json.load(file)
access_token = token_data['access_token']
headers = {'Authorization': f'Bearer {access_token}'}

# Last.fm API key
LASTFM_API_KEY = '1248d8056afa6877059f8441e116e073'

# Problematic genre tags to filter out (AudioDB)
problematic_tags = {'…', 'song writer', '', ' '}

# Final genre tag list
final_genre_list = []

# Loop through each track
for track_n in range(len(track_details)):
    artist, song_name = track_details.iloc[track_n, :]

    genre = None

    # ------------------ AudioDB ------------------
    audioDB_endpoint = f'https://www.theaudiodb.com/api/v1/json/523532/searchtrack.php?s={artist}&t={song_name}'
    try:
        response = requests.get(audioDB_endpoint)
        audioDB_data = response.json()
        genre_candidate = audioDB_data['track'][0]['strGenre']
        if genre_candidate and genre_candidate.lower().strip() not in problematic_tags:
            genre = genre_candidate
    except Exception:
        pass

    # ------------------ Spotify API ------------------
    if genre is None:
        spotify_endpoint = f"https://api.spotify.com/v1/search?q={artist}&type=artist&limit=1"
        try:
            response = requests.get(spotify_endpoint, headers=headers)
            if response.status_code == 401:
                raise Exception(f'Spotify token expired, please rerun spotify_connection.py')
            spotify_data = response.json()
            genre_candidate = spotify_data['artists']['items'][0]['genres'][0]
            if genre_candidate and genre_candidate.lower().strip() not in problematic_tags:
                genre = genre_candidate
        except Exception:
            pass

    # ------------------ Last.fm ------------------
    if genre is None:
        lastfm_endpoint = 'http://ws.audioscrobbler.com/2.0/'
        params = {
            'method': 'track.getInfo',
            'api_key': LASTFM_API_KEY,
            'artist': artist,
            'track': song_name,
            'format': 'json'
        }
        try:
            response = requests.get(lastfm_endpoint, params=params)
            data = response.json()
            genre_candidate = data['track']['toptags']['tag'][0]['name']
            if genre_candidate and genre_candidate.lower().strip() not in problematic_tags:
                genre = genre_candidate
        except Exception:
            pass

    # Append result
    final_genre_list += [{'artist': artist, 'song_name': song_name, 'genre': genre}]

    # API rate limits
    sleep(0.5)

# Write to JSON file
with open('final_genre_tags.json', 'w') as file:
    json.dump(final_genre_list, file, indent=2)

