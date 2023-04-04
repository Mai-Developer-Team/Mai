import lightbulb
import hikari
import miru

from config import setting
from utils import local, db


plugin = lightbulb.Plugin("guild_setting", default_enabled_guilds=setting.guild_id)

#TODO: сделать после релиза)
class ServerSettingButton(miru.View):
    
    @miru.button(label=":gear:", style=hikari.ButtonStyle.PRIMARY)
    async def logsSetting(self, button: miru.Button, ctx: miru.ViewContext):
        ...

@plugin.command()
@lightbulb.add_checks(
    lightbulb.has_role_permissions(hikari.Permissions.MANAGE_GUILD)
)
@lightbulb.command("guild_setting", "Настройки сервера")
@lightbulb.implements(lightbulb.SlashCommand)
async def guild_setting(ctx: lightbulb.Context) -> None:
    #TODO: привязать бд, локализацию и добавить кнопки на управление
    ser = db.server(ctx.get_guild().id)

    emb = hikari.Embed(
        title = f"Настройки сервера {ctx.get_guild().name}",
        description="Здесь находятся все настройки сервера для удобного использования бота",
        color = setting.color
    )
    emb.add_field(name="Основной язык", value = ser["localization"])
    if ser["premium"] == 1:
        emb.add_field(name="Буст", value="На этом сервере доступны команды, которые проходят публичный бета-тест")
    if ser["blockSettings"] == True:
        emb.add_field(name="Внимание", value="На данном сервере были заблокированы любые настройки разработчиком")

    emb.set_thumbnail(ctx.get_guild().icon_url)

    button = ServerSettingButton()
    msg = await ctx.respond(embed=emb, component=button)
    await button.start(msg)

def load(client):
    client.add_plugin(plugin)