import lightbulb
import hikari
import miru
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

    guild_count = len(ctx.bot.cache.get_guilds_view())
    member_count = len(ctx.bot.cache.get_users_view())
    all_shard = ctx.bot.shard_count
    shard_id = ctx.get_guild().shard_id

    emb = hikari.Embed(
            title = l["stats.title"],
            color=setting.color
        )
    emb.add_field(name= l["stats.guild_count"], value=guild_count)
    emb.add_field(name= l["stats.member_count"], value=member_count)
    emb.add_field(name= l["stats.all_shard"], value=all_shard)
    emb.add_field(name= l["stats.shard_id"], value=shard_id)
    emb.add_field(name= l["stats.uptime"], value=f"<t:{date.timestamp():.0f}:R>")
    emb.add_field(name= l["stats.version_library"], value=f'**hikari({hikari.__version__})** | **lightbulb({lightbulb.__version__})** | **hikari-miru({miru.__version__})**')
    emb.add_field(name= l["stats.version_bot"], value=setting.version)

    await ctx.respond(embed=emb)


def load(client):
    client.add_plugin(plugin)
