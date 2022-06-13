import lightbulb
import hikari

import ast
from config import setting

plugin = lightbulb.Plugin("eval")

def insert_returns(body):
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)


@plugin.command()
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.option("code", "da", modifier=lightbulb.OptionModifier.CONSUME_REST)
@lightbulb.command("eval", description = "dev commands", hidden = True, aliases = ["e"])
@lightbulb.implements(lightbulb.PrefixCommand)
async def eval(ctx: lightbulb.Context) -> None:
    
    await ctx.respond(f"Yes, its eval :D \nCode: {ctx.options.code}")
    

def load(client):
    client.add_plugin(plugin)

