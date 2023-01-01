import hikari
import lightbulb

from config import setting
from utils import access

plugin = lightbulb.Plugin("error", default_enabled_guilds=setting.guild_id)


@plugin.listener(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:

    if isinstance(event.exception, lightbulb.CommandInvocationError):
        await event.context.respond('Произошла критическая ошибка в команде! Если ничего не измениться, то обратитесь на сервер поддержки', flags=hikari.MessageFlag.EPHEMERAL)
    if isinstance(event.exception, lightbulb.NotOwner):
        await event.context.respond("https://http.cat/400", flags=hikari.MessageFlag.EPHEMERAL)
    if isinstance(event.exception, lightbulb.CheckFailure):
        await event.context.respond(f"Возможные причины ошибки:\n`[1]`У вас закончился буст на сервере\n`[2]`Вы не является альфа-тестером", flags=hikari.MessageFlag.EPHEMERAL)
    
    #логи
    if isinstance(event.exception, (lightbulb.CommandInvocationError)):
        thread = await event.bot.rest.create_thread(1053706633487859722, 11, f"Ошибка в команде {event.context.command.name}")
        await thread.send(
            f"<@&807901614450671637>\nИспользовал её **{event.context.member}** в гильдии `{event.context.get_guild().name}`|`{event.context.get_guild().id}`\nОшибка ```python\n{type(event.exception.__cause__).__name__}: {event.exception.__cause__}```",
            role_mentions = True
        )

def load(client):
    client.add_plugin(plugin)
