# Spotify Listening Trends and the Economic Climate

## Project Overview
This data science project investigates the relationship between Spotify users' listening trends and key macroeconomic indicators in the UK, including:
- Unemployment rates
- Inflation rates
- GDP fluctuations

**Primary Research Question**:  
*How do Spotify users' genre preferences vary with macroeconomic factors in the UK?*

## Repository Structure
```bash
group4-project/
│
├── analysis_notebooks/                             # Jupyter notebooks for analysis
│   ├── Analysis_VAR                                 # Vector Autoregression analysis
│   ├── ONS_EDA_Time                                 # Exploratory Data Analysis on ONS data
│   ├── SentimentAnalysis                            # Sentiment analysis on song titles
│   ├── Spotify_Genres_GDP_Analysis                  # Analysis of Quarterly Spotify Streams against GDP
│   ├── Spotify_Genres_Unemployment_Analysis         # Analysis of Quarterly Spotify Streams against Unemployment
│   ├── Spotify_vs_Inflation_analysis                # Analysis of Quarterly Spotify Streams against Inflation rates
│   └── ons_regression                               #  ONS data analysed using regression analysis
│
├── data/                                 # Data files (raw and processed)
│   ├── ONS/                              # Economic indicators data
│   │   └── ons_filtered
│   ├── images/                               # Images used in Jupyter notebooks
│   ├── GenreGroup_Lookup                    # Mapping of Broader Genre Categories to Original Genre Tags
│   ├── ons_genre_grouped_by_genregroup      # Quarterly Aggregation of Genre Groups (Excluding Detailed Genres)
│   ├── ons_genre_including_genregroup_new   # New Genre Files - Contains Spotify Data and ONS data- Cleaned Tags, Minimal 'Unknown' Tags, Enhanced Data Coverage (Generated via build_spotify_dataset.ipynb and spotift_dataset_new.csv)
│   ├── regional-gb-weekly-2024-01-04                 # Track-level dataset including Spotify URIs, artist names, and track titles.
│   ├── spotify_dataset_new                           # Song-level dataset including artist names, original genre tags and genre group classifications- Includes 'Unknown' Genre
│   ├── spotify_quarterly_merged                      # Quarterly - Dataset Containing Song data, Performer Names, Quarterly Streaming Figures, and Chart Rankings
│   └── weekly_gb_merged                              # Weekly Dataset Containing Song data, Performer Names, Region and Chart Rankings
│
├── build_datasets/
│   ├── spotify_dataset/                  # Create the Spotify dataset
│   │    ├── get_genretags/               # Python files for getting tags from APIs
│   │    ├── analysis_weekly_gb_merged    # Analysis of the weekly_gb_merged dataset
│   │    ├── build_spotify_dataset        # Includes Instructions of how to build the Spotify dataset
│   │    ├── final_merged_dataset         # Contains Artist information, Song name, Quarterly date and streams- merged dataset
│   └── build_ons_dataset                 # Create the ONS dataset
│
├── report.docx
└── README.md
```


### spotify_dataset/
* #### get_genretags
   - _build_genre_dataset.py_: Creates final_genre_tags.json from unique_tracks.csv. It extracts each song's detail and uses it to call AudioDB, Spotify and Last.fm APIs and request genre tags for each.
   - _final_genre_tags.json_: List of dictionaries with the following content: {"artist": "50 Cent","song_name": "In Da Club","genre": "Hip-Hop"}
   - _unique_tracks.csv_: Contains all unique songs that appear on the top 200 charts through the years
   - _spotify_connection.py_: Authorises the connection to Spotify API and creates an access token (**needs to be run before _build_genre_dataset.py_**)
   - _spotify_client_details.py_: Contains client details for the Spotify API requests.
   - _spotify_access_token.json_: Is used by build_genre_dataset.py to make requests to Spotify API
* #### Spotify_Quarterly/
* #### analysis_weekly_gb_merged
* #### build_spotify_dataset
* #### data_cleaning_spotify-checkpoint
* #### final_merged_dataset
* #### merged_bianca_nikki

### data/
* #### GenreGroup_Lookup/
* #### ons_genre_grouped_by_genregroup
* #### ons_genre_including_genregroup
* #### ons_genre_including_genregroup_new
* #### regional-gb-weekly-2024-01-04
* #### spotify_dataset
* #### spotify_dataset_new
* #### spotify_quarterly_merged
* #### weekly_gb_merged.csv

### Analysis/
* #### Analysis_VAR
   - Analysis of the interactions over time of unemployment and inflation with genre shares
* #### ONS_EDA_Time                    
* #### SentimentAnalysis
* #### Spotify_Genres_GDP_Analysis
* #### Spotify_Genres_Unemployment_Analysis    
* #### Spotify_vs_Inflation_analysis
* #### ons_regression

## Data Sources
1. **Music Data**:
   - [Historical charts data (2016-2022)](https://github.com/HipsterVizNinja/Spotify-Top-200)
   - Genre tags: [AudioDB](https://www.theaudiodb.com/free_music_api), [Spotify API](https://developer.spotify.com/documentation/web-api), [Last.fm](https://www.last.fm/api/show/track.getTags)

2. **Economic Indicators**:
   - [Office for National Statistics (ONS)](https://www.ons.gov.uk)


## How to Reproduce
1. Clone this repository:
   ```bash
   git clone git@github.com:Yrielu/group4-project.git
2. Run Analysis notebooks in order:
   1. ons_regression
   2. Spotify_vs_Inflation_analysis
   3. Spotify_Genres_Unemployment_Analysis
   4. Spotify_Genres_GDP_Analysis
   5. ONS_EDA_Time
   6. Analysis_VAR
   7. SentimentAnalysis   

## Contributors
- [Bianca](https://github.com/BiancaVendone)  
- [Nikki](https://github.com/NikkiHelliwell)
- [Becca](https://github.com/WithBecca)
- [Amina](https://github.com/aminai01)  
- [Amber](https://github.com/ambahaverly)  
- [Lisa](https://github.com/lisainscotland)  
- [Yrina](https://github.com/Yrielu)  

