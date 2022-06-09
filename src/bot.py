import hikari 
import lightbulb

import logging

from config import setting

if setting.debug == False:
    info = "INFO"
    prefix = setting.prefix 
    token = setting.token
else:
    info = "DEBUG"
    prefix = setting.devprefix
    token = setting.token #yes


client = lightbulb.BotApp(
    token = token,
    prefix = prefix,
    intents = hikari.Intents.ALL_MESSAGES | hikari.Intents.GUILDS | hikari.Intents.MESSAGE_CONTENT,
    logs = {
        "version": 1,
        "incremental": True,
        "loggers": {
            "hikari": {"level": info},
            "hikari.ratelimits": {"level": "TRACE_HIKARI"},
            "lightbulb": {"level": "DEBUG"}
            },
        }
)

#client.load_extensions_from("./plugins")
#TODO: fix load plugins :D
client.run(
    activity = hikari.Activity(
        name = f"hikari {hikari.__version__} | Mai {setting.version}",
        type = hikari.ActivityType.WATCHING
        )
)

