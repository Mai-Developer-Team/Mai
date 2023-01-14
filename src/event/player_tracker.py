import lightbulb
import hikari
import lavaplayer

import asyncio

plugin = lightbulb.Plugin("player_tracker")
lavalink = lavaplayer.LavalinkClient(
    host = "localhost", 
    port = 2333,  
    password = "123"
)

@plugin.listener(hikari.StartedEvent)
async def started(event: hikari.StartedEvent):
    lavalink.set_user_id(plugin.bot.get_me().id)
    lavalink.set_event_loop(asyncio.get_event_loop())
    lavalink.connect()
    print('* Бот подключился к лавалинку')

@plugin.listener(hikari.VoiceStateUpdateEvent)
async def voice_state_update(event: hikari.VoiceStateUpdateEvent):
    await lavalink.raw_voice_state_update(event.guild_id, event.state.user_id, event.state.session_id, event.state.channel_id)

@plugin.listener(hikari.VoiceServerUpdateEvent)
async def voice_server_update(event: hikari.VoiceServerUpdateEvent):
    await lavalink.raw_voice_server_update(event.guild_id, event.endpoint, event.token)

def load(client):
    client.add_plugin(plugin)