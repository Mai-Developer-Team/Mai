import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("TOKEN")
webhook_id_shard = 1040292382844932147
webhook_id_status = 1040292752673493114
webhook_token_shard = os.environ.get("WEBHOOK_TOKEN_SHARD")
webhook_token_status = os.environ.get("WEBHOOK_TOKEN_STATUS")
guild_id = [992117772521836674, 807900317823402004]
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
    "plugins.basic.userinfo",
    "plugins.basic.serverinfo",
    "plugins.dev.ping",
    "plugins.dev.eval",
    "plugins.setting.guild_setting",
    "event.error"
    #"event.shard_tracker",
    #"event.status_tracker"
]

