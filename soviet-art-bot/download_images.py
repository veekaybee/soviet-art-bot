"""
This code queries WikiArt and returns all paintings and metadata
in the Socialist Realism category  

"""

import json
import shutil
import sys

import boto3
import requests
import settings

s3 = boto3.resource('s3')
s3_client = boto3.client('s3', 'us-east-1')



def get_json():
    """
    Returns: 
        Dict of JSON metadata from WikiArt
    """
    data_list = []

    for page in range(1,10):
        url = settings.BASE_URL + settings.STYLE_URL + "&" + settings.PAGINATION_URL + str(page)
        print(url)
        try:
            response = requests.get(url, timeout=settings.METADATA_REQUEST_TIMEOUT)
            data = response.json()
            data = data['Paintings']
            data_list.extend(data)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

    return data_list



def save_json(data):
    """
    Converts list to JSON, writes to file
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
    Passes in list of image links
    Args:
        Data (dictionary)
    Returns:
        List of painting links
    """

    painting_links = []

    print(data)

    for painting in data:
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
                                    timeout=settings.METADATA_REQUEST_TIMEOUT, stream=True)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

        find_index = link.rfind('/')
        image_name  = link[find_index+1:]


        with open(str(settings.ASSET_PATH) + image_name, 'wb') as outfile:
            shutil.copyfileobj(response.raw, outfile)
        del response

def upload_images_to_s3(directory):

    for f in directory.iterdir():
        if str(f).endswith(('.png', '.jpg')):
            full_file_path = str(f.parent) + "/" + str(f.name)
            file_name = str(f.name)
            s3_client.upload_file(full_file_path, settings.BASE_BUCKET, file_name)
            print(f,"put")


def upload_json_to_s3(directory):

    for f in directory.iterdir():
        if str(f).endswith('.json'):
            full_file_path = str(f.parent) + "/" + str(f.name)
            file_name  = str(f.name)
            s3_client.upload_file(full_file_path, settings.JSON_FOLDER, file_name)

data = get_json()
files = save_json(data)
links = get_image_links(data)
download_images(links)
upload_json_to_s3()
upload_images_to_s3(settings.BASE_FOLDER)
upload_json_to_s3(settings.BASE_FOLDER)







