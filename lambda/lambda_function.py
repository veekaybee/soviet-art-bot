import json
import boto3
import tempfile
import os


import random

from collections import defaultdict
from twython import Twython, TwythonError

session = boto3.Session()
s3_resource = boto3.resource('s3', region_name='us-east-1')
s3 = boto3.client('s3')
ssm = boto3.client('ssm')


def lambda_handler(event, context):
    bucket_name = 'soviet-art-bot'
    key = 'art_metadata.json'

    try:
        data = s3.get_object(Bucket=bucket_name, Key=key)
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
        img_link = "https://s3.amazonaws.com/soviet-art-bot/" + img_suffix

        try:
            indexed_json[img_link].append(values)
        except KeyError:
            indexed_json[img_link] = (values)


    metadata = random.choice(list(indexed_json.items()))

    url =  metadata[0]
    painter = metadata[1][0]
    title = metadata[1][1]
    year = metadata[1][2]

    print(url, painter, title,year)

    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

    try:

        tmp_dir = tempfile.gettempdir()
        path = os.path.join(tmp_dir, key)

        s3_resource.Bucket(bucket_name).download_file(img_suffix, path)
        print("file moved to /tmp")
        print(os.listdir(tmp_dir))

        with open("/tmp/%s" % object, 'rb') as img:
            print(img)
            twit_resp = twitter.upload_media(media=img)
            print(twit_resp)
            client.update_status(status="Heres more photos for u", media_ids=[twit_resp['media_id']])

    except TwythonError as e:
        print(e)



