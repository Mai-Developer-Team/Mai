import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("TOKEN")
webhook_id_shard = 1040292382844932147
webhook_id_status = 1040292752673493114
webhook_token_shard = os.environ.get("WEBHOOK_TOKEN_SHARD")
webhook_token_status = os.environ.get("WEBHOOK_TOKEN_STATUS")
guild_id = [992117772521836674, 807900317823402004, 833880841976938576]
mongodb_client = os.environ.get("MONGO")

debug = False
version = "3.0.0.dev3"

if debug == False:
    info = "INFO"
    token = token
    status = "https://me.shuoki.top/mai"
else:
    info = "DEBUG"
    token = token #yes
    status = "котики чинят ботика >W<"
    
color = 0x2b2d31


plugins = [
    "plugins.basic.custom_help",
    "plugins.basic.stats",
    "plugins.basic.userinfo",
    "plugins.basic.serverinfo",
    "plugins.dev.ping",
    "plugins.dev.eval",
    "plugins.dev.boost",
    #"plugins.dev.play",
    "plugins.setting.guild_setting",
    "plugins.setting.user_setting",
    "event.error"
    #"event.player_tracker"
    #"event.shard_tracker"
    #"event.status_tracker"
]

