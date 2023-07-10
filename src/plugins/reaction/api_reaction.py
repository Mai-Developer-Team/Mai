import requests

def nekos_best(reaction):
    img = requests.get(f"https://nekos.best/api/v2/{reaction}").json()
    return img["results"][0]["url"]

def img_api(reaction):
    image = nekos_best(reaction)
    return image
