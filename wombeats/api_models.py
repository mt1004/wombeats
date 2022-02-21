from typing import List

from pydantic import BaseModel, HttpUrl
from datetime import date


class SpotipyAlbum(BaseModel):
    name: str
    release_date: date
    uri: str


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
