import unittest
from decimal import Decimal

import spotipy

from wombeats.api_access import SpotifyAPIAccess
from wombeats.constants import SCOPE
from wombeats.models import SearchQuery
import os


class SpotipyPlaylistApiTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        client_id = os.environ.get('SPOTIPY_CLIENT_ID')
        client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
        redirect_uri = "http://localhost:8888/callback"
        scope = SCOPE
        sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id=client_id,
                                                                client_secret=client_secret,
                                                                redirect_uri=redirect_uri,
                                                                scope=scope,
                                                                show_dialog=False))
        self.spotify = sp

    def test_api_access_search_by_artist(self):
        api_access = SpotifyAPIAccess.build(client=self.spotify)
        sq = SearchQuery(
            artist="Twenty One Pilots",
            from_bpm=Decimal(90),
            to_bpm=Decimal(100)
        )
        search_results = api_access.search(sq)
        assert len(search_results) >= 0
        for sr in search_results:
            assert sr.bpm_decimal.compare(90) >= 0
            assert sr.bpm_decimal.compare(101) == -1
        assert search_results[0].artist == "Twenty One Pilots"

    def test_api_access_search_by_artist_and_year(self):
        api_access = SpotifyAPIAccess.build(client=self.spotify)
        sq = SearchQuery(
            artist="Twenty One Pilots",
            year=2015,
            from_bpm=Decimal(90),
            to_bpm=Decimal(100)
        )
        search_results = api_access.search(sq)
        assert search_results[0].bpm_decimal.compare(90) >= 0
        assert search_results[0].bpm_decimal.compare(101) == -1
        assert search_results[0].release_date_year == 2015

    def test_api_access_search_by_artist_and_album(self):
        api_access = SpotifyAPIAccess.build(client=self.spotify)
        sq = SearchQuery(
            artist="Twenty One Pilots",
            album="Blurryface",
            year=2015,
            from_bpm=Decimal(90),
            to_bpm=Decimal(100)
        )
        search_results = api_access.search(sq)
        assert search_results[0].bpm_decimal.compare(90) >= 0
        assert search_results[0].bpm_decimal.compare(101) == -1
        assert search_results[0].album == "Blurryface"

    def test_api_access_get_current_playlists(self):
        api_access = SpotifyAPIAccess.build(client=self.spotify)
        playlists = api_access.get_current_playlists()
        assert playlists


    def test_api_access_read_tracks_from_playlist(self):
        api_access = SpotifyAPIAccess.build(client=self.spotify)
        tracks = api_access._get_tracks_from_playlist("7jd5fwnsmhrzDw7HsVg0RD")
        print(tracks)

    def test_api_access_filter_playlist(self):
        api_access = SpotifyAPIAccess.build(client=self.spotify)
        sq = SearchQuery(
            from_bpm=Decimal(70),
            to_bpm=Decimal(100)
        )
        search_results = api_access.filter_playlist_tracks("7jd5fwnsmhrzDw7HsVg0RD", query=sq)
        print(search_results)
        assert search_results[0].bpm_decimal.compare(70) >= 0

    def test_api_access_filter_new_music_friday_playlist(self):
        api_access = SpotifyAPIAccess.build(client=self.spotify)
        sq = SearchQuery(
            from_bpm=Decimal(70),
            to_bpm=Decimal(100)

        )
        search_results = api_access.filter_new_music_friday_playlist(query=sq)
        print(search_results)
        print(len(search_results))
        assert search_results[0].bpm_decimal.compare(70) >= 0

    def test_api_access_search_by_playlist(self):
        api_access = SpotifyAPIAccess.build(client=self.spotify)
        sq = SearchQuery(
            genre="New Music Friday",
            from_bpm=Decimal(90),
            to_bpm=Decimal(100)
        )
        search_results = api_access.search(sq)
        print(search_results)