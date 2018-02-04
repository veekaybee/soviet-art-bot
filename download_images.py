'''
Scrapes Socialist Realist Paintings from WikiArt

'''
#
import requests
import settings
import os
import json
import sys
import boto3



s3 = boto3.resource('s3')
s3_client = boto3.client('s3')


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

# #
# # def get_images():
# #     try:
# #         response = requests.get(
# #             settings.BASE_URL+settings.STYLE_URL,
# #             timeout=settings.METADATA_REQUEST_TIMEOUT)
# #         data = response.json()
# #     except requests.exceptions.RequestException as e:
# #         print(e)
# #         sys.exit(1
# #
# #     return data
# # #
# def upload_images_to_s3(files):
#
#     for f in files:
#         key = settings.IMAGE_FOLDER + f
#         client.put_object(Bucket=settings.BUCKET_NAME, Key=key, Body=f)
#
def upload_json_to_s3():

    json_files = list(settings.ASSET_PATH.rglob('*.json'))

    for f in json_files:
        full_file_path = str(f.parent) + "/" + str(f.name)
        file_name  = str(f.name)
        # object = s3.Object(settings.JSON_FOLDER, file_name)
        # object.put(Body=file_name)
        s3_client.upload_file(full_file_path, settings.JSON_FOLDER, file_name)

data = get_json()
files = save_json(data)
upload_json_to_s3()







