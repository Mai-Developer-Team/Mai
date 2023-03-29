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
    serverOwnerTag,
    upUserID,
    upChannelID,
    upChannelName
):
    data = {
        "serverID": serverID,
        "up": 1,
        "status": 1,
        "serverName": serverName,
        "serverAvatar": serverAvatar,
        "serverMembersAllCount": serverMemberAll,
        "serverMembersOnlineCount": serverMemberOnline,
        "serverOwnerID": serverOwnerID,
        "serverOwnerTag": serverOwnerTag,
        "upUserID": upUserID,
        "upChannelID": upChannelID,
        "upChannelName": upChannelName
    }

    headers = {
        "Authorization": f"Bot {setting.bc_key}",
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
    res = requests.get(url_api.format(f"profile/{userID}"))
    return res

def bot(botID):
    res = requests.get(url_api.format(f"bot/{botID}"))
    return res

def server(serverID):
    res = requests.get(url_api.format(f"server/{serverID}"))
    return res

#TODO: до конца сделать :klass:
#def shortlink()