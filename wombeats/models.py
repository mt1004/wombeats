from decimal import Decimal
from typing import Optional
from pydantic import BaseModel


class SearchQuery(BaseModel):
    artist: str
    album: Optional[str]
    track: Optional[str]
    year: Optional[str]
    genre: Optional[str]
    from_bpm: Decimal
    to_bpm: Decimal

    @property
    def query_str(self):
        query_list = [f"artist:{self.artist}"]
        if self.album:
            query_list.append(f"album:{self.album}")
        if self.track:
            query_list.append(f"track:{self.track}")
        if self.year:
            query_list.append(f"year:{self.year}")
        return " ".join(query_parameter for query_parameter in query_list)


class SearchResult(BaseModel):
    artist: str
    album: str
    track: str
    release_date: str
    bpm: str
    track_uri: str
    external_url: str
