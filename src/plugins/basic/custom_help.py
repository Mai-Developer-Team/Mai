import lightbulb
import hikari

from config import setting
from utils import local

plugin = lightbulb.Plugin("custom_help")


@plugin.command()
@lightbulb.command("help", "Узнать все доступные команды в боте")
@lightbulb.implements(lightbulb.SlashCommand)
async def help(ctx: lightbulb.Context) -> None:
    
    l = local.localization(ctx.get_guild().id)

    embed = (
        hikari.Embed(color = setting.color)
        .add_field(
            name=l["help.command_category.basic"], 
            value="</stats:1059129259806969869>, </userinfo:1059129259806969870>, </serverinfo:1059129259806969871>, </report:1027629303875244057>"
        )
        .add_field(
            name=l["help.command_category.economic"],
            value="</fishing:1134066288868732989>, </profile:1134066285630722068>, </shop:1027629304307265616>, </work:1027629303875244059>"
        )
        .add_field(
            name=l["help.command_category.reaction"],
            value="</reaction:1134066292488405092>"
        )
        .add_field(
            name=l["help.command_category.setting"],
            value="</user_setting:1134066295751573515>"
        )
        .set_thumbnail(ctx.bot.application.icon_url)
    )

    await ctx.respond(embed = embed)

def load(client):
    client.add_plugin(plugin)
