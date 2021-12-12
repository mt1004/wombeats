from flask import Flask, render_template, redirect, request, session
import spotipy
import spotipy.util as util
import time
import json
import urllib3
import os

app = Flask(__name__)

from spotipy.oauth2 import SpotifyClientCredentials

app.secret_key = 'super secret key'.encode('utf-8')

API_BASE = 'https://accounts.spotify.com'
CLI_ID = '09f8a8b99b0d4f1c804753c3c5451f09'
CLI_SEC = '060ad82b313f4864b748c80f550a5cbc'

# Make sure you add this to Redirect URIs in the setting of the application dashboard
REDIRECT_URI = "http://127.0.0.1:5000/api_callback"

SCOPE = 'playlist-modify-private,playlist-modify-public,user-top-read'

# Set this to True for testing but you probaly want it set to False in production.
SHOW_DIALOG = True


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
    if 'token_info' in session:
        auth_manager = SpotifyClientCredentials()
        sp = spotipy.Spotify(auth_manager=auth_manager)
        return redirect("/static/build/index.html")

    return 'logged in?'


# authorization-code-flow Step 2.
# Have your application request refresh and access tokens;
# Spotify returns access and refresh tokens
@app.route("/api_callback")
def api_callback():
    # Don't reuse a SpotifyOAuth object because they store token info and you could leak user tokens if you reuse a SpotifyOAuth object
    sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id=CLI_ID, client_secret=CLI_SEC, redirect_uri=REDIRECT_URI,
                                           scope=SCOPE)
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)

    # Saving the access token along with all other token related info
    session["token_info"] = token_info

    return redirect("index")


# authorization-code-flow Step 3.
# Use the access token to access the Spotify Web API;
# Spotify returns requested data
@app.route("/go", methods=['POST'])
def go():
    session['token_info'], authorized = get_token(session)
    session.modified = True
    if not authorized:
        return redirect('/')
    data = request.form
    sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))
    response = sp.current_user_top_tracks(limit=data['num_tracks'], time_range=data['time_range'])

    # print(json.dumps(response))

    return render_template("results.html", data=data)


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


if __name__ == "__main__":
    app.run(debug=True)

