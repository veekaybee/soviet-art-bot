import pytest
import os

import soviet_art_bot.soviet_art_bot.download_images as dl
import settings


# Test JSON
single_painting = [{'artistName': 'Aleksandr Deyneka', 'images': None, 'width': 634, 'artistUrl': '/en/aleksandr-deyneka', 'albums': None, 'title': 'Winter in Kursk', 'id': '577271cfedc2cb3880c2de61', 'year': '1916', 'height': 750, 'paintingUrl': '/en/aleksandr-deyneka/winter-in-kursk-1916', 'flags': 2, 'image': 'https://uploads8.wikiart.org/images/aleksandr-deyneka/winter-in-kursk-1916.jpg', 'map': '0123**67*'}]
add_painting = [{'artistName': 'Konstantin Yuon', 'images': None, 'width': 776, 'artistUrl': '/en/konstantin-yuon', 'albums': None, 'title': 'The Symphony of Action', 'id': '57727792edc2cb3880d4f131', 'year': '1922', 'height': 650, 'paintingUrl': '/en/konstantin-yuon/the-symphony-of-action-1922', 'flags': 2, 'image': 'https://uploads4.wikiart.org/images/konstantin-yuon/the-symphony-of-action-1922.jpg', 'map': '0123**67*'}]


def test_build_url():
    url = settings.BASE_URL + settings.STYLE_URL + "&" + settings.PAGINATION_URL + str(1)
    assert url == "https://www.wikiart.org/en/paintings-by-style/socialist-realism?json=2&page=1"


# Tests that paintings are extracted and added to a list
def test_parse_data():
    dl.parse_data(single_painting, add_painting)
    assert len(single_painting) == 2







