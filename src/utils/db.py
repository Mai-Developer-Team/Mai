from pymongo import MongoClient
import hikari

from config import setting

import dns.resolver

dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
cluster = MongoClient(setting.mongodb_client) 
db = cluster.maiv3


def user(id):
    if not db.user.find_one({"id": id}):
        db.user.insert_one(
            {
                "id": id,
                "premium": {
                    "guild_add_premium": None
                },
                "nothing": False,
                "badge": None,
                "bio": None,
                "xp": 0,
                "coin": 0,
                "macoin": 0,
                "rod": None,
                "fish_hook": None,
                "banner": None,
                "genshin_token": None,
                "blacklist": {
                    "block": 0,
                    "reason": None
                }
            }
        )
    else:
        return db.user.find_one({"id": id})

def premium(id):
    return db.premium.find_one({"id": id})

def server(id):
    if not db.server.find_one({"id": id}):
        db.server.insert_one(
            {
                "id": id,
                "localization": "ru-RU",
                "premium": 0,
                "disableCommand": False,
                "kickBlacklist": False,
                "WelcomeSetting": False,
                "WelcomeText": None,
                "GoodByeSetting": False,
                "GoodByeText": None,
                "logsSetting": False,
                "logsConnectMember": False,
                "logsLeaveMember": False,
                "logsAuditLog": False,
                "logsVoiceChannel": False,
                "logsWebhookURL": None,
                "blockSettings": False
            }
        )
    else:
        return db.server.find_one({"id": id})
