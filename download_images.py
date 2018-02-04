'''
Scrapes Socialist Realist Paintings from WikiArt

'''

import requests
import settings
import os
import json
import sys
import boto3
from pathlib import Path

s3 = boto3.resource('s3')


def get_json():
    try:
        response = requests.get(
            settings.BASE_URL+settings.STYLE_URL,
            timeout=settings.METADATA_REQUEST_TIMEOUT)
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)

    return data

def save_json(data):
    data = json.dumps(data)
    with open('%s/art_metadata.json' % settings.ASSET_PATH, 'w') as outfile:
        outfile.write(data)

#
# def get_images():
#     try:
#         response = requests.get(
#             settings.BASE_URL+settings.STYLE_URL,
#             timeout=settings.METADATA_REQUEST_TIMEOUT)
#         data = response.json()
#     except requests.exceptions.RequestException as e:
#         print(e)
#         sys.exit(1
#
#     return data
# #
def upload_images_to_s3(files):

    for f in files:
        key = settings.IMAGE_FOLDER + f
        client.put_object(Bucket=settings.BUCKET_NAME, Key=key, Body=f)

def upload_json_to_s3(files):

    for f in files:
        key = settings.IMAGE_FOLDER + f
        print(key)
        s3.put_object(Bucket=settings.BUCKET_NAME, Key=key, Body=f)
#
# # get_images_and_json()

data = get_json()
files = save_json(data)
upload_json_to_s3([files])






