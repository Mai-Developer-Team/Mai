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
    l = local.localization(ctx.get_guild().id)
    d = db.user(ctx.author.id)
    a = level.display_lvl(ctx.author.id)

    emb = hikari.Embed(
        title = l["profile.title"].format(ctx.author),
        color = setting.color
    )
    emb.add_field(name = l["profile.balance.coin"], value=f'{d["coin"]} :coin:', inline=True)
    emb.add_field(name = l["profile.balance.macoin"], value=f'{d["macoin"]} :star:', inline=True)
    emb.add_field(name = l["profile.lvl"], value=l["profile.lvl.display"].format(a, d["xp"]))
    emb.add_field(name = l["profile.rod"], value=l[f"fishing.rod.id.{d['rod']}"], inline=True)
    emb.add_field(name = l["profile.fishhook"], value=l[f"fishing.fish_hook.id.{d['fish_hook']}"], inline=True)
    emb.set_thumbnail(ctx.author.avatar_url)
    emb.set_image(d["banner"])

    await ctx.respond(embed=emb)

def load(client):
    client.add_plugin(plugin)