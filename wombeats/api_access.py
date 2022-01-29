from decimal import Decimal
from typing import List

from spotipy import Spotify

from wombeats.api_models import SpotipyTrackItem
from wombeats.models import SearchQuery, SearchResult


class SpotifyAPIAccess:
    @classmethod
    def build(cls, client: Spotify):
        return cls(client)

    def __init__(self, client: Spotify):
        self.client = client

    def search(self, query: SearchQuery, pagination: int = 50) -> List[SearchResult]:
        query_str = query.query_str
        results = self.client.search(q=query_str, limit=pagination)
        search_results: List[SearchResult] = []
        for idx, track in enumerate(results['tracks']['items']):
            features = self.client.audio_features(track["uri"])
            bpm_decimal = Decimal(features[0]["tempo"])
            if query.from_bpm <= bpm_decimal <= query.to_bpm:
                track_item = SpotipyTrackItem(**track)
                search_result = SearchResult(
                    artist=track_item.artists[0].name,
                    album= track_item.album.name,
                    track=track_item.name,
                    track_uri=str(track_item.uri),
                    release_date=str(track_item.album.release_date),
                    bpm=str(int(bpm_decimal)),
                    external_url=str(track_item.external_urls.spotify)
                )
                search_results.append(search_result)
        return search_results

    def get_user_playlists(self):
        return self.client.current_user_playlists()
