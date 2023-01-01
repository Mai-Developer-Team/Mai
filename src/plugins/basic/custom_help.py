import lightbulb
import hikari

from config import setting
from utils import local

plugin = lightbulb.Plugin("custom_help", default_enabled_guilds=setting.guild_id)


@plugin.command()
@lightbulb.command("help", "Узнать все доступные команды в боте")
@lightbulb.implements(lightbulb.SlashCommand)
async def help(ctx: lightbulb.Context) -> None:
    
    l = local.localization(ctx.get_guild().id)

    embed = (
        hikari.Embed(color = setting.color)
        .add_field(
            name=l["help.command_categoty.basic"], 
            value="</ping:1025071954027347989>, </stats:1025811202946912368>, </userinfo:1026850965854363689>"
        )
        .add_field(
            name=l["help.command_categoty.setting"],
            value="</guild_setting:1055495743714107402>"
        )
        .set_thumbnail(ctx.bot.application.icon_url)
    )

    await ctx.respond(embed = embed)

def load(client):
    client.add_plugin(plugin)
