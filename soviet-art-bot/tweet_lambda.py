import json
import boto3
import tempfile
import os
from subprocess import call
import random

from collections import defaultdict
from twython import Twython, TwythonError

session = boto3.Session()
s3_resource = boto3.resource('s3', region_name='us-east-1')
s3 = boto3.client('s3')
ssm = boto3.client('ssm')


def lambda_handler(event, context):
    bucket_name = 'soviet-art-bot'
    metadata = 'art_metadata.json'

    try:
        data = s3.get_object(Bucket=bucket_name, Key=metadata)
        json_data = json.loads(data['Body'].read().decode('utf-8'))

    except Exception as e:
        print(e)
        raise e

    CONSUMER_KEY = ssm.get_parameter(Name='CONSUMER_KEY')['Parameter']['Value']
    CONSUMER_SECRET = ssm.get_parameter(Name='CONSUMER_SECRET')['Parameter']['Value']
    ACCESS_TOKEN = ssm.get_parameter(Name='ACCESS_TOKEN')['Parameter']['Value']
    ACCESS_SECRET = ssm.get_parameter(Name='ACCESS_SECRET')['Parameter']['Value']

    indexed_json = defaultdict()

    for value in json_data:
        artist = value['artistName']
        title = value['title']
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

    single_image_metadata = random.choice(list(indexed_json.items()))

    url = single_image_metadata[0]
    painter = single_image_metadata[1][0]
    title = single_image_metadata[1][1]
    year = single_image_metadata[1][2]

    print(url, painter, title, year)

    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

    try:

        tmp_dir = tempfile.gettempdir()
        call('rm -rf /tmp/*', shell=True)
        path = os.path.join(tmp_dir, url)
        print(path)

        s3_resource.Bucket(bucket_name).download_file(url, path)
        print("file moved to /tmp")
        print(os.listdir(tmp_dir))

        with open(path, 'rb') as img:
            print("Path", path)
            twit_resp = twitter.upload_media(media=img)
            twitter.update_status(status="\"%s\"\n%s, %s" % (title, painter, year), media_ids=twit_resp['media_id'])

    except TwythonError as e:
        print(e)



