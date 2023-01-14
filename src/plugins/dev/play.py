import lightbulb
import hikari

from event.player_tracker import lavalink
from config import setting
from utils import access

plugin = lightbulb.Plugin("play", default_enabled_guilds=setting.guild_id)

@plugin.command()
@lightbulb.option(name="query", description="запрос на музыку", required=True)
@lightbulb.command("play", "(DEV)прослушивание музыки")
@lightbulb.implements(lightbulb.SlashCommand)
async def play(ctx: lightbulb.Context) -> None:
    query = ctx.options.query
    voice = ctx.bot.cache.get_voice_state(ctx.get_guild().id, ctx.author.id)

    await ctx.bot.update_voice_state(ctx.get_guild().id, voice.channel_id, self_deaf=True)
    await lavalink.wait_for_connection(ctx.get_guild().id)

    result = await lavalink.auto_search_tracks(query)
    await lavalink.play(ctx.get_guild().id, result[0], ctx.member.id)

    await ctx.respond(f'Сейчас играет **{result[0].title}**')


def load(client):
    client.add_plugin(plugin)