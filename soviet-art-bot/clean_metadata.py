"""
Opens S3 bucket with metadata, pull it into memory for use in bot

Pulls in JSON metadata file and creates Ordered dict keyed by filename, with metadata for reference

"""

import boto3
import botocore

import random

import settings
import json
from glob import glob
from collections import defaultdict

import tweepy


import settings

session = boto3.Session(profile_name='default')
s3 = boto3.resource('s3')
s3_client = boto3.client('s3', 'us-east-1')

def get_s3_painting_metadata():

    """
    Open JSON metadata file in S3 and return an object to manipulate
    Convert link to point to S3 bucket
    :return: JSON array
    """

    local_json_file = settings.JSON_FILE  + settings.JSON_SUFFIX

    #pull json file info
    obj = s3.Object(settings.BASE_BUCKET, local_json_file)
    jsonload = json.loads(obj.get()['Body'].read().decode('utf-8'))

    return jsonload

def create_indexed_json(json_object):

    """
    Pass in JSON Array, create an indexed defaultdict with the filename as the key for use in Twitter bot metdata lookup
    :return: defaultdict
    """

    indexed_json = defaultdict()

    for value in json_object:
        artist = value['artistName']
        title = value['title']
        year = value['year']
        values = [artist, title, year]

        # return only image name at end of URL
        find_index = value['image'].rfind('/')
        img_suffix = value['image'][find_index + 1:]
        img_link =  "https://s3.amazonaws.com/soviet-art-bot/" + img_suffix

        try:
            indexed_json[img_link].append(values)
        except KeyError:
            indexed_json[img_link] = (values)

    return indexed_json


def access_twitter_api():
    access_token = settings.ACCESS_TOKEN
    access_token_secret = settings.ACCESS_SECRET
    consumer_key = settings.CONSUMER_KEY
    consumer_secret = settings.CONSUMER_SECRET

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api


def post_tweet(api, json_defaultdict):

    metadata = random.choice(list(json_defaultdict.items()))

    url =  metadata[0]
    painter = metadata[1][0]
    title = metadata[1][1]
    year = metadata[1][2]

    print(url, painter, title,year)

    api.update_with_media(url,
                          status="\"%s\"\n$s, %s") % (title, painter, year)
    print("Tweet posted")



metadata = get_s3_painting_metadata()
call_json = create_indexed_json(metadata)

api = access_twitter_api()
post_tweet(api, call_json)



