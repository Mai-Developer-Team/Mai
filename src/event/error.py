import hikari
import lightbulb

import datetime, time

from config import setting
from utils import local

plugin = lightbulb.Plugin("error", default_enabled_guilds=setting.guild_id)


@plugin.listener(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:

    l = local.localization(event.context.get_guild().id)

    if isinstance(event.exception, lightbulb.CommandInvocationError):
        await event.context.respond(
            l["error.CommandInvocationError"],
            flags=hikari.MessageFlag.EPHEMERAL
            )
        if event.context.command.cooldown_manager != None:
            await event.context.command.cooldown_manager.reset_cooldown(event.context)

        thread = await event.bot.rest.create_thread(
            1053706633487859722,
            11,
            f"Ошибка в команде {event.context.command.name}",
            reason="Отчет по ошибке"
        )
        await thread.send(
            f"<@&890683001065848842>\nИспользовал её **{event.context.member}** в гильдии `{event.context.get_guild().name}`|`{event.context.get_guild().id}`\nОшибка ```python\n{type(event.exception.__cause__).__name__}: {event.exception.__cause__}```",
            role_mentions = True
        )
        return
    if isinstance(event.exception, lightbulb.NotOwner):
        await event.context.respond(
            "https://cdn.discordapp.com/attachments/996413253456511096/1083467516568948829/IMG_20230309_160732_416.jpg", 
            flags=hikari.MessageFlag.EPHEMERAL
            )
        return
    if isinstance(event.exception, lightbulb.MissingRequiredPermission):
        await event.context.respond(
            l["error.MissingRequiredPermission"],
            flags=hikari.MessageFlag.EPHEMERAL
        )
        return
    if isinstance(event.exception, lightbulb.CheckFailure):
        await event.context.respond(
            l["error.CheckFailure"], 
            flags=hikari.MessageFlag.EPHEMERAL
            )
        return
    if isinstance(event.exception, lightbulb.CommandIsOnCooldown):
        dt = datetime.datetime.now()
        value = datetime.datetime.fromtimestamp(time.mktime(dt.timetuple()))
        conv = datetime.datetime.strptime(str(value), '%Y-%m-%d %H:%M:%S').timestamp()
        await event.context.respond(
            l["error.CommandIsOnCooldown"].format(round(conv) + round(event.exception.retry_after)),
            flags=hikari.MessageFlag.EPHEMERAL
        )
        return

def load(client):
    client.add_plugin(plugin)
