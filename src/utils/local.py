#DEV

import json 


def local_file(guild_id):
    if guild_id == 992117772521836674:
        lang = "ru-RU"

    with open(f"./src/config/localization/{lang}.json", "r", encoding='utf-8') as r:
        translate = json.load(r)
        return translate

def help_category_info(guild_id):
    return local_file(guild_id)["help_category_info"]

def help_name_command(guild_id):
    return local_file(guild_id)["help_name_command"]

def help_description_command(guild_id):
    return local_file(guild_id)["help_description_command"]

def stats(guild_id, guilds, users, shards, shard_server_id):
    return local_file(guild_id)["stats"].format(guilds, users, shards, shard_server_id)

def help_err(guild_id, command):
    return local_file(guild_id)["help_err"].format(command)