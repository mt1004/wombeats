import json
import time
from decimal import Decimal

import spotipy
from flask import Flask, redirect, request, session
from spotipy.oauth2 import SpotifyClientCredentials

from wombeats.api_access import SpotifyAPIAccess
from wombeats.constants import CLI_ID, CLI_SEC, REDIRECT_URI, SCOPE
from wombeats.models import SearchQuery

app = Flask(__name__)

app.secret_key = 'super secret key'.encode('utf-8')
# Set this to True for testing but you probaly want it set to False in production.
SHOW_DIALOG = True


def is_logged_in():
    session['token_info'], authorized = get_token(session)
    return 'token_info' in session


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


# authorization-code-flow Step 1. Have your application request authorization;
# the user logs in and authorizes access
@app.route("/login")
def verify():
    return '<h1>Welcome</h1>Please click <a href="/login">here</a> to log in.'


@app.route("/")
def login():
    # Don't reuse a SpotifyOAuth object because they store token info and you could leak user tokens if you reuse a SpotifyOAuth object
    sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id=CLI_ID, client_secret=CLI_SEC, redirect_uri=REDIRECT_URI,
                                           scope=SCOPE)
    auth_url = sp_oauth.get_authorize_url()
    print(auth_url)
    return redirect(auth_url)


@app.route("/index")
def index():
    session['token_info'], authorized = get_token(session)
    if is_logged_in():
        return redirect("/static/index.html")

    return redirect("/")


@app.route("/search")
def search():
    if not is_logged_in():
        return redirect('/')

    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)
    print('***session', session)
    api_access = SpotifyAPIAccess.build(client=sp)
    search_query = SearchQuery(
        artist=request.args.get('artist'),
        album=request.args.get('album'),
        track=request.args.get('track'),
        year=request.args.get('year'),
        genre=request.args.get('genre'),
        from_bpm=request.args.get('fromBpm') or Decimal(0),
        to_bpm=request.args.get('toBpm') or Decimal(500),
    )

    search_results = api_access.search(search_query)
    sorted_search_results = sorted(search_results, key=lambda row: int(row.bpm))
    results = json.dumps([result.dict() for result in sorted_search_results])
    print(results)
    return results


# authorization-code-flow Step 2.
# Have your application request refresh and access tokens;
# Spotify returns access and refresh tokens
@app.route("/api_callback")
def api_callback():
    # Don't reuse a SpotifyOAuth object because they store token info and you could leak user tokens if you reuse a SpotifyOAuth object
    sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id=CLI_ID, client_secret=CLI_SEC, redirect_uri=REDIRECT_URI,
                                           scope=SCOPE)
    auth_manager = SpotifyClientCredentials()
    auth_token = auth_manager.get_access_token()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)

    # Saving the access token along with all other token related info
    session["token_info"] = token_info
    print('Session, auth_token, token info is: ', session, auth_token, session['token_info'])

    return redirect("index")


# Checks to see if token is valid and gets a new token if not
def get_token(session):
    token_valid = False
    token_info = session.get("token_info", {})

    # Checking if the session already has a token stored
    if not (session.get('token_info', False)):
        token_valid = False
        return token_info, token_valid

    # Checking if token has expired
    now = int(time.time())
    is_token_expired = session.get('token_info').get('expires_at') - now < 60

    # Refreshing token if it has expired
    if (is_token_expired):
        # Don't reuse a SpotifyOAuth object because they store token info and you could leak user tokens if you reuse a SpotifyOAuth object
        sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id=CLI_ID, client_secret=CLI_SEC, redirect_uri=REDIRECT_URI,
                                               scope=SCOPE)
        token_info = sp_oauth.refresh_access_token(session.get('token_info').get('refresh_token'))

    token_valid = True
    return token_info, token_valid
