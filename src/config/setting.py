import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("TOKEN")
webhook_id = 891360914819932261
webhook_token = os.environ.get("WEBHOOK_TOKEN")
guild_id = [992117772521836674]
mongodb_client = os.environ.get("MONGO")

debug = False
version = "3.0.0.dev2"

if debug == False:
    info = "INFO"
    token = token
    status = "https://me.shuoki.top/mai"
else:
    info = "DEBUG"
    token = token #yes
    status = "котики чинят ботика >W<"
    
color = 0x2f3136


plugins = [
    "plugins.basic.custom_help",
    "plugins.basic.stats",
    "plugins.basic.username",
    "plugins.basic.serverinfo",
    "plugins.dev.ping",
    #"event.shard_tracker"
]

