import hikari 
import lightbulb
import miru

from config import setting
from utils import local

plugin = lightbulb.Plugin("user_setting", default_enabled_guilds=setting.guild_id)

#TODO: все сделать!

class UserSetting(miru.View):

    def __init__(self, author: hikari.User) -> None:
        self.author = author
        super().__init__(timeout=60)
    
    @miru.button(label="Click me!", style=hikari.ButtonStyle.SUCCESS)
    async def basic_button(self, button: miru.Button, ctx: miru.ViewContext) -> None:
        await ctx.respond("You clicked me!")
    
    async def on_timeout(self) -> None:
        await self.message.edit(":c", components=[])


@plugin.command()
@lightbulb.command("user_setting", "Настройка профиля")
@lightbulb.implements(lightbulb.SlashCommand)
async def user_setting(ctx: lightbulb.Context) -> None:

    button = UserSetting()
    msg = await ctx.respond("test", components=button)
    await button.start(msg)


def load(client):
    client.add_plugin(plugin)
