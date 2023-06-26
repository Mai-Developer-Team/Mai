#DEV TEST
import lightbulb
import hikari

import random

from config import setting
from utils import local, access, level, db

plugin = lightbulb.Plugin("fishing", default_enabled_guilds=setting.guild_id)


@plugin.command()
@lightbulb.add_checks(access.disable_command)
@lightbulb.command("fishing", "рыбалка наше все")
@lightbulb.implements(lightbulb.SlashCommand)
async def fishing(ctx: lightbulb.Context) -> None:
    u = db.user(ctx.author.id)

    if u["rod"] == None:
        await ctx.respond(
            "У вас нету удочки, чтобы порыбачить",
            flags=hikari.MessageFlag.EPHEMERAL
        )
        return

    if u["rod"] == 0:
        coin = random.randint(1, 3)

    if u["fish_hook"] == None:
        hook = 0
        a = "d"

    if u["fish_hook"] == 0:
        change = random.randint(1, 9)

        if change == 5:
            hook = 0
            a = "Ваш крючок потерялся в пучине озера"
        else:
            hook = random.randint(0, 1)
            a = "Благодаря крючку da заработали дополнительно деньги"


    await ctx.respond(
            f"Это тестовое сообщение для откладки\n Заработано {coin + hook} :coin:\n{a}"
        )

def load(client):
    client.add_plugin(plugin)