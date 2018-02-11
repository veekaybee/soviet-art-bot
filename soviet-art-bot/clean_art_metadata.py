"""
Opens S3 bucket with

Pulls in JSON metadata file and creates Ordered dict keyed by filename, with metadata for reference

"""

import boto3
import settings
import json
from glob import glob
from collections import defaultdict


s3 = boto3.resource('s3')
s3_client = boto3.client('s3', 'us-east-1')



def create_indexed_json(json_file):

    indexed_json = defaultdict()

    with open(str(json_file), 'r') as json_stream:
        for line in json_stream:
            line = json.loads(line)
            for value in line:
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

    for k,v in indexed_json.items():
        print(k,v)


def get_s3_painting_metadata():

    metadata_location = settings.JSON_FILE + settings.JSON_SUFFIX

    for key in s3_client.list_objects(Bucket=settings.BASE_BUCKET)['Contents']:
            print(key['Key'])


def get_s3_painting_name():
    pass


get_s3_painting_metadata()
