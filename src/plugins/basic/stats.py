import lightbulb
import hikari
from datetime import datetime, timezone

from config import setting
from utils import local


plugin = lightbulb.Plugin("stats")
date = datetime.utcnow().replace(tzinfo=timezone.utc)

@plugin.command()
@lightbulb.command("stats", "Статистика Маи")
@lightbulb.implements(lightbulb.SlashCommand)
async def stats(ctx: lightbulb.Context) -> None:
    l = local.localization(ctx.get_guild().id)

    guild_count = await ctx.bot.rest.fetch_my_guilds().count()
    member_count = len(ctx.bot.cache.get_users_view())
    all_shard = ctx.bot.shard_count
    shard_id = ctx.get_guild().shard_id

    emb = (
        hikari.Embed(
            title = l["stats.title"],
            color=setting.color
        )
        .add_field(name= l["stats.guild_count"], value=guild_count)
        .add_field(name= l["stats.member_count"], value=member_count)
        .add_field(name= l["stats.all_shard"], value=all_shard)
        .add_field(name= l["stats.shard_id"], value=shard_id)
        .add_field(name= l["stats.uptime"], value=f"<t:{date.timestamp():.0f}:R>")
        .add_field(name= l["stats.version_library"], value=f'**hikari({hikari.__version__})** | **lightbulb({lightbulb.__version__})**')
        .add_field(name= l["stats.version_bot"], value=setting.version)
    )

    await ctx.respond(embed=emb)

def load(client):
    client.add_plugin(plugin)
