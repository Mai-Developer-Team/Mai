import lightbulb
import hikari

from config import setting
from utils import local


plugin = lightbulb.Plugin("serverinfo", default_enabled_guilds=setting.guild_id)


@plugin.command()
@lightbulb.command("serverinfo", "Информация о данном сервере")
@lightbulb.implements(lightbulb.SlashCommand)
async def serverinfo(ctx: lightbulb.Context) -> None:
    l = local.localization(ctx.get_guild().id)

    guild = ctx.get_guild()
    member = guild.get_members()
    rules = await guild.fetch_rules_channel() or l["serverinfo.general_channel.NONE"]
    systems = await guild.fetch_system_channel() or l["serverinfo.general_channel.NONE"]

    lang_server = {
        "de": l["serverinfo.lang_server.de"],
        "en-US": l["serverinfo.lang_server.en-US"],
        "ru": l["serverinfo.lang_server.ru"],
        "uk": l["serverinfo.lang_server.uk"]
    }
    verify_server = {
        "NONE": l["serverinfo.verify_server.NONE"],
        "LOW": l["serverinfo.verify_server.LOW"],
        "MEDIUM": l["serverinfo.verify_server.MEDIUM"],
        "HIGH": l["serverinfo.verify_server.HIGH"],
        "VERY_HIGH": l["serverinfo.verify_server.VERY_HIGH"]
    }
    premium_tier = {
        "NONE": 0,
        "TIER_1": 1,
        "TIER_2": 2,
        "TIER_3": 3
    }

    emb = (
        hikari.Embed(
            title = l["serverinfo.title"].format(guild.name),
            description = guild.description,
            color = setting.color
        )
        .add_field(
            name = l["serverinfo.name.general_information"],
            value = l["serverinfo.value.general_information"].format(
                guild.owner_id, 
                lang_server[str(guild.preferred_locale)], 
                verify_server[str(guild.verification_level)]
            )
        )
        .add_field(
            name = l["serverinfo.name.general_channel"],
            value = l["serverinfo.value.general_channel"].format(
                rules, 
                systems
            )
        )
        .add_field(
            name = l["serverinfo.name.member"],
            value = l["serverinfo.value.member"].format(
                len(member)
            )
        )
        .add_field(
            name = l["serverinfo.name.boost_information"],
            value = l["serverinfo.value.boost_information"].format(
                premium_tier[str(guild.premium_tier)],
                guild.premium_subscription_count
            )
        )
        .set_thumbnail(guild.icon_url)
        .set_image(guild.banner_url)
    )

    await ctx.respond(embed=emb)

def load(client):
    client.add_plugin(plugin)
