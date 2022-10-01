import lightbulb

from config import setting
from utils import local


plugin = lightbulb.Plugin("stats", default_enabled_guilds=setting.guild_id)


@plugin.command()
@lightbulb.command("stats", "Циферки красивые")
@lightbulb.implements(lightbulb.SlashCommand)
async def stats(ctx: lightbulb.Context) -> None:
    
    await ctx.respond("Тут статистика, но нету еще дизайна")

def load(client):
    client.add_plugin(plugin)
