#DEV

import json 


def localization(guild_id):
    if guild_id == 992117772521836674:
        lang = "ru-RU"

    with open(f"./src/config/localization/{lang}.json", "r", encoding='utf-8') as r:
        translate = json.load(r)
        return translate
