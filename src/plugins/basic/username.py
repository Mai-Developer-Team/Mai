import lightbulb
import hikari

from config import setting
from utils import local, db

import datetime, time


plugin = lightbulb.Plugin("username", default_enabled_guilds=setting.guild_id)


@plugin.command()
@lightbulb.option(
    "member", 
    "Укажите пользователя или ID для получения информации",
    type = hikari.OptionType.USER,
    required=False
)
@lightbulb.command(
    "userinfo", 
    "Показать информацию об пользователе"
)
@lightbulb.implements(lightbulb.SlashCommand)
async def userinfo(ctx: lightbulb.Context) -> None:
    
    if ctx.options.member is None:
        member = ctx.member
        db.user(member.id)
    else:
        member = ctx.options.member

    info = db.user(member.id)
    dtc = member.created_at.strftime('%Y-%m-%d %H:%M:%S')
    conv = datetime.datetime.strptime(dtc, '%Y-%m-%d %H:%M:%S').timestamp()

    emb = hikari.Embed(
            title="Информация о пользователе",
            color = setting.color
        )
    emb.add_field(name = "Пользователь", value=f"{member} | {member.id}")
    emb.add_field(name = "Дата регистрации", value=f"<t:{round(conv)}:D> (<t:{round(conv)}:R>)")
    emb.set_image(member.avatar_url)

    await ctx.respond(embed = emb)


def load(client):
    client.add_plugin(plugin)

