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
                    "profile": { 
                        "premium": {
                            "guild_add_premium": None
                        },
                        "badge": None,
                        "bio": None
                    },
                    "eco": {
                        "xp": 0,
                        "rod": None,
                        "fish_hook": None,
                        "banner": None,
                        "contract": None
                    },
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
                "setting": {}
            }
        )
    else:
        return db.server.find_one({"id": id})
