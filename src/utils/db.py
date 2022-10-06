from pymongo import MongoClient
import hikari

from config import setting

cluster = MongoClient(setting.mongodb_client) 
db = cluster.maiv3

def user(id):
    if not db.user.find_one({"id": id}):
        db.user.insert_one(
            {
                    "id": id,
                    "profile": { 
                        "premium": 0,
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
