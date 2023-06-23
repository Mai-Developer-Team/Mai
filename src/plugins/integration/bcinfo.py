import lightbulb

from config import setting
from utils import boticord_api

plugin = lightbulb.Plugin("bcinfo", default_enabled_guilds=setting.guild_id)

#TODO: Сделать после выхода бк в2
@plugin.command()
@lightbulb.command("bcinfo", "узнать информацию с проекта BotiCord.top")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def bcinfo(ctx: lightbulb.Context) -> None:
    ...

@bcinfo.child
@lightbulb.command("server", "узнать информацию о сервере с проекта BotiCord.top")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def server(ctx: lightbulb.Context) -> None:
    ...

@bcinfo.child
@lightbulb.command("bot", "узнать информацию о боте с проекта BotiCord.top")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def bot(ctx: lightbulb.Context) -> None:
    ...

@bcinfo.child
@lightbulb.command("profile", "узнать информацию о пользователе с проекта BotiCord.top")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def profile(ctx: lightbulb.Context) -> None:
    ...


def load(client):
    client.add_plugin(plugin)