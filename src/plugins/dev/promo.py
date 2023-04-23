import lightbulb
import hikari

from config import setting
from utils import db

plugin = lightbulb.Plugin("promo", default_enabled_guilds=setting.guild_id)

#Все это пока концепт
@plugin.command()
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.option(
    "name",
    "название промокода",
    type = hikari.OptionType.STRING,
    required=True
)
@lightbulb.option(
    "limit",
    "установка лимита на использования промокода",
    type = hikari.OptionType.FLOAT,
    required=True
)
@lightbulb.option(
    "forwhat",
    "для чего нужно создать",
    type = hikari.OptionType.STRING,
    required=True
)
@lightbulb.command("promo", "создание специальных кодов с разными плюшками")
@lightbulb.implements(lightbulb.SlashCommand)
async def promo(ctx: lightbulb.Context) -> None:
    name = ctx.options.name
    limit = ctx.options.limit
    forWhat = ctx.options.forwhat
    
    if db.promo(name) != None:
        await ctx.respond(f"Данный промокод уже существует, вся информация про промокод: **{db.promo(name)}**", flags=hikari.MessageFlag.EPHEMERAL)
    else:
        db.db.promocode.insert_one(
            {
                "name": name,
                "usageLimit": limit,
                "forWhat": forWhat,
                "used": 0
            }
        )
        await ctx.respond(f"Промокод **{name}** был создан", flags=hikari.MessageFlag.EPHEMERAL)


def load(client):
    client.add_plugin(plugin)
