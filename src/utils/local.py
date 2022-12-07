#DEV

import json

from utils import db


def localization(guild_id):
    l = db.server(guild_id)

    if not l:
        local = 'ru-RU'
    else:
        local = l["localization"]

    with open(f"./src/config/localization/{local}.json", "r", encoding='utf-8') as r:
        translate = json.load(r)
        return translate
