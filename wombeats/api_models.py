from typing import List, Optional
from pydantic import BaseModel, HttpUrl, validator
from datetime import datetime, date


class SpotipyAlbum(BaseModel):
    name: str
    release_date: Optional[date]
    uri: str

    @validator("release_date", pre=True)
    def parse_release_date(cls, value):
        splits = value.split("-")

        if len(splits) == 2:
            date_format = "%Y-%m"
        else:
            date_format = "%Y-%m-%d"

        return datetime.strptime(
            value,
            date_format
        ).date()



class SpotipyArtist(BaseModel):
    name: str
    uri: str


class ExternalURL(BaseModel):
    spotify: HttpUrl


class SpotipyTrackItem(BaseModel):
    album: SpotipyAlbum
    artists: List[SpotipyArtist]
    name: str
    external_urls: ExternalURL
    uri: str


class SpotipyPlaylistTrack(BaseModel):
    total: int


class SpotipyPlaylist(BaseModel):
    name: str
    id: str
    tracks: SpotipyPlaylistTrack
