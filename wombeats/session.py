import time

import spotipy
from flask import session

from wombeats.constants import CLI_ID, CLI_SEC, REDIRECT_URI, SCOPE


class WombeatsSession:
    def __init__(self, session: session):
        self.session = session

    def is_logged_in(self):
        session['token_info'] = self.get_token()
        return 'token_info' in session

    def set_token_info(self, token_info):
        self.session["token_info"] = token_info

    def get_token(self):
        token_info = self.session.get("token_info", {})

        # Checking if the session already has a token stored
        if not (self.session.get('token_info', False)):
            return token_info

        # Checking if token has expired
        now = int(time.time())
        is_token_expired = self.session.get('token_info').get('expires_at') - now < 60

        # Refreshing token if it has expired
        if is_token_expired:
            sp_oauth = spotipy.oauth2.SpotifyOAuth(
                client_id=CLI_ID,
                client_secret=CLI_SEC,
                redirect_uri=REDIRECT_URI,
                scope=SCOPE
            )

            token_info = sp_oauth.refresh_access_token(self.session.get('token_info').get('refresh_token'))

        return token_info
