import lightbulb
import hikari
import miru

from config import setting
from utils import local, access, db

plugin = lightbulb.Plugin("shop", default_enabled_guilds=setting.guild_id)


@plugin.command()
@lightbulb.add_checks(access.disable_command)
@lightbulb.option(
    name="list",
    description="Выберите из списка, что вы хотите купить",
    type = hikari.OptionType.STRING,
    choices=[
        "Удочка",
        "Крючок",
        "Баннер"
    ],
    required=False
)
@lightbulb.option(
    name="id",
    description="ID покупки",
    type= hikari.OptionType.INTEGER,
    required=False
)
@lightbulb.command("shop", "Глобальный магазин бота")
@lightbulb.implements(lightbulb.SlashCommand)
async def shop(ctx: lightbulb.Context) -> None:
    l = local.localization(ctx.get_guild().id)
    user = db.user(ctx.author.id)
    list = ctx.options.list
    id = int(ctx.options.id)

    class ShopButton(miru.View):

        @miru.button(emoji="🎣", style=hikari.ButtonStyle.SECONDARY)
        async def rod_list(self, button: miru.Button, ctx: miru.ViewContext) -> None:
            emb = (
                hikari.Embed(
                    title="Список доступных удочек",
                    description="Ага",
                    color=setting.color
                )
            )
            await ctx.respond(
                embed=emb,
                component=None,
                flags=hikari.MessageFlag.EPHEMERAL
            )

        @miru.button(emoji="🪝", style=hikari.ButtonStyle.SECONDARY)
        async def fish_hook_list(self, button: miru.Button, ctx: miru.ViewContext) -> None:
            emb = (
                hikari.Embed(
                    title="Список доступных крючков",
                    description="Ага",
                    color=setting.color
                )
            )
            await ctx.respond(
                embed=emb,
                component=None,
                flags=hikari.MessageFlag.EPHEMERAL
            )

        @miru.button(emoji="🖼️", style=hikari.ButtonStyle.SECONDARY)
        async def banner_list(self, button: miru.Button, ctx: miru.ViewContext):
            emb = (
                hikari.Embed(
                    title="Список доступных баннеров",
                    description="Весь список баннеров находиться [здесь](https://boticord.gay)",
                    color=setting.color
                )
            )
            await ctx.respond(
                embed=emb,
                component=None,
                flags=hikari.MessageFlag.EPHEMERAL
            )


    emb = (
        hikari.Embed(
            title="Магазин бота",
            description="Здесь вы можете покупать как удочки и крючки, так и баннеры для своего профиля\nДля дополнительной информацией посетите [документацию](https://docs.maibot.xyz)",
            color=setting.color
        )
    )

    if list and id == None:
        button = ShopButton()
        msg = await ctx.respond(embed=emb, components=button, flags=hikari.MessageFlag.EPHEMERAL)
        await button.start(msg)

    if list == "Удочка":

        if user["rod"] >= id:
            await ctx.respond("У вас уже есть такая удочка или была в использовании")
            return

        if id <= 0:
            await ctx.respond(123)

        if id == 1:
            if user["coin"] < 100:
                await ctx.respond("У вас нет денег на покупку F")
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "rod": id
                }}
            )

            await ctx.respond("Благодарим за покупку")
        else:
            await ctx.respond("такой удочки не существует")


def load(client):
    client.add_plugin(plugin)