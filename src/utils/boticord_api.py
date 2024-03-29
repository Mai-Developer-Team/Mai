import requests

from config import setting

url_api = "https://api.boticord.top/v2/{}"


def user(userID):
    s = f"profile/{userID}"
    res = requests.get(url_api.format(s))
    return res

def bot(botID):
    s = f"bot/{botID}"
    res = requests.get(url_api.format(s))
    return res

def server(serverID):
    s = f"server/{serverID}"
    res = requests.get(url_api.format(s))
    return res

def shortlink_get(code):
    data = {
        "code": code
    }
    headers = {
        "Authorization": f"Profile {setting.bckeyProfile}"
    }
    res = requests.get(url_api.format("links/get"), headers=headers, json=data).json()
    return res

def shortlink_add(url, code, domain):
    data = {
        "code": code,
        "link": url,
        "domain": domain
    }
    headers = {
        "Authorization": f"Profile {setting.bckeyProfile}"
    }
    res = requests.post(url_api.format("links/create"), headers=headers, json=data)
    return res