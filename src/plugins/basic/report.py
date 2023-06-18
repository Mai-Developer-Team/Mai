import lightbulb
import hikari
import miru

from config import setting
from utils import local, db

plugin = lightbulb.Plugin("report", default_enabled_guilds=setting.guild_id)


class ReportButton(miru.View):

    @miru.button(label="принять", style=hikari.ButtonStyle.SUCCESS)
    async def success_button(self, button: miru.Button, ctx: miru.ViewContext):
        await ctx.edit_response(f"жалоба была обработана **{ctx.author}**", component=None)

    @miru.button(label="отклонить", style=hikari.ButtonStyle.DANGER)
    async def danger_button(self, button: miru.Button, ctx: miru.ViewContext):
        await ctx.edit_response(f"жалоба отказана **{ctx.author}**", component=None)

@plugin.command()
@lightbulb.option(
    "member",
    "Укажите пользователя или ID",
    type = hikari.OptionType.USER,
    required=True
)
@lightbulb.option(
    "reason",
    "причина репорта",
    type = hikari.OptionType.STRING,
    required=True
)
@lightbulb.option(
    "image",
    "скриншот где данный пользователь нарушает",
    type = hikari.OptionType.ATTACHMENT,
    required=True
)
@lightbulb.command("report", "пожаловаться на пользователя, который нарушает discord ToS")
@lightbulb.implements(lightbulb.SlashCommand)
async def report(ctx: lightbulb.Context) -> None:
    member = ctx.options.member
    reason = ctx.options.reason
    image = ctx.options.image

    if ctx.author.id == member.id:
        await ctx.respond(
            "a",
            flags=hikari.MessageFlag.EPHEMERAL
        )
        return
    if db.user(ctx.author.id)["blacklist"]["block"] == 1:
        await ctx.respond(
            "Вы находитесь в черном списке бота, поэтому не можете отправлять жалобы на других пользователей",
            flags=hikari.MessageFlag.EPHEMERAL
        )
        return
    if db.user(member.id)["blacklist"]["block"] == 1:
        await ctx.respond(
            "Данный пользователь уже был наказан",
            flags=hikari.MessageFlag.EPHEMERAL
        )
        return
    if db.db.report.find_one({"id": member.id}) == None:
        db.db.report.insert_one({
            "id": member.id,
            "reason": reason,
            "image": image.url,
            "sender": ctx.author.id
        })

        await ctx.respond(
            "Спасибо за жалобу, мы в скором времени её рассмотрим!",
            flags=hikari.MessageFlag.EPHEMERAL
        )

        button = ReportButton()
        channel = await plugin.bot.rest.fetch_channel(1120001098372100197)
        msg = await channel.send(
            embed = (
                hikari.Embed(
                    title = f"Жалоба на {member}",
                    color = setting.color
                )
                .add_field(name="Отправитель", value=ctx.author)
                .add_field(name="ID отправителя", value=ctx.author.id)
                .add_field(name="Причина жалобы", value=reason)
                .add_field(name="ID пользователя на которого была подана жалоба", value=member.id)
                .set_image(image.url)
            ),
            components=button
        )
        await button.start(msg)
        return
    else:
        await ctx.respond(
            "На данного пользователя уже был отправлена жалоба",
            flags=hikari.MessageFlag.EPHEMERAL
        )
        return

def load(client):
    client.add_plugin(plugin)
