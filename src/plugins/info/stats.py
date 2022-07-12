import lightbulb
from utils import local

plugin = lightbulb.Plugin("stats")


@plugin.command()
@lightbulb.command("stats", description = "Циферки красивые")
@lightbulb.implements(lightbulb.PrefixCommand)
async def stats(ctx: lightbulb.Context) -> None:
    
    await ctx.respond(
        local.stats(
            ctx.get_guild().id,
            len(ctx.bot.cache.get_available_guilds_view()), 
            len(ctx.bot.cache.get_members_view()),
            ctx.bot.shard_count - 1,
            ctx.get_guild().shard_id
            )
    )

def load(client):
    client.add_plugin(plugin)
