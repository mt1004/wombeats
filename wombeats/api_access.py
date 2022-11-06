from decimal import Decimal
from typing import List

from spotipy import Spotify

from wombeats.api_models import SpotipyTrackItem, SpotipyPlaylist
from wombeats.models import SearchQuery, SearchResult
import logging
logger = logging.getLogger(__name__)


class SpotifyAPIAccess:
    @classmethod
    def build(cls, client: Spotify):
        return cls(client)

    def __init__(self, client: Spotify):
        self.client = client

    def search(self, query: SearchQuery, pagination: int = 50) -> List[SearchResult]:
        if query.genre:
            filtered_playlists = self.filter_current_playlists_by_name(query.genre)
            all_search_results = []
            for playlist in filtered_playlists:
                playlist_tracks = self._get_tracks_from_playlist(playlist.id)
                all_search_results.extend( self.filter_track_items_by_query(playlist_tracks, query))
            return all_search_results
        else:
            query_str = query.query_str
            results = self.client.search(q=query_str, limit=pagination)

            all_spotipy_track_items: List[SpotipyTrackItem] = []
            for track in results['tracks']['items']:
                track_item = SpotipyTrackItem(**track)
                all_spotipy_track_items.append(track_item)
            search_results = self.filter_track_items_by_query(all_spotipy_track_items, query)
            return search_results

    def pre_filter_tracks_by_search_query(self,
                                          track_items: List[SpotipyTrackItem],
                                          query: SearchQuery) -> List[SpotipyTrackItem]:
        if not query.artist and not query.album and not query.track and not query.year:
            return track_items

        filtered_artist_items = [track_item for track_item in track_items if
                 (query.artist and query.artist == track_item.artists[0].name)]
        final_track_items = self.validate_filtered_items(filtered_artist_items, track_items)
        filtered_album_items = [track_item for track_item in final_track_items if
                 (query.album and query.album == track_item.album.name)]
        final_track_items = self.validate_filtered_items(filtered_album_items, final_track_items)
        filtered_track_items = [track_item for track_item in final_track_items if
                 (query.track and query.track == track_item.name)]
        final_track_items = self.validate_filtered_items(filtered_track_items, final_track_items)
        filtered_year_items = [track_item for track_item in final_track_items if
                 (query.year and int(query.year) == track_item.album.release_date.year)]
        final_track_items = self.validate_filtered_items(filtered_year_items, final_track_items)
        return final_track_items

    @staticmethod
    def validate_filtered_items(filtered_items: List[SpotipyTrackItem], orig_track_items: List[SpotipyTrackItem] ):
        return filtered_items if len(filtered_items) > 0 else orig_track_items


    def filter_track_items_by_query(self, track_items:  List[SpotipyTrackItem], query: SearchQuery):
        search_results: List[SearchResult] = []
        pre_filtered_track_items = self.pre_filter_tracks_by_search_query(track_items, query)
        for track_item in pre_filtered_track_items:
            features = self.client.audio_features(track_item.uri)
            if not features or not features[0]:
                continue
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

    def get_current_playlists(self, offset: int = 0) -> List[SpotipyPlaylist]:
        logger.info("Getting current user playlists")
        playlists = self.client.current_user_playlists(offset=offset)
        all_playlists = playlists["items"]
        logger.info(f"Done getting current user playlists: size: {len(all_playlists)}")
        spotipy_playlists: List[SpotipyPlaylist] = []
        for item in all_playlists:
            spotipy_playlist = SpotipyPlaylist(**item)
            spotipy_playlists.append(spotipy_playlist)
        return spotipy_playlists

    def filter_current_playlists_by_name(self, name:str) -> List[SpotipyPlaylist]:
        offset = 0
        all_playlists = []
        while offset < 200:
            all_playlists.extend(self.get_current_playlists(offset=offset))
            offset = offset + 49
        return [playlist for playlist in all_playlists if name == playlist.name]

    def _get_tracks_from_playlist(self, playlist_id:str) -> List[SpotipyTrackItem] :
        results = self.client.playlist(playlist_id, fields="tracks,next")
        list_of_tracks: List[SpotipyTrackItem] = []
        results_tracks = results["tracks"]

        for item in results_tracks["items"]:
            track = item["track"]
            track_item = SpotipyTrackItem(**track)
            list_of_tracks.append(track_item)

        return list_of_tracks

    def filter_playlist_tracks(self, playlist_id:str, query: SearchQuery) -> List[SearchResult]:
        playlist_tracks = self._get_tracks_from_playlist(playlist_id)
        return self.filter_track_items_by_query(playlist_tracks, query=query)

    def filter_new_music_friday_playlist(self, query: SearchQuery) -> List[SearchResult]:
        playlist_tracks = self._get_tracks_from_playlist("6ev6yxufHeDvitWMugIwXy")
        return self.filter_track_items_by_query(playlist_tracks, query=query)


