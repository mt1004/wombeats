from decimal import Decimal
from typing import List

from spotipy import Spotify

from wombeats.api_models import SpotipyTrackItem, SpotipyPlaylist
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

        all_spotipy_track_items: List[SpotipyTrackItem] = []
        for track in results['tracks']['items']:
            track_item = SpotipyTrackItem(**track)
            all_spotipy_track_items.append(track_item)
        search_results = self.filter_track_items_by_bpm(all_spotipy_track_items,query)
        return search_results

    def filter_track_items_by_bpm(self, track_items:  List[SpotipyTrackItem], query: SearchQuery):
        search_results: List[SearchResult] = []
        for track_item in track_items:
            features = self.client.audio_features(track_item.uri)
            bpm_decimal = Decimal(features[0]["tempo"])
            if query.from_bpm <= bpm_decimal <= query.to_bpm:
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

    def get_current_playlists(self) -> List[SpotipyPlaylist]:
        playlists = self.client.current_user_playlists(offset=99)
        all_playlists = playlists["items"]
        spotipy_playlists: List[SpotipyPlaylist] = []
        for item in all_playlists:
            spotipy_playlist = SpotipyPlaylist(**item)
            spotipy_playlists.append(spotipy_playlist)
        return spotipy_playlists

    def _get_tracks_from_playlist(self, playlist_id:str) -> List[SpotipyTrackItem] :
        results = self.client.playlist(playlist_id, fields="tracks,next")
        list_of_tracks: List[SpotipyTrackItem] = []
        results_tracks = results["tracks"]
        # print(results_tracks)
        for item in results_tracks["items"]:
            track = item["track"]
            track_item = SpotipyTrackItem(**track)
            list_of_tracks.append(track_item)
        print(len(list_of_tracks))
        return list_of_tracks

    def filter_playlist_tracks(self, playlist_id:str, query: SearchQuery) -> List[SearchResult]:
        playlist_tracks = self._get_tracks_from_playlist(playlist_id)
        return self.filter_track_items_by_bpm(playlist_tracks, query=query)

    def filter_new_music_friday_playlist(self, query: SearchQuery) -> List[SearchResult]:
        playlist_tracks = self._get_tracks_from_playlist("6ev6yxufHeDvitWMugIwXy")
        return self.filter_track_items_by_bpm(playlist_tracks, query=query)

