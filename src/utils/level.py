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


def display_lvl(id):
    if db.user(id) != None:
        d = db.user(id)["xp"]

        #Я знаю, что это говно, но это мое
        if d >= 0:
            current_level = 0
        if d >= 100:
            current_level = 1
        if d >= 200:
            current_level = 2
        if d >= 300:
            current_level = 3

        return current_level