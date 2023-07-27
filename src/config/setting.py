import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("TOKEN")
dev_token = os.environ.get("DEVTOKEN")
webhook_id_shard = 1040292382844932147
webhook_id_status = 1040292752673493114
webhook_token_shard = os.environ.get("WEBHOOK_TOKEN_SHARD")
webhook_token_status = os.environ.get("WEBHOOK_TOKEN_STATUS")
guild_id = [992117772521836674, 807900317823402004]
mongodb_client = os.environ.get("MONGO")
bc_api = os.environ.get("BC_API")
id_shop = os.environ.get("ID_SHOP")
secret_key = os.environ.get("SECRET_KEY")

debug = False
version = "3.0.1"

if debug == False:
    info = "INFO"
    token = token
    status = "https://docs.maibot.xyz"
else:
    info = "DEBUG"
    token = dev_token #yes
    status = "DEBUG"
    
color = 0x2b2d31


plugins = [
    "plugins.basic.custom_help",
    "plugins.basic.stats",
    "plugins.basic.userinfo",
    "plugins.basic.serverinfo",
    "plugins.basic.report",
    #"plugins.dev.pay_boost",
    "plugins.economic.work",
    "plugins.economic.profile",
    "plugins.economic.fishing",
    "plugins.economic.shop",
    "plugins.reaction.reaction",
    #"plugins.integration.bcinfo",
    "plugins.dev.ping",
    "plugins.dev.eval",
    "plugins.dev.boost",
    "plugins.dev.promo",
    #"plugins.dev.play",
    "plugins.setting.guild_setting",
    "plugins.setting.user_setting",
    "event.error",
    "event.bc_notify",
    "event.shard_tracker",
    "event.status_tracker"
]

