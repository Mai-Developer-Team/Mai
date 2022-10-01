import lightbulb

from config import setting
from utils import local

plugin = lightbulb.Plugin("ping", default_enabled_guilds=setting.guild_id)


@plugin.command()
@lightbulb.command("ping", "blyat cringe")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:

    await ctx.respond(
        local.localization(ctx.get_guild().id)["ping"]
    )


def load(client):
    client.add_plugin(plugin)

