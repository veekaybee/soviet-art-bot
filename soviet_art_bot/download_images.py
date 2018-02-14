"""
This code queries WikiArt and returns all paintings and metadata
in the Socialist Realism category
"""

import json
import shutil
import sys
from glob import glob
import boto3
import requests

import PIL
from PIL import Image

import soviet_art_bot.settings as settings

# intialize connection to S3 resources
s3 = boto3.resource('s3')
s3_client = boto3.client('s3', 'us-east-1')


def get_json():
    """
    Get JSON with art name and location from WikiArt site
    :return: dictionary of filenames from WikiArt
    """
    data_list = []

    for page in range(1,10):
        url = settings.BASE_URL + settings.STYLE_URL + "&" + settings.PAGINATION_URL + str(page)
        print(page, "pages processed")
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
    :param data: Data (list)
    :return:
    """
    data = json.dumps(data)

    with open('%s/art_metadata.json' % settings.ASSET_PATH, 'w') as outfile:
        outfile.write(data)

def get_image_links(data):
    """
    Passes in a list of image links
    :param data: Data (list)
    :return: List of painting links
    """

    painting_links = []

    print(data)

    for painting in data:
        painting_link = (painting['image'])
        painting_links.append(painting_link)

    return painting_links



def download_images(links):
    """
    Passes in a list of links to download
    :param links (list):
    :return Images downloaded into the assets folder:
    """

    for link in links:
        print(link) #print link to be processed
        try:
            response = requests.get(link,
                                    timeout=settings.METADATA_REQUEST_TIMEOUT, stream=True)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

        image_name  = link.rsplit('/', 1)[1]
        print(image_name)

        file_location = settings.ASSET_PATH.joinpath(image_name)

        with open(str(file_location), 'wb') as outfile:
                shutil.copyfileobj(response.raw, outfile)



def upload_images_to_s3(directory):
    """
    Upload images to S3 bucket if they end with png or jpg
    :param directory:
    :return: null
    """

    for f in directory.iterdir():
        if str(f).endswith(('.png', '.jpg', '.jpeg')):
            full_file_path = str(f.parent) + "/" + str(f.name)
            file_name = str(f.name)
            s3_client.upload_file(full_file_path, settings.BASE_BUCKET, file_name)
            print(f,"put")



def upload_json_to_s3(directory):
    """
    Upload metadata json to directory
    :param directory:
    :return: null
    """

    for f in directory.iterdir():
        if str(f).endswith('.json'):
            full_file_path = str(f.parent) + "/" + str(f.name)
            file_name  = str(f.name)
            s3_client.upload_file(full_file_path, settings.BASE_BUCKET, file_name)

#TODO: CLEAN UP RESIZING UTILITY

def resize_images():
    pass
        # if os.path.getsize(filename) > (max_size * 1024):
        #     basewidth = 300
        #     img = Image.open('fullsized_image.jpg')
        #     wpercent = (basewidth / float(img.size[0]))
        #      hsize = int((float(img.size[1]) * float(wpercent)))
        #     img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        #      img.save('resized_image.jpg')


data = get_json()
files = save_json(data)
links = get_image_links(data)
download_images(links)
# upload_images_to_s3(settings.ASSET_PATH)
# upload_json_to_s3(settings.ASSET_PATH)







