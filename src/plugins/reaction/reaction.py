import lightbulb
import hikari

from config import setting
from utils import local
from . import api_reaction

plugin = lightbulb.Plugin("reaction")


@plugin.command()
@lightbulb.option(
    "member",
    "Укажите пользователя на которого хотите использовать реакцию",
    type = hikari.OptionType.USER,
    required = True
)
@lightbulb.option(
    "choice",
    "Выберите одну из реакций",
    type = hikari.OptionType.STRING,
    choices = [
        "hug",
        "poke",
        "kiss",
        "pat",
        "happy",
        "cry",
        "slap"
    ],
    required = True
)
@lightbulb.command(
    "reaction", 
    "Разные реакции, которые помогают проявлять чувства к другим"
)
@lightbulb.implements(lightbulb.SlashCommand)
async def reaction(ctx: lightbulb.Context) -> None:
    member = ctx.options.member
    choice = ctx.options.choice
    l = local.localization(ctx.get_guild().id)

    if member.id == ctx.author.id:
        await ctx.respond(l["reaction.error"], flags=hikari.MessageFlag.EPHEMERAL)
        return
    
    else:
        req = api_reaction.img_api(choice)
        if choice == "hug":
            title = l["reaction.hug.title"]
            desc = l["reaction.hug.description"].format(ctx.author.mention, member.mention)
        if choice == "poke":
            title = l["reaction.poke.title"]
            desc = l["reaction.poke.description"].format(ctx.author.mention, member.mention)
        if choice == "kiss":
            title = l["reaction.kiss.title"]
            desc = l["reaction.kiss.description"].format(ctx.author.mention, member.mention)
        if choice == "pat":
            title = l["reaction.pat.title"]
            desc = l["reaction.pat.description"].format(ctx.author.mention, member.mention)
        if choice == "happy":
            title = l["reaction.happy.title"]
            desc = l["reaction.happy.description"].format(ctx.author.mention, member.mention)
        if choice == "cry":
            title = l["reaction.cry.title"]
            desc = l["reaction.cry.description"].format(ctx.author.mention, member.mention)
        if choice == "slap":
            title = l["reaction.slap.title"]
            desc = l["reaction.slap.description"].format(ctx.author.mention, member.mention)
        
        emb = hikari.Embed(
            title = title,
            description = desc,
            color = setting.color 
        )
        emb.set_image(req)
        await ctx.respond(embed=emb)


def load(client):
    client.add_plugin(plugin)