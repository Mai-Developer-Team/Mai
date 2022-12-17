import hikari
import lightbulb

from config import setting

plugin = lightbulb.Plugin("error", default_enabled_guilds=setting.guild_id)


@plugin.listener(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:

    if isinstance(event.exception, lightbulb.CommandInvocationError):
        await event.context.respond('Произошла критическая ошибка в команде! Если ничего не измениться, то обратитесь на сервер поддержки')
        ping = "<@&807901614450671637>"
    if isinstance(event.exception, lightbulb.NotOwner):
        await event.context.respond("https://http.cat/400")

    thread = await event.bot.rest.create_thread(1053706633487859722, 11, f"Ошибка в команде {event.context.command.name}")
    await thread.send(
        f"{ping or None}\nИспользовал её **{event.context.member}** в гильдии `{event.context.get_guild().name}`|`{event.context.get_guild().id}`\nОшибка ```python\n{type(event.exception.__cause__).__name__}: {event.exception.__cause__}```"
    )

def load(client):
    client.add_plugin(plugin)
