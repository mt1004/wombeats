import time

import spotipy
from flask import session

from wombeats.api_access import SpotifyAPIAccess
from wombeats.constants import CLI_ID, CLI_SEC, REDIRECT_URI, SCOPE


class WombeatsSpotipySession:
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
        return bool(self._get_token())

    def login(self, code):
        token_info = self.sp_oauth.get_access_token(code)
        self.session["token_info"] = token_info

    def get_authorize_url(self) -> str:
        sp_oauth = self.sp_oauth
        auth_url = sp_oauth.get_authorize_url()

        return auth_url

    def get_api_access(self) -> SpotifyAPIAccess:
        token = self._get_token()
        if not token:
            return None

        sp = spotipy.Spotify(auth=token.get('access_token'))
        api_access = SpotifyAPIAccess.build(client=sp)

        return api_access

    def _is_token_expired(self):
        now = int(time.time())
        token_info = self.session.get('token_info')
        is_token_expired = False
        if token_info:
            is_token_expired = token_info.get('expires_at') - now < 60

        return is_token_expired

    def _refresh_token(self):
        original_token_info = self.session.get('token_info')
        if not original_token_info:
            return

        token_info = self.sp_oauth.refresh_access_token(original_token_info.get('refresh_token'))
        self.session['token_info'] = token_info

    def _get_token(self):
        if self._is_token_expired():
            self._refresh_token()

        token_info = self.session.get("token_info", None)

        return token_info
