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

    class ShopButton(miru.View):

        @miru.button(emoji="🎣", style=hikari.ButtonStyle.SECONDARY)
        async def rod_list(self, button: miru.Button, ctx: miru.ViewContext) -> None:
            emb = (
                hikari.Embed(
                    title=l["shop.title.rod"],
                    description=l["shop.description.rod"].format(
                        l["fishing.rod.id.1"],
                        l["fishing.rod.id.2"],
                        l["fishing.rod.id.3"],
                        l["fishing.rod.id.4"],
                        l["fishing.rod.id.5"],
                        l["fishing.rod.id.6"],
                        l["fishing.rod.id.7"],
                        l["fishing.rod.id.8"],
                        l["fishing.rod.id.9"],
                    ),
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
                    title=l["shop.title.fish_hook"],
                    description=l["shop.description.fish_hook"].format(
                        l["fishing.fish_hook.id.1"],
                        l["fishing.fish_hook.id.2"],
                        l["fishing.fish_hook.id.3"],
                        l["fishing.fish_hook.id.4"],
                        l["fishing.fish_hook.id.5"],
                        l["fishing.fish_hook.id.6"]
                    ),
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
                    title=l["shop.title.banner"],
                    description=l["shop.description.banner"],
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
            title=l["shop.title"],
            description=l["shop.description"],
            color=setting.color
        )
    )

    if list == None and ctx.options.id == None:

        button = ShopButton()
        msg = await ctx.respond(embed=emb, components=button, flags=hikari.MessageFlag.EPHEMERAL)
        await button.start(msg)
        return

    if list == "Удочка":
        id = int(ctx.options.id)

        if user["rod"] >= id:
            await ctx.respond(l["shop.buy.rod.was"], flags=hikari.MessageFlag.EPHEMERAL)
            return

        if id <= 0:
            await ctx.respond(l["shop.buy.pay.0"], flags=hikari.MessageFlag.EPHEMERAL)
            return

        if id == 1:
            if user["coin"] <= 900:
                await ctx.respond(l["shop.buy.pay.false"].format(900-user["coin"]), flags=hikari.MessageFlag.EPHEMERAL)
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "rod": id
                }}
            )

            await ctx.respond(l["shop.buy.pay.done"].format(l["fishing.rod.id.1"]))
            return
        if id == 2:
            if user["coin"] <= 2000:
                await ctx.respond(l["shop.buy.pay.false"].format(2000-user["coin"]), flags=hikari.MessageFlag.EPHEMERAL)
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "rod": id
                }}
            )

            await ctx.respond(l["shop.buy.pay.done"].format(l["fishing.rod.id.2"]))
            return
        if id == 3:
            if user["coin"] <= 4500:
                await ctx.respond(await ctx.respond(l["shop.buy.pay.false"].format(4500-user["coin"]), flags=hikari.MessageFlag.EPHEMERAL))
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "rod": id
                }}
            )

            await ctx.respond(l["shop.buy.pay.done"].format(l["fishing.rod.id.3"]))
            return
        if id == 4:
            if user["coin"] <= 7800:
                await ctx.respond(await ctx.respond(l["shop.buy.pay.false"].format(7800-user["coin"]), flags=hikari.MessageFlag.EPHEMERAL))
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "rod": id
                }}
            )

            await ctx.respond(l["shop.buy.pay.done"].format(l["fishing.rod.id.4"]))
            return
        if id == 5:
            if user["coin"] <= 11000:
                await ctx.respond(await ctx.respond(l["shop.buy.pay.false"].format(11000-user["coin"]), flags=hikari.MessageFlag.EPHEMERAL))
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "rod": id
                }}
            )

            await ctx.respond(l["shop.buy.pay.done"].format(l["fishing.rod.id.5"]))
            return
        if id == 6:
            if user["coin"] <= 16500:
                await ctx.respond(await ctx.respond(l["shop.buy.pay.false"].format(16500-user["coin"]), flags=hikari.MessageFlag.EPHEMERAL))
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "rod": id
                }}
            )

            await ctx.respond(l["shop.buy.pay.done"].format(l["fishing.rod.id.6"]))
            return
        if id == 7:
            if user["coin"] <= 20000:
                await ctx.respond(await ctx.respond(l["shop.buy.pay.false"].format(20000-user["coin"]), flags=hikari.MessageFlag.EPHEMERAL))
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "rod": id
                }}
            )

            await ctx.respond(l["shop.buy.pay.done"].format(l["fishing.rod.id.7"]))
            return
        if id == 8:
            if user["coin"] <= 27000:
                await ctx.respond(await ctx.respond(l["shop.buy.pay.false"].format(27000-user["coin"]), flags=hikari.MessageFlag.EPHEMERAL))
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "rod": id
                }}
            )

            await ctx.respond(l["shop.buy.pay.done"].format(l["fishing.rod.id.8"]))
            return
        if id == 9:
            if user["coin"] <= 40000:
                await ctx.respond(await ctx.respond(l["shop.buy.pay.false"].format(40000-user["coin"]), flags=hikari.MessageFlag.EPHEMERAL))
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "rod": id
                }}
            )

            await ctx.respond(l["shop.buy.pay.done"].format(l["fishing.rod.id.9"]))
            return
        else:
            await ctx.respond(l["shop.buy.rod.none"], flags=hikari.MessageFlag.EPHEMERAL)

    if list == "Крючок":
        id = int(ctx.options.id)

        if user["fish_hook"] >= id:
            await ctx.respond(l["shop.buy.fish_hook.was"], flags=hikari.MessageFlag.EPHEMERAL)
            return

        if id <= 0:
            await ctx.respond(l["shop.buy.pay.0"], flags=hikari.MessageFlag.EPHEMERAL)
            return

        if id == 1:
            if user["coin"] <= 250:
                await ctx.respond(await ctx.respond(l["shop.buy.pay.false"].format(250-user["coin"]), flags=hikari.MessageFlag.EPHEMERAL))
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "fish_hook": id
                }}
            )

            await ctx.respond(l["shop.buy.pay.done"].format(l["fishing.fish_hook.id.1"]))
            return
        if id == 2:
            if user["coin"] <= 500:
                await ctx.respond(await ctx.respond(l["shop.buy.pay.false"].format(500-user["coin"]), flags=hikari.MessageFlag.EPHEMERAL))
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "fish_hook": id
                }}
            )

            await ctx.respond(l["shop.buy.pay.done"].format(l["fishing.fish_hook.id.2"]))
            return
        if id == 3:
            if user["coin"] <= 1250:
                await ctx.respond(await ctx.respond(l["shop.buy.pay.false"].format(1250-user["coin"]), flags=hikari.MessageFlag.EPHEMERAL))
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "fish_hook": id
                }}
            )

            await ctx.respond(l["shop.buy.pay.done"].format(l["fishing.fish_hook.id.3"]))
            return
        if id == 4:
            if user["coin"] <= 2500:
                await ctx.respond(await ctx.respond(l["shop.buy.pay.false"].format(2500-user["coin"]), flags=hikari.MessageFlag.EPHEMERAL))
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "fish_hook": id
                }}
            )

            await ctx.respond(l["shop.buy.pay.done"].format(l["fishing.fish_hook.id.4"]))
            return
        if id == 5:
            if user["coin"] <= 3600:
                await ctx.respond(await ctx.respond(l["shop.buy.pay.false"].format(3600-user["coin"]), flags=hikari.MessageFlag.EPHEMERAL))
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "fish_hook": id
                }}
            )

            await ctx.respond(l["shop.buy.pay.done"].format(l["fishing.fish_hook.id.5"]))
            return
        if id == 6:
            if user["macoin"] <= 25:
                await ctx.respond(await ctx.respond(l["shop.buy.pay.false"].format(25-user["macoin"]), flags=hikari.MessageFlag.EPHEMERAL))
                return

            db.db.user.update_one(
                {"id": ctx.author.id},
                {"$set": {
                    "fish_hook": id
                }}
            )

            await ctx.respond(l["shop.buy.pay.done"].format(l["fishing.fish_hook.id.6"]))
            return
        else:
            await ctx.respond(l["shop.buy.fish_hook.none"], flags=hikari.MessageFlag.EPHEMERAL)

def load(client):
    client.add_plugin(plugin)