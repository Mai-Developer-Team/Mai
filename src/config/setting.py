import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("TOKEN")
webhook_id = 891360914819932261
webhook_token = os.environ.get("WEBHOOK_TOKEN")

debug = False
version = "3.0.0.dev2"

if debug == False:
    info = "INFO"
    prefix = "m"
    token = token
    status = "https://me.shuoki.top/mai"
else:
    info = "DEBUG"
    prefix = "m#"
    token = token #yes
    status = "котики чинят ботика >W<"
    
color = 0x2f3136


plugins = [
    "plugins.info.custom_help",
    "plugins.dev.ping",
    "plugins.info.stats"
    #"event.shard_tracker"
]

