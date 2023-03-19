import requests
from pynepcord.base import ImageSession
import random

from config import setting


def nekos_best(reaction):
    img = requests.get(f"https://nekos.best/api/v2/{reaction}").json()
    return img["results"][0]["url"]

def pynepcord(reaction):
    session = ImageSession(setting.pynepcord_token)
    image = session.get_image(reaction)
    return image.url

def img_api(reaction):
    image = random.choice([nekos_best(reaction), pynepcord(reaction)])
    return image
