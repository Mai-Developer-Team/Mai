import lightbulb
import hikari

from config import setting

plugin = lightbulb.Plugin("shard_tracker")

@plugin.listener(hikari.ShardConnectedEvent)
async def connect(event: hikari.ShardConnectedEvent):
    
    emb = hikari.Embed(
        title = "Шард подключился",
        color = setting.color
    )
    emb.add_field(name = "Шард ID", value = event.shard._shard_id)

    await plugin.bot.rest.execute_webhook(
        setting.webhook_id,
        setting.webhook_token,
        '<@&890683001065848842>',
        embed=emb
    )
    
@plugin.listener(hikari.ShardDisconnectedEvent)
async def disconnect(event: hikari.ShardDisconnectedEvent):
    
    emb = hikari.Embed(
        title = "Шард отключился",
        color = setting.color
    )
    emb.add_field(name = "Шард ID", value = event.shard._shard_id)

    await plugin.bot.rest.execute_webhook(
        setting.webhook_id,
        setting.webhook_token,
        '<@&890683001065848842>',
        embed=emb
    )

@plugin.listener(hikari.ShardResumedEvent)
async def resume(event: hikari.ShardResumedEvent):
    
    emb = hikari.Embed(
        title = "Шард возобновлен",
        color = setting.color
    )
    emb.add_field(name = "Шард ID", value = event.shard._shard_id)

    await plugin.bot.rest.execute_webhook(
        setting.webhook_id,
        setting.webhook_token,
        '<@&890683001065848842>',
        embed=emb
    )

@plugin.listener(hikari.ShardReadyEvent)
async def ready(event: hikari.ShardReadyEvent):
    
    emb = hikari.Embed(
        title = "Шард готов",
        color = setting.color
    )
    emb.add_field(name = "Шард ID", value = event.shard._shard_id)

    await plugin.bot.rest.execute_webhook(
        setting.webhook_id,
        setting.webhook_token,
        '<@&890683001065848842>',
        embed=emb
    )


def load(client):
    client.add_plugin(plugin)