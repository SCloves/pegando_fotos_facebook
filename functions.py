from PIL import Image
from io import BytesIO
import requests

def get_images_links(photos_data):
    img_list = []
    for i in photos_data:
        for img  in i["images"]:
            if img["source"] not in img_list:
                img_list.append(img["source"])
    
    return img_list

def get_next_url(json_format):

    try:
        paging = json_format["paging"]["next"]
        return paging

    except KeyError:
        return None


def download_images(links):
    n = 1
    for link in links:
        img = requests.get(link)
        img = Image.open(BytesIO(img.content))
        n = str(n)
        path = '/home/cloves/Documentos/web_scraping/facebook_api/code_facebook/photos/%s.jpg' %n
        img.save(path)
        n = int(n) + 1




