#DEV TEST
import lightbulb
import hikari

import random

from config import setting
from utils import local, access, level, db

plugin = lightbulb.Plugin("fishing", default_enabled_guilds=setting.guild_id)


@plugin.command()
@lightbulb.add_checks(access.disable_command)
@lightbulb.add_cooldown(86400, 1, lightbulb.UserBucket)
@lightbulb.command("fishing", "рыбалка наше все")
@lightbulb.implements(lightbulb.SlashCommand)
async def fishing(ctx: lightbulb.Context) -> None:
    u = db.user(ctx.author.id)
    level.add_xp(ctx.author.id)
    change = random.randint(1, 10)

    coins = db.db.user.find_one({"id": ctx.author.id})["coin"]

    if u["rod"] == None:
        await ctx.respond(
            "У вас нету удочки, чтобы порыбачить",
            flags=hikari.MessageFlag.EPHEMERAL
        )
        return

    if u["rod"] == 1:
        fishcoin = random.randint(125, 150)


    emb = hikari.Embed(
        title="Рыбалка",
        description="Теперь можете сходить только через день",
        color=setting.color
    )
    emb.add_field(
        name="Вы заработали",
        value=f"{fishcoin} :coin:"
    )
    if u["fish_hook"] != None:
        if u["fish_hook"] == 1:
            if change == 6:
                fishhookcoin = 0
                emb.add_field(
                    name="Крючек",
                    value="Ваш крючок потерялся в пучине озера"
                )
                db.db.user.update_one(
                    {"id": ctx.author.id},
                    {
                        "$set": {
                            "fish_hook": None
                        }
                    }
                )
            else:
                fishhookcoin = random.randint(12, 31)
                emb.add_field(
                    name="Крючек",
                    value=f"Благодаря крючку заработали дополнительно {fishhookcoin} :coin:"
                )

    db.db.user.update_one(
        {"id": ctx.author.id},
        {
            "$set": {
                "coin": coins + fishcoin + fishhookcoin
            }
        }
    )

    await ctx.respond(embed=emb)

def load(client):
    client.add_plugin(plugin)