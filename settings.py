from pathlib import Path


#Wikiart
BASE_URL= "https://www.wikiart.org/"
STYLE_URL = "en/paintings-by-style/socialist-realism?json=2"
PAGINATION_URL = "page="


#timeout for WikiArt
# SEE https://github.com/lucasdavid/wikiart/blob/master/wikiart/settings.py
METADATA_REQUEST_TIMEOUT = 2 * 60
PAINTINGS_REQUEST_TIMEOUT = 5 * 60

#Local filepaths

ASSET_PATH = Path('assets')
print(ASSET_PATH.absolute())


#AWS Locations

BASE_BUCKET  = 'soviet-art-bot'
