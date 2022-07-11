#DEV

import json 


def local_file(guild_id):
    if guild_id == 992117772521836674:
        lang = "ru-RU"

    with open(f"./src/config/localization/{lang}.json", "r", encoding='utf-8') as r:
        translate = json.load(r)
        return translate

def stats(guild_id, guilds, users, shards, shard_server_id):
    return local_file(guild_id)["stats"].format(guilds, users, shards, shard_server_id)
