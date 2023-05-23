import lightbulb
import hikari

from config import setting
from utils import db

plugin = lightbulb.Plugin("promo", default_enabled_guilds=setting.guild_id)

#Пока еще не придумал


def load(client):
    client.add_plugin(plugin)
