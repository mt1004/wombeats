import unittest
from decimal import Decimal

import spotipy

from wombeats.api_access import SpotifyAPIAccess
from wombeats.models import SearchQuery
import os


class SpotipyPlaylistApiTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        client_id = os.environ.get('SPOTIPY_CLIENT_ID')
        client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
        sp = spotipy.Spotify(auth_manager=spotipy.SpotifyClientCredentials(client_id=client_id,
                                                                           client_secret=client_secret))
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
            assert sr.bpm.compare(90) >= 0
            assert sr.bpm.compare(101) == -1
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
        print(search_results)
        assert search_results[0].bpm.compare(90) >= 0
        assert search_results[0].bpm.compare(101) == -1
        assert search_results[0].release_date.year == 2015

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
        assert search_results[0].bpm.compare(90) >= 0
        assert search_results[0].bpm.compare(101) == -1
        assert search_results[0].album == "Blurryface"

