import hikari 
import lightbulb
import miru

import logging
import os
import sys
import traceback

from config import setting


client = lightbulb.BotApp(
    token = setting.token,
    intents = hikari.Intents.ALL_MESSAGES 
    | hikari.Intents.GUILDS 
    | hikari.Intents.GUILD_MEMBERS 
    | hikari.Intents.GUILD_VOICE_STATES,
    logs = {
        "version": 1,
        "incremental": True,
        "loggers": {
            "hikari": {"level": setting.info},
            "hikari.ratelimits": {"level": "TRACE_HIKARI"},
            "lightbulb": {"level": setting.info}
            },
        }
)
miru.install(client)

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
        name = setting.status,
        type = hikari.ActivityType.CUSTOM)
    )
