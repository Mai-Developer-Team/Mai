import json
import random

from utils import db


def add_xp(id):
    if db.user(id) != None:
        xp = random.randint(1, 2)
        d = db.user(id)["xp"]
        db.db.user.update_one(
            {"id": id},
            {
                "$set":
                    {
                        "xp": d + xp
                    }
            }
        )

#TODO: не работает, но должно)
def display_lvl(id):
    if db.user(id) != None:
        with open(f"./src/config/lvl_sys.json", "r", encoding='utf-8') as r:
            l = json.load(r)

        d = db.user(id)["xp"]

        if d >= l:
            return l