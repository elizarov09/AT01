# cat_api.py
import requests

def get_random_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data:
            return data[0]['url']
    except requests.RequestException:
        return None
