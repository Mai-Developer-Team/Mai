#DEV

import json 

def local_guilds(guild_id):
    if guild_id == 992117772521836674:
        return "ru-RU"

def local_file(guild_id):
    with open(f"./src/config/localization/{local_guilds(guild_id)}.json", "r", encoding='utf-8') as r:
        translate = json.load(r)
        return translate

def stats(guild_id, guilds, users, shards, shard_server_id):
    return local_file(guild_id)["stats"].format(guilds, users, shards, shard_server_id)
