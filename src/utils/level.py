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
        if d >= 50:
            current_level = 0
        if d >= 100:
            current_level = 1
        if d >= 200:
            current_level = 2
        if d >= 300:
            current_level = 3
        if d >= 400:
            current_level = 4
        if d >= 500:
            current_level = 5
        if d >= 1000:
            current_level = 6
        if d >= 2000:
            current_level = 7
        if d >= 3000:
            current_level = 8
        if d >= 4000:
            current_level = 9
        if d >= 5000:
            current_level = 10
        if d >= 10000:
            current_level = 11
        if d >= 11000:
            current_level = 12
        if d >= 12000:
            current_level = 13
        if d >= 13000:
            current_level = 14
        if d >= 14000:
            current_level = 15
        if d >= 15000:
            current_level = 16
        if d >= 20000:
            current_level = 17
        if d >= 25000:
            current_level = 18
        if d >= 30000:
            current_level = 19
        if d >= 40000:
            current_level = 20

        return current_level