import lightbulb
import hikari

from config import setting
from utils import local, db


plugin = lightbulb.Plugin("guild_setting", default_enabled_guilds=setting.guild_id)


@plugin.command()
@lightbulb.command("guild_setting", "Настройки сервера")
@lightbulb.implements(lightbulb.SlashCommand)
async def stats(ctx: lightbulb.Context) -> None:
    #TODO: привязать бд, локализацию и добавить кнопки на управление

    emb = hikari.Embed(
            title = f"Настройки сервера {ctx.get_guild().name}",
            color = setting.color
    )
    emb.add_field(name = "Основной язык", value="Русский")
    emb.add_field(name = "Буст", value="На сервере доступны бета-тест команд")
    emb.add_field(name = "Что-то еще", value="не придумал")
    emb.set_thumbnail(ctx.get_guild().icon_url)

    await ctx.respond(embed=emb)


def load(client):
    client.add_plugin(plugin)