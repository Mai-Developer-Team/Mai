import lightbulb
import hikari
import miru

from config import setting
from utils import local, db


plugin = lightbulb.Plugin("guild_setting", default_enabled_guilds=setting.guild_id)


@plugin.command()
@lightbulb.add_checks(
    lightbulb.has_role_permissions(hikari.Permissions.MANAGE_GUILD)
)
@lightbulb.command("guild_setting", "Настройки сервера")
@lightbulb.implements(lightbulb.SlashCommand)
async def guild_setting(ctx: lightbulb.Context) -> None:
    #TODO: привязать бд, локализацию и добавить кнопки на управление
    ser = db.server(ctx.get_guild().id)
    l = local.localization(ctx.get_guild().id)

    class LocalButton(miru.View):
        @miru.button(emoji="🇷🇺")
        async def ru_button(self, button: miru.Button, ctx: miru.ViewContext):
            ...
        @miru.button(emoji="<:c_w_:837281007693594665>")
        async def ru_meow_button(self, button: miru.Button, ctx: miru.ViewContext):
            ...

        @miru.button(emoji="🇧🇾")
        async def by_button(self, button: miru.Button, ctx: miru.ViewContext):
            ...

        @miru.button(emoji="🇬🇧")
        async def en_button(self, button: miru.Button, ctx: miru.ViewContext):
            ...

    if ser["blockSettings"] != True:
        class SettingButton(miru.View):
            @miru.button(label="Язык", style=hikari.ButtonStyle.SECONDARY)
            async def lang(self, button: miru.Button, ctx: miru.ViewContext):
                view = LocalButton()
                emb = (
                    hikari.Embed(
                        title="Смена языка",
                        description="Здесь вы можете поменять язык в боте. Можно так же помочь в переводе [на гитхабе](https://github.com/Mai-Developer-Team/Mai/tree/dev/src/config/localization)\nВнизу отображены флаги стран, где используется тот или иной язык(и не только)",
                        color=setting.color
                    )
                )
                q = await ctx.edit_response(embed=emb, components=view, flags=hikari.MessageFlag.EPHEMERAL)
                await view.start(q)

            @miru.button(label="Отключение команд", style=hikari.ButtonStyle.SECONDARY)
            async def disable(self, button: miru.Button, ctx: miru.ViewContext):
                ...

            @miru.button(label="Буст", style=hikari.ButtonStyle.SECONDARY)
            async def boost(self, button: miru.Button, ctx: miru.ViewContext):
                ...
    else:
        class SettingButton(miru.View):
            @miru.button(label="Язык", style=hikari.ButtonStyle.SECONDARY, disabled=True)
            async def lang(self, button: miru.Button, ctx: miru.ViewContext):
                ...

            @miru.button(label="Отключение команд", style=hikari.ButtonStyle.SECONDARY, disabled=True)
            async def disable(self, button: miru.Button, ctx: miru.ViewContext):
                ...

            @miru.button(label="Буст", style=hikari.ButtonStyle.SECONDARY, disabled=True)
            async def boost(self, button: miru.Button, ctx: miru.ViewContext):
                ...

    lang_ser = {
        "ru-RU": l["lang"],
        "ru-MEOW": l["lang"],
        "by-BY": l["lang"],
        "en-US": l["lang"],
        "es-ES": l["lang"],
    }

    emb = hikari.Embed(
        title = f"Настройки сервера {ctx.get_guild().name}",
        description="Здесь находятся все настройки сервера для удобного использования бота",
        color = setting.color
    )
    emb.add_field(name="Основной язык", value = lang_ser[str(ser["localization"])])
    if ser["disableCommand"] == False:
        emb.add_field(name="Экономические команды", value="На данном сервере экономические команды не отключены")
    else:
        emb.add_field(name="Экономические команды", value="На данном сервере экономические команды отключены")
    if ser["premium"] == 1:
        emb.add_field(name="Буст", value="На этом сервере доступны команды, которые проходят публичный бета-тест")
    if ser["blockSettings"] == True:
        emb.add_field(name="Внимание", value="На данном сервере были заблокированы любые настройки разработчиком")

    emb.set_thumbnail(ctx.get_guild().icon_url)

    button = SettingButton()
    msg = await ctx.respond(embed=emb, components=button, flags=hikari.MessageFlag.EPHEMERAL)
    await button.start(msg)

def load(client):
    client.add_plugin(plugin)