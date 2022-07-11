import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("TOKEN")
webhook_id = 891360914819932261
webhook_token = os.environ.get("WEBHOOK_TOKEN")

debug = False
version = "3.0.0.dev2"
prefix = "m"
devprefix = "m#"
color = 0x2f3136

status = "https://me.shuoki.top/mai"
debug_status = "котики чинят ботика >W<"


plugins = [
    "plugins.dev.ping",
    "plugins.info.stats"
    #"event.shard_tracker"
]

