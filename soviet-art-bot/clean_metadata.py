"""
Opens S3 bucket with

Pulls in JSON metadata file and creates Ordered dict keyed by filename, with metadata for reference

"""

import boto3
import botocore

import settings
import json
from glob import glob
from collections import defaultdict

session = boto3.Session(profile_name='default')
s3 = boto3.resource('s3')
s3_client = boto3.client('s3', 'us-east-1')





def get_s3_painting_metadata():

    """
    Open JSON metadata file in S3 and return an object to manipulate
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

    # with open(str(json_object), 'r') as json_stream:
    # for line in json_stream:
    #     line = json.loads(line)
    for value in json_object:
        artist = value['artistName']
        title = value['title']
        year = value['year']
        values = [artist, title, year]

        # return only image name at end of URL
        find_index = value['image'].rfind('/')
        img_link = value['image'][find_index + 1:]

        try:
            indexed_json[img_link].append(values)
        except KeyError:
            indexed_json[img_link] = (values)

    return indexed_json

def get_s3_painting_name():
    pass


metadata = get_s3_painting_metadata()
print(create_indexed_json(metadata))
