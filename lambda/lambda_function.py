#system imports
import json
import boto3
from botocore.exceptions import ClientError
import tempfile
import os
import subprocess
from six.moves.html_parser import HTMLParser
import random
import dotenv

dotenv.load_dotenv(os.path.join(here, "../.env"))
dotenv.load_dotenv(os.path.join(here, "../../.env"))

from collections import defaultdict
from twython import Twython, TwythonError
import html

from settings import CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET

session = boto3.Session()
s3_resource = boto3.resource('s3', region_name='us-east-1')
s3 = boto3.client('s3')
ssm = boto3.client('ssm')
h = HTMLParser()


def lambda_handler(event, context):
    bucket_name = 'soviet-art-bot'
    key = 'art_metadata.json'

    try:
        # load json metadata from S3 bucket into JSON
        data = s3.get_object(Bucket=bucket_name, Key=key)
        json_data = json.loads(data['Body'].read().decode('utf-8'))
    except Exception as e:
        print(e)
        raise e

    # Create .env file path.
    dotenv_path = join(dirname(__file__), '.env')

    # Load file from the path.
    load_dotenv(dotenv_path)

    # Twitter Keys

    CONSUMER_KEY = os.getenv('CONSUMER_KEY')
    CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    ACCESS_SECRET = os.getenv('ACCESS_SECRET')

    # Twitter Keys
    # CONSUMER_KEY = settings.CONSUMER_KEY
    # CONSUMER_SECRET = settings.CONSUMER_SECRET
    # ACCESS_TOKEN = settings.ACCESS_TOKEN
    # ACCESS_SECRET = settings.ACCESS_SECRET


    # CONSUMER_SECRET = ssm.get_parameter(Name='CONSUMER_SECRET_TEST')['Parameter']['Value']
    # ACCESS_TOKEN = ssm.get_parameter(Name='ACCESS_TOKEN_TEST')['Parameter']['Value']
    # ACCESS_SECRET = ssm.get_parameter(Name='ACCESS_SECRET_TEST')['Parameter']['Value']

    print("Got keys")

    indexed_json = defaultdict()

    html_escape_table = {"&": "&amp;",'"': "&quot;", "'": "&amp;#39;", "'": "&#39;", ">": "&gt;","<": "&lt;","&": "&amp;"}

    def html_escape(text):
        """Produce entities within text."""
        return "".join(html_escape_table.get(c, c) for c in text)

    for value in json_data:
        artist = value['artistName']
        title = value['title']
        title = html.escape(title)
        year = value['year']
        values = [artist, title, year]

        # return only image name at end of URL
        find_index = value['image'].rfind('/')
        img_suffix = value['image'][find_index + 1:]
        img_link = img_suffix

        try:
            indexed_json[img_link].append(values)
        except KeyError:
            indexed_json[img_link] = (values)

    # Shuffle images
    single_image_metadata = random.choice(list(indexed_json.items()))

    url = single_image_metadata[0]
    painter = single_image_metadata[1][0]
    title= single_image_metadata[1][1]
    year = single_image_metadata[1][2]

    print(url, painter, title,year)

    # Connect to Twitter via Twython
    try:
        twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
        print(twitter)
    except TwythonError as e:
        print(e)

    #Try tweeting
    try:

        tmp_dir = tempfile.gettempdir()
        # subprocess.call('rm -rf /tmp/*', shell=True)
        path = os.path.join(tmp_dir, url)
        print(path)

        # Try to match URL in filepath to URL in metadata; if it doesn't work, try another one
        for i in range(0, 3):
                try:
                    x = s3_resource.Bucket(bucket_name).download_file(url, path)
                    print("file moved to /tmp")
                    print(os.listdir(tmp_dir))

                    with open(path, 'rb') as img:
                        print("Path", path)
                        twit_resp = twitter.upload_media(media=img)
                        twitter.update_status(status="\"%s\"\n%s, %s" % (title, painter, year),
                                              media_ids=twit_resp['media_id'])
                except ClientError as e:
                    if e.response['Error']['Code'] == 'ResourceNotFoundException':
                        continue
                break


    except TwythonError as e:
        print(e)



