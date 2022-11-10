import lightbulb
import hikari

from config import setting

plugin = lightbulb.Plugin("status_tracker")


@plugin.listener(hikari.StartedEvent)
async def started(event: hikari.StartedEvent):

    emb = hikari.Embed(
        title = "Код бота заработал успешно/основная часть работает",
        color = setting.color
    )
    emb.add_field(name = "Статус", value = "<:lapka:1008685525596643380>")

    await plugin.bot.rest.execute_webhook(
        setting.webhook_id_status,
        setting.webhook_token_status,
        '<@&890683001065848842>',
        embed=emb
    )


@plugin.listener(hikari.StartingEvent)
async def starting(event: hikari.StoppingEvent):

    emb = hikari.Embed(
        title = "Бот подключился к Discord API",
        color = setting.color
    )
    emb.add_field(name = "Статус", value = "<:masero:895402664102330368>")

    await plugin.bot.rest.execute_webhook(
        setting.webhook_id_status,
        setting.webhook_token_status,
        '<@&890683001065848842>',
        embed=emb
    )


@plugin.listener(hikari.StoppedEvent)
async def stopped(event: hikari.StoppingEvent):

    emb = hikari.Embed(
        title = "Бот отключился",
        color = setting.color
    )
    emb.add_field(name = "Статус", value = "<:PaimonAngry:951909102253142096>")

    await plugin.bot.rest.execute_webhook(
        setting.webhook_id_status,
        setting.webhook_token_status,
        '<@&890683001065848842>',
        embed=emb
    )


@plugin.listener(hikari.StoppingEvent)
async def stopping(event: hikari.StoppingEvent):

    emb = hikari.Embed(
        title = "Вы полностью отключили бота",
        color = setting.color
    )
    emb.add_field(name = "Статус", value = "<a:catFlex:858073711922774068>")

    await plugin.bot.rest.execute_webhook(
        setting.webhook_id_status,
        setting.webhook_token_status,
        '<@&890683001065848842>',
        embed=emb
    )


def load(client):
    client.add_plugin(plugin)
