# wombeats

wombeats gives you songs in BPMs


## Local Development Setup
#### Install Poetry
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
```
#### Configure Environment Variables
| Name   |  Value |
|----------|:-----------------------------------------------------------------------------------------------|
|SPOTIPY_CLIENT_ID |  Go to "Dashboard" at [Spotify Developer](https://developer.spotify.com/) |
| SPOTIPY_CLIENT_SECRET |    Go to "Dashboard" at [Spotify Developer](https://developer.spotify.com/)   | 
| FLASK_APP | wombeats |
1. Run `poetry install` to install all package dependencies
2. Run `poetry env info` to see where virtual env is installed locally
3. Run `poetry run flask run` at wombeats root directory

