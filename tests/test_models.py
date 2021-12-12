from wombeats.models import SearchQuery


def test_query_str_album_property():
    artist_album_query = SearchQuery(artist="Taylor Swift",
                                     album="Red")
    assert artist_album_query.query_str == "artist:Taylor Swift album:Red"


def test_query_str_year_property():
    artist_year_query = SearchQuery(artist="Taylor Swift",
                                    year=2021)
    assert artist_year_query.query_str == "artist:Taylor Swift year:2021"
