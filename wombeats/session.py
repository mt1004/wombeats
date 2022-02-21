import time

import spotipy
from flask import session

from wombeats.constants import CLI_ID, CLI_SEC, REDIRECT_URI, SCOPE


class WombeatsSession:
    def __init__(self, session: session):
        self.session = session

        # One dev auth session per client
        self.sp_oauth = spotipy.oauth2.SpotifyOAuth(
            client_id=CLI_ID,
            client_secret=CLI_SEC,
            redirect_uri=REDIRECT_URI,
            scope=SCOPE
        )

    def is_logged_in(self):
        return bool(self.get_token())

    def set_token_info(self, token_info):
        self.session["token_info"] = token_info

    def _is_token_expired(self):
        now = int(time.time())
        is_token_expired = self.session.get('token_info').get('expires_at') - now < 60

        return is_token_expired

    def _refresh_token(self):
        token_info = self.sp_oauth.refresh_access_token(self.session.get('token_info').get('refresh_token'))
        self.session['token_info'] = token_info

    def get_token(self):
        if self._is_token_expired():
            self._refresh_token()

        token_info = self.session.get("token_info", None)

        return token_info
