import lightbulb
import hikari

from boticordpy import BotiCordWebsocket

from config import setting
from utils import db

plugin = lightbulb.Plugin("bc_notify", default_enabled_guilds=setting.guild_id)
websocket = BotiCordWebsocket(setting.bc_api)


@websocket.listener()
async def up_added(data):
    user = data['user']
    resource = data['id']

    if resource == "802987390033330227":
        d = db.user(user)

        if d["nothing"] != False:
            db.db.user.update_one(
                {"id": user},
                {
                    "$set": {
                        "coin": 800
                    }
                }
            )

            us = await plugin.bot.rest.fetch_user(user)

            await us.send("<:boticord:1129078945506152501> Благодарим за ап! Ваша награда 800 :coin:")


@plugin.listener(hikari.StartedEvent)
async def bc_notify_api(event: hikari.StartedEvent):
    await websocket.connect()


def load(client):
    client.add_plugin(plugin)
