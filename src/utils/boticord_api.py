import requests

from config import setting

url_api = "https://api.boticord.top/v2/{}"


def up(
    serverID,
    serverName,
    serverAvatar,
    serverMemberAll,
    serverMemberOnline,
    serverOwnerID,
    serverOwnerName,
    serverOwnerTag,
    upUserID,
    upChannelID,
    upChannelName
):
    data = {
        "serverID": str(serverID),
        "up": 1,
        "status": 1,
        "serverName": serverName,
        "serverAvatar": serverAvatar,
        "serverMembersAllCount": serverMemberAll,
        "serverMembersOnlineCount": serverMemberOnline,
        "serverOwnerID": str(serverOwnerID),
        "serverOwnerTag": serverOwnerName + "#" + serverOwnerTag,
        "upUserID": upUserID,
        "upChannelID": upChannelID,
        "upChannelName": upChannelName
    }

    headers = {
        "Authorization": f"Bot {setting.bcKeyBot}",
        "Content-Type": "application/json"
    }

    res = requests.post(url_api.format("server"), headers = headers, json = data)

    if res.json()["updated"]:
        d = res.json()["message"]
        return d
    else:
        d = res.json()["message"]
        return d

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