import lightbulb

from config import setting
from utils import boticord_api

plugin = lightbulb.Plugin("up", default_enabled_guilds=setting.guild_id)


@plugin.command()
@lightbulb.command("up", "Повысить сервер на BotiCord.top")
@lightbulb.implements(lightbulb.SlashCommand)
async def up(ctx: lightbulb.Context) -> None:
    guild = ctx.get_guild()
    serv = boticord_api.server(guild.id)
    if serv.status_code == 404:
        await ctx.respond("<:bc:941035403182489690> Типа тут текст, что сервера нет")
    else:
        owner = await ctx.bot.rest.fetch_member(guild.id, guild.owner_id)
        member_online = await ctx.bot.rest.fetch_invite(serv.json()["links"]["invite"])

        ups = boticord_api.up(
            guild.id,
            guild.name,
            guild.icon_url,
            len(guild.get_members),
            member_online.approximate_active_member_count,
            owner.username,
            owner.discriminator,
            ctx.member.id,
            ctx.get_channel().id,
            ctx.get_channel().name
        )

        await ctx.respond(ups)


def load(client):
    client.add_plugin(plugin)