from wombeats.api_models import SpotipyTrackItem


def test_spotipy_track_item():
    track_item_dict = {
        'album': {
            'album_type': 'album',
            'artists': [{
                'external_urls': {
                    'spotify': 'https://open.spotify.com/artist/3YQKmKGau1PzlVlkL1iodx'
                },
                'href': 'https://api.spotify.com/v1/artists/3YQKmKGau1PzlVlkL1iodx',
                'id': '3YQKmKGau1PzlVlkL1iodx',
                'name': 'Twenty One Pilots',
                'type': 'artist',
                'uri': 'spotify:artist:3YQKmKGau1PzlVlkL1iodx'
            }
            ],
            'available_markets': ['AD', 'AE', 'AG', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BB', 'BD', 'BE',
                                  'BF', 'BG', 'BH', 'BI', 'BJ', 'BN', 'BO', 'BR', 'BS', 'BW', 'BY', 'BZ', 'CA', 'CD',
                                  'CG', 'CH', 'CI', 'CL', 'CM', 'CO', 'CR', 'CV', 'CW', 'CY', 'CZ', 'DE', 'DJ', 'DK',
                                  'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FJ', 'FM', 'FR', 'GA', 'GB', 'GD',
                                  'GH', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GW', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE',
                                  'IL', 'IN', 'IQ', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KM', 'KN', 'KR',
                                  'KW', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA',
                                  'MC', 'MD', 'ME', 'MG', 'MK', 'ML', 'MN', 'MO', 'MR', 'MT', 'MU', 'MW', 'MX', 'MY',
                                  'MZ', 'NA', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NZ', 'OM', 'PA', 'PE', 'PG', 'PH',
                                  'PK', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'RS', 'RU', 'RW', 'SA', 'SC', 'SE', 'SG',
                                  'SI', 'SK', 'SL', 'SM', 'SN', 'ST', 'SV', 'SZ', 'TD', 'TG', 'TH', 'TJ', 'TL', 'TN',
                                  'TR', 'TT', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VC', 'VE', 'VN', 'XK', 'ZA',
                                  'ZM', 'ZW'],
            'external_urls': {
                'spotify': 'https://open.spotify.com/album/3cQO7jp5S9qLBoIVtbkSM1'
            },
            'href': 'https://api.spotify.com/v1/albums/3cQO7jp5S9qLBoIVtbkSM1',
            'id': '3cQO7jp5S9qLBoIVtbkSM1',
            'images': [{
                'height': 640,
                'url': 'https://i.scdn.co/image/ab67616d0000b273de03bfc2991fd5bcfde65ba3',
                'width': 640
            }, {
                'height': 300,
                'url': 'https://i.scdn.co/image/ab67616d00001e02de03bfc2991fd5bcfde65ba3',
                'width': 300
            }, {
                'height': 64,
                'url': 'https://i.scdn.co/image/ab67616d00004851de03bfc2991fd5bcfde65ba3',
                'width': 64
            }
            ],
            'name': 'Blurryface',
            'release_date': '2015-05-15',
            'release_date_precision': 'day',
            'total_tracks': 14,
            'type': 'album',
            'uri': 'spotify:album:3cQO7jp5S9qLBoIVtbkSM1'
        },
        'artists': [{
            'external_urls': {
                'spotify': 'https://open.spotify.com/artist/3YQKmKGau1PzlVlkL1iodx'
            },
            'href': 'https://api.spotify.com/v1/artists/3YQKmKGau1PzlVlkL1iodx',
            'id': '3YQKmKGau1PzlVlkL1iodx',
            'name': 'Twenty One Pilots',
            'type': 'artist',
            'uri': 'spotify:artist:3YQKmKGau1PzlVlkL1iodx'
        }
        ],
        'available_markets': ['AD', 'AE', 'AG', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF',
                              'BG', 'BH', 'BI', 'BJ', 'BN', 'BO', 'BR', 'BS', 'BW', 'BY', 'BZ', 'CA', 'CD', 'CG', 'CH',
                              'CI', 'CL', 'CM', 'CO', 'CR', 'CV', 'CW', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ',
                              'EC', 'EE', 'EG', 'ES', 'FI', 'FJ', 'FM', 'FR', 'GA', 'GB', 'GD', 'GH', 'GM', 'GN', 'GQ',
                              'GR', 'GT', 'GW', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IS', 'IT',
                              'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KM', 'KN', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LC', 'LI',
                              'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MG', 'MK', 'ML', 'MN',
                              'MO', 'MR', 'MT', 'MU', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP',
                              'NZ', 'OM', 'PA', 'PE', 'PG', 'PH', 'PK', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'RS', 'RU',
                              'RW', 'SA', 'SC', 'SE', 'SG', 'SI', 'SK', 'SL', 'SM', 'SN', 'ST', 'SV', 'SZ', 'TD', 'TG',
                              'TH', 'TJ', 'TL', 'TN', 'TR', 'TT', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VC', 'VE',
                              'VN', 'XK', 'ZA', 'ZM', 'ZW'],
        'disc_number': 1,
        'duration_ms': 202333,
        'explicit': False,
        'external_ids': {
            'isrc': 'USAT21500597'
        },
        'external_urls': {
            'spotify': 'https://open.spotify.com/track/3CRDbSIZ4r5MsZ0YwxuEkn'
        },
        'href': 'https://api.spotify.com/v1/tracks/3CRDbSIZ4r5MsZ0YwxuEkn',
        'id': '3CRDbSIZ4r5MsZ0YwxuEkn',
        'is_local': False,
        'name': 'Stressed Out',
        'popularity': 86,
        'preview_url': 'https://p.scdn.co/mp3-preview/0e0951b811f06fea9162eb7e95e4bae4802d97af?cid=7a525dbfd0e545358c1d7546b741d1a7',
        'track_number': 2,
        'type': 'track',
        'uri': 'spotify:track:3CRDbSIZ4r5MsZ0YwxuEkn'
    }

    track_item = SpotipyTrackItem(**track_item_dict)
    assert track_item.album.name == "Blurryface"
    assert track_item.artists[0].name == "Twenty One Pilots"
    assert track_item.name == "Stressed Out"
    assert track_item.external_urls.spotify == "https://open.spotify.com/track/3CRDbSIZ4r5MsZ0YwxuEkn"
    assert track_item.uri == "spotify:track:3CRDbSIZ4r5MsZ0YwxuEkn"

