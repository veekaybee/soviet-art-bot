import pytest
import os

from soviet_art_bot import download_images as dl
from soviet_art_bot import settings


# Tests that WikiArt responds with a JSON object
@pytest.mark.order1
def test_json():
    assert type(dl.get_json()) == list

# Tests that JSON file is saved correctly
@pytest.mark.order2
def test_save_json():
    assert settings.ASSET_PATH.joinpath(settings.JSON_FILE+settings.JSON_SUFFIX).is_file()





