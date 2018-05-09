from pathlib import Path
from dotenv import load_dotenv

# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')

# Load file from the path.
load_dotenv(dotenv_path)

# Twitter Keys

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')


#Wikiart
BASE_URL= "https://www.wikiart.org/"
STYLE_URL = "en/paintings-by-style/socialist-realism?json=2"
PAGINATION_URL = "page="


#timeout for WikiArt
# SEE https://github.com/lucasdavid/wikiart/blob/master/wikiart/settings.py
METADATA_REQUEST_TIMEOUT = 2 * 60
PAINTINGS_REQUEST_TIMEOUT = 5 * 60

#Local filepaths
TOP_LEVEL_PATH = Path('/Users/vboykis/Desktop/soviet_art_bot/')
ASSET_PATH = TOP_LEVEL_PATH/ 'assets'

# Metadata filename

METADATA_FILENAME = 'art_metadata.json'
MEDTADATA_FILE = ASSET_PATH.joinpath(METADATA_FILENAME)


#AWS Locations

BASE_BUCKET  = 'soviet-art-bot'


