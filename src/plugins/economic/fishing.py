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
    l = local.localization(ctx.get_guild().id)
    u = db.user(ctx.author.id)
    level.add_xp(ctx.author.id)
    change = random.randint(1, 10)

    coins = db.db.user.find_one({"id": ctx.author.id})["coin"]

    if u["rod"] == None:
        await ctx.respond(
            l["fishing.none_rod"],
            flags=hikari.MessageFlag.EPHEMERAL
        )
        return

    if u["rod"] == 1:
        fishcoin = random.randint(225, 300)
    if u["rod"] == 2:
        fishcoin = random.randint(400, 653)
    if u["rod"] == 3:
        fishcoin = random.randint(700, 920)
    if u["rod"] == 4:
        fishcoin = random.randint(1000, 1220)
    if u["rod"] == 5:
        fishcoin = random.randint(1300, 1450)
    if u["rod"] == 6:
        fishcoin = random.randint(1500, 1700)
    if u["rod"] == 7:
        fishcoin = random.randint(2000, 2300)
    if u["rod"] == 8:
        fishcoin = random.randint(2350, 2600)
    if u["rod"] == 9:
        fishcoin = random.randint(3000, 4000)


    emb = hikari.Embed(
        title=l["fishing.title"],
        description=l["fishing.description"],
        color=setting.color
    )
    emb.add_field(
        name=l["fishing.field.rod_money"],
        value=f"{fishcoin} :coin:"
    )
    if u["fish_hook"] != None:
        if u["fish_hook"] == 1:
            if change == 6:
                fishhookcoin = 0
                emb.add_field(
                    name=l["fishing.name.fish_hook"],
                    value=l["fishing.fish_hook.err"]
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
                fishhookcoin = random.randint(25, 40)
                emb.add_field(
                    name=l["fishing.name.fish_hook"],
                    value=l["fishing.name.fish_hook"].format(fishhookcoin)
                )
        if u["fish_hook"] == 2:
            if change == 6:
                fishhookcoin = 0
                emb.add_field(
                    name=l["fishing.name.fish_hook"],
                    value=l["fishing.fish_hook.err"]
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
                fishhookcoin = random.randint(50, 75)
                emb.add_field(
                    name=l["fishing.name.fish_hook"],
                    value=l["fishing.name.fish_hook"].format(fishhookcoin)
                )
        if u["fish_hook"] == 3:
            if change == 6:
                fishhookcoin = 0
                emb.add_field(
                    name=l["fishing.name.fish_hook"],
                    value=l["fishing.fish_hook.err"]
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
                fishhookcoin = random.randint(80, 95)
                emb.add_field(
                    name=l["fishing.name.fish_hook"],
                    value=l["fishing.name.fish_hook"].format(fishhookcoin)
                )
        if u["fish_hook"] == 4:
            if change == 6:
                fishhookcoin = 0
                emb.add_field(
                    name=l["fishing.name.fish_hook"],
                    value=l["fishing.fish_hook.err"]
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
                fishhookcoin = random.randint(125, 200)
                emb.add_field(
                    name=l["fishing.name.fish_hook"],
                    value=l["fishing.name.fish_hook"].format(fishhookcoin)
                )
        if u["fish_hook"] == 5:
            if change == 6:
                fishhookcoin = 0
                emb.add_field(
                    name=l["fishing.name.fish_hook"],
                    value=l["fishing.fish_hook.err"]
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
                fishhookcoin = random.randint(300, 350)
                emb.add_field(
                    name=l["fishing.name.fish_hook"],
                    value=l["fishing.name.fish_hook"].format(fishhookcoin)
                )
        if u["fish_hook"] == 6:
            if change == 6:
                fishhookcoin = 0
                emb.add_field(
                    name=l["fishing.name.fish_hook"],
                    value=l["fishing.fish_hook.err"]
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
                fishhookcoin = random.randint(500, 600)
                emb.add_field(
                    name=l["fishing.name.fish_hook"],
                    value=l["fishing.name.fish_hook"].format(fishhookcoin)
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