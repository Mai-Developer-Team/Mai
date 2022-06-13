import hikari 
import lightbulb

import logging
import os
import sys
import traceback

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
            "lightbulb": {"level": info}
            },
        }
)

if __name__ == '__main__':
    for plugin in setting.plugins:
        try:
            client.load_extensions(plugin)
        except Exception as err:
            print(f"[LOG PLUGINS] Error starting {plugin}", file = sys.stderr)
            traceback.print_exc()
            print("==============")
        else:
            pass


client.run(
    activity = hikari.Activity(
        name = f"hikari {hikari.__version__} | Mai {setting.version}",
        type = hikari.ActivityType.WATCHING
        )
)

