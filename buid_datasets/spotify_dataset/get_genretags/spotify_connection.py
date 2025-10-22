import requests
import base64
from spotify_client_details import Client_ID, Client_SECRET
import json


''''
Run this file to send an authorisation request and get the access token that will allow to make API calls.

All requests to Spotify Web API require authorisation. 
This file follows the Client Credential Flow, the code was witten following the instructions in: https://developer.spotify.com/documentation/web-api/tutorials/client-credentials-flow
'''

# 1. Get client details
client_id = Client_ID
client_secret = Client_SECRET

# 2. Build authorisation request
auth_details = f"{client_id}:{client_secret}".encode('utf-8')
auth_base64 = base64.b64encode(auth_details).decode('utf-8')

header_params = {
    "Authorization": f"Basic {auth_base64}",
    "Content-Type": "application/x-www-form-urlencoded"
}

body_params = {
    "grant_type": "client_credentials"
}

# 3. Send authorisation request
auth_response = requests.post("https://accounts.spotify.com/api/token", headers=header_params, data=body_params)

# 4. Save access token
with open('spotify_access_token.json', 'w') as file:
    json.dump(auth_response.json(), file, indent=2)

print(f'\nThis program has finished running. Your access token has been successfully saved to spotify_access_token.json!')
