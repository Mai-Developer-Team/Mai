import lightbulb
import hikari

from config import setting
from utils import local, access, db, level

plugin = lightbulb.Plugin("profile", default_enabled_guilds=setting.guild_id)


@plugin.command()
@lightbulb.add_checks(access.disable_command)
@lightbulb.command("profile", "просмотреть экономический профиль")
@lightbulb.implements(lightbulb.SlashCommand)
async def profile(ctx: lightbulb.Context) -> None:
    d = db.user(ctx.author.id)
    a = level.display_lvl(ctx.author.id)

    emb = hikari.Embed(
        title = f"Профиль @{ctx.author}",
        color = setting.color
    )
    emb.add_field(name = "Баланс", value=f'{d["coin"]} :coin:', inline=True)
    emb.add_field(name = "Макойны", value=f'{d["macoin"]} :star:', inline=True)
    emb.add_field(name = "Уровень/XP", value=f'{a} ур/{d["xp"]}')
    emb.add_field(name = "Удочка", value=d["rod"] or "Отсутсвует", inline=True)
    emb.add_field(name = "Крючки", value=d["fish_hook"] or "Отсутсвуют", inline=True)
    emb.set_thumbnail(ctx.author.avatar_url)
    emb.set_image(d["banner"])

    await ctx.respond(embed=emb)

def load(client):
    client.add_plugin(plugin)