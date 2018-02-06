"""
This code queries WikiArt and returns all paintings and metadata
in the Socialist Realism category  

"""

import requests
import settings
import os
import json
import sys
import boto3
import shutil
import re



s3 = boto3.resource('s3')
s3_client = boto3.client('s3')


def get_json():
    """
    Returns: 
        Dict of JSON metadata from WikiArt
    """
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
    """
    Converts dictionary to JSON, writes to file
    Args: 
        Data (dictionary)
    
    Returns: 
        None  
    """
    data = json.dumps(data)

    with open('%s/art_metadata.json' % settings.ASSET_PATH, 'w') as outfile:
        outfile.write(data)

def get_image_links(data):
    """
    Passes in dictionary of image links
    Args: 
        Data (dictionary)
    Returns: 
        List of painting links
    """
    painting_links = []
    
    for painting in data['Paintings']:
        painting_link = (painting['image'])
        painting_links.append(painting_link)

    return painting_links


def download_images(links):
    """
    Passes in a list of links
    Args:
        links(list)
    Returns:
        Images of paintings to download
    """

    for link in links:
        print(link)
        try:
            response = requests.get(link,
                timeout=settings.METADATA_REQUEST_TIMEOUT,stream=True)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)


        regex_search = re.search('[a-z-0-9]+.jpg', link, re.IGNORECASE)
        print(regex_search)
        regex = regex_search.group(0)
        print(regex)

        with open(str(settings.ASSET_PATH) + regex, 'wb') as outfile:
            shutil.copyfileobj(response.raw, outfile)
        del response
#
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
        s3_client.upload_file(full_file_path, settings.JSON_FOLDER, file_name)

data = get_json()
files = save_json(data)
links = get_image_links(data)
download_images(links)
# upload_json_to_s3()







