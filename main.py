import requests
import json
import os
from functions import *

def main():

    url = os.environ["URL"]
    links = []
    
    while url != None:
        resultado = requests.get(url)
        json_format = resultado.json()
        photos_data = json_format['data']
        links.extend(get_images_links(photos_data))
        url = get_next_url(json_format)
    
    
    download_images(links)


if __name__=="__main__":
    main()