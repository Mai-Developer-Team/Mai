import lightbulb
import hikari

from config import setting
from utils import local


plugin = lightbulb.Plugin("serverinfo", default_enabled_guilds=setting.guild_id)


@plugin.command()
@lightbulb.command("serverinfo", "Информация о данном сервере")
@lightbulb.implements(lightbulb.SlashCommand)
async def serverinfo(ctx: lightbulb.Context) -> None:
    
    await ctx.respond("Тут статистика, но нету еще дизайна")

def load(client):
    client.add_plugin(plugin)
