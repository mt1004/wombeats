import json
from decimal import Decimal

from flask import Flask, redirect, request, session

from wombeats.models import SearchQuery
from wombeats.session import WombeatsSession

app = Flask(__name__)

app.secret_key = 'super secret key'.encode('utf-8')

wombeats_session = WombeatsSession(session)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


# Browser Endpoints

@app.route("/")
def login():
    # Checks spotify to see if the user is logged in
    # After successful login verification from spotify,
    # User is redirected to /api_callback (REDIRECT_URI)
    sp_oauth = wombeats_session.sp_oauth
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


@app.route("/index")
def index():
    if wombeats_session.is_logged_in():
        # This is the JS App entry point
        return redirect("/static/index.html")

    # If we can't verify the user is logged in the session, redirect back to '/' flow
    return redirect("/")


# 3rd party endpoints (Spotify)

@app.route("/api_callback")
def api_callback():
    # Spotify calls this API endpoint after successful login validation
    # This arg comes from spotify
    code = request.args.get('code')

    # Token = User code + sp_oauth (Developer token)
    sp_oauth = wombeats_session.sp_oauth
    token_info = sp_oauth.get_access_token(code)

    # Saving the access token into the user's cookies along with all other token related info
    wombeats_session.set_token_info(token_info)

    return redirect("index")


# API Endpoints called by Javascript code

@app.route("/search")
def search():
    print("*******searching")
    if not wombeats_session.is_logged_in():
        return redirect('/')

    api_access = wombeats_session.get_api_access()
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
