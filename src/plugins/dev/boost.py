import lightbulb
import hikari

from config import setting
from utils import db

import datetime


plugin = lightbulb.Plugin("boost", default_enabled_guilds=setting.guild_id)

@plugin.command()
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.command("Выдача примиум", "Выдать премиум пользователю")
@lightbulb.implements(lightbulb.UserCommand)
async def boost(ctx: lightbulb.Context) -> None:
    user = ctx.options.target
    premium = db.premium(user.id)
    
    if premium is None:
        db.db.premium.insert_one(
            {
                "expireAt": datetime.datetime.now() + datetime.timedelta(hours = -3, days = 30), 
                "originalDate": datetime.datetime.now() + datetime.timedelta(days = 30),
                "id": user.id
            }
        )
        await ctx.respond(f"Было выдано 30 дней подписки пользователю {user}", flags=hikari.MessageFlag.EPHEMERAL)
    else:
        await ctx.respond(f"Я не могу выдать подписку {user}, т.к у него уже есть", flags=hikari.MessageFlag.EPHEMERAL)

def load(client):
    client.add_plugin(plugin)