import lightbulb
import hikari
import miru

from config import setting
from utils import local, db


plugin = lightbulb.Plugin("guild_setting")


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
            if ser["localization"] == "ru-RU":
                await ctx.respond(l["guild_setting.button.lang.using"],
                                  flags=hikari.MessageFlag.EPHEMERAL)
                return
            else:
                db.db.server.update_one(
                    {"id": ctx.get_guild().id},
                    {"$set": {
                        "localization": "ru-RU"
                    }}
                )
                await ctx.edit_response(l["guild_setting.button.lang.done"], embed=None, components=[],
                                        flags=hikari.MessageFlag.EPHEMERAL)
                return

        @miru.button(emoji="<:c_w_:837281007693594665>")
        async def ru_meow_button(self, button: miru.Button, ctx: miru.ViewContext):
            if ser["localization"] == "ru-MEOW":
                await ctx.respond(l["guild_setting.button.lang.using"],
                                  flags=hikari.MessageFlag.EPHEMERAL)
                return
            else:
                db.db.server.update_one(
                    {"id": ctx.get_guild().id},
                    {"$set": {
                        "localization": "ru-MEOW"
                    }}
                )
                await ctx.edit_response(l["guild_setting.button.lang.done"], embed=None, components=[],
                                        flags=hikari.MessageFlag.EPHEMERAL)
                return

        @miru.button(emoji="🇧🇾")
        async def by_button(self, button: miru.Button, ctx: miru.ViewContext):
            if ser["localization"] == "by-BY":
                await ctx.respond(l["guild_setting.button.lang.using"],
                                  flags=hikari.MessageFlag.EPHEMERAL)
                return
            else:
                db.db.server.update_one(
                    {"id": ctx.get_guild().id},
                    {"$set": {
                        "localization": "by-BY"
                    }}
                )
                await ctx.edit_response(l["guild_setting.button.lang.done"], embed=None, components=[],
                                        flags=hikari.MessageFlag.EPHEMERAL)
                return

        @miru.button(emoji="🇬🇧")
        async def en_button(self, button: miru.Button, ctx: miru.ViewContext):
            if ser["localization"] == "en-US":
                await ctx.respond(l["guild_setting.button.lang.using"],
                                  flags=hikari.MessageFlag.EPHEMERAL)
                return
            else:
                db.db.server.update_one(
                    {"id": ctx.get_guild().id},
                    {"$set": {
                        "localization": "en-US"
                    }}
                )
                await ctx.edit_response(l["guild_setting.button.lang.done"], embed=None, components=[],
                                        flags=hikari.MessageFlag.EPHEMERAL)
                return

        @miru.button(emoji="<:flag_eo:1143806874311995432>")
        async def eo_button(self, button: miru.Button, ctx: miru.ViewContext):
            if ser["localization"] == "eo-EO":
                await ctx.respond(l["guild_setting.button.lang.using"],
                                  flags=hikari.MessageFlag.EPHEMERAL)
                return
            else:
                db.db.server.update_one(
                    {"id": ctx.get_guild().id},
                    {"$set": {
                        "localization": "eo-EO"
                    }}
                )
                await ctx.edit_response(l["guild_setting.button.lang.done"], embed=None, components=[],
                                        flags=hikari.MessageFlag.EPHEMERAL)
                return

    if ser["blockSettings"] != True:
        class SettingButton(miru.View):
            @miru.button(label=l["guild_setting.button.lang"], style=hikari.ButtonStyle.SECONDARY)
            async def lang(self, button: miru.Button, ctx: miru.ViewContext):
                view = LocalButton()
                emb = (
                    hikari.Embed(
                        title=l["guild_setting.button.lang.title"],
                        description=l["guild_setting.button.lang.description"],
                        color=setting.color
                    )
                )
                q = await ctx.edit_response(embed=emb, components=view, flags=hikari.MessageFlag.EPHEMERAL)
                await view.start(q)

            @miru.button(label=l["guild_setting.button.disable_command"], style=hikari.ButtonStyle.SECONDARY)
            async def disable(self, button: miru.Button, ctx: miru.ViewContext):
                if ser["disableCommand"] == False:
                    db.db.server.update_one(
                        {"id": ctx.get_guild().id},
                        {"$set": {
                            "disableCommand": True
                        }}
                    )
                    await ctx.edit_response(l["guild_setting.button.disable_command.disable"],
                                            embed=None, components=[], flags=hikari.MessageFlag.EPHEMERAL)
                    return
                else:
                    db.db.server.update_one(
                        {"id": ctx.get_guild().id},
                        {"$set": {
                            "disableCommand": False
                        }}
                    )
                    await ctx.edit_response(l["guild_setting.button.disable_command.enable"],
                                            embed=None, components=[], flags=hikari.MessageFlag.EPHEMERAL)
                    return

            @miru.button(label=l["guild_setting.button.boost"], style=hikari.ButtonStyle.SECONDARY)
            async def boost(self, button: miru.Button, ctx: miru.ViewContext):
                if ctx.get_guild().owner_id != ctx.author.id:
                    await ctx.respond(l["guild_setting.button.boost.not_owner"], flags=hikari.MessageFlag.EPHEMERAL)
                    return

                if db.premium(ctx.author.id) == None:
                    await ctx.respond(l["guild_setting.button.boost.not_premium"], flags=hikari.MessageFlag.EPHEMERAL)
                    return

                if db.user(ctx.author.id)["premium"]["guild_add_premium"] == ctx.guild_id:
                    await ctx.respond(l["guild_setting.button.boost.err_done_guild"], flags=hikari.MessageFlag.EPHEMERAL)
                    return

                if ser["premium"] == 0:
                    db.db.server.update_one(
                        {"id": ctx.get_guild().id},
                        {"$set": {
                            "premium": 1
                        }}
                    )
                    db.db.user.update_one(
                        {"id": ctx.author.id},
                        {"$set": {
                            "premium": {
                                "guild_add_premium": ctx.get_guild().id
                            }
                        }}
                    )
                    await ctx.edit_response(l["guild_setting.button.boost.done_guild"],
                                            embed=None, components=[], flags=hikari.MessageFlag.EPHEMERAL)
                    return


    else:
        class SettingButton(miru.View):
            @miru.button(label=l["guild_setting.button.lang"], style=hikari.ButtonStyle.SECONDARY, disabled=True)
            async def lang(self, button: miru.Button, ctx: miru.ViewContext):
                ...

            @miru.button(label=l["guild_setting.button.disable_command"], style=hikari.ButtonStyle.SECONDARY, disabled=True)
            async def disable(self, button: miru.Button, ctx: miru.ViewContext):
                ...

            @miru.button(label=l["guild_setting.button.boost"], style=hikari.ButtonStyle.SECONDARY, disabled=True)
            async def boost(self, button: miru.Button, ctx: miru.ViewContext):
                ...

    lang_ser = {
        "ru-RU": l["lang"],
        "ru-MEOW": l["lang"],
        "by-BY": l["lang"],
        "en-US": l["lang"],
        "eo-EO": l["lang"],
    }

    emb = hikari.Embed(
        title = l["guild_setting.title.main"].format(ctx.get_guild().name),
        description=l["guild_setting.description.main"],
        color = setting.color
    )
    emb.add_field(name=l["guild_setting.main_lang"], value = lang_ser[str(ser["localization"])])
    if ser["disableCommand"] == False:
        emb.add_field(name=l["guild_setting.eco_command"], value=l["guild_setting.eco_command.enable"])
    else:
        emb.add_field(name=l["guild_setting.eco_command"], value=l["guild_setting.eco_command.disable"])
    if db.user(ctx.author.id)["premium"]["guild_add_premium"] == ctx.guild_id and ser["premium"] == 1:
        emb.add_field(name=l["guild_setting.boost"], value=l["guild_setting.boost.enable"])
    if ser["blockSettings"] == True:
        emb.add_field(name=l["guild_setting.disable_setting.name"], value=l["guild_setting.disable_setting.value"])

    emb.set_thumbnail(ctx.get_guild().icon_url)

    button = SettingButton()
    msg = await ctx.respond(embed=emb, components=button, flags=hikari.MessageFlag.EPHEMERAL)
    await button.start(msg)


def load(client):
    client.add_plugin(plugin)
