import lightbulb
import hikari

from config import setting

import typing
import ast
import textwrap


plugin = lightbulb.Plugin("eval", default_enabled_guilds=setting.guild_id)


@plugin.command()
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.command('выполнить', ...)
@lightbulb.implements(lightbulb.MessageCommand)
async def eval(ctx: lightbulb.Context) -> None:
    #Код не мой евала, так что не бить если что-то не работает
    cmd = ctx.options.target.content
    
    globals_dict = {
        "_author": ctx.author,
        "_bot": ctx.bot,
        "_app": ctx.app,
        "_channel": ctx.get_channel(),
        "_guild": ctx.get_guild(),
        "_ctx": ctx,
    }

    code = cmd.replace("```py", "").replace("`", "").strip()

    abstract_syntax_tree = ast.parse(code, filename=f"{ctx.guild_id}{ctx.channel_id}.py")
    node: typing.List[ast.stmt] = abstract_syntax_tree.body

    if node and type(node[0]) is ast.Expr:
        code_split = code.split("\n")
        code_split[-1] = f"return {code_split[-1]}"
        code = "\n".join(code_split)

    code_func = f"async def _container():\n" + textwrap.indent(code, "   ")

    emb = hikari.Embed(title="Выполнение команды", color=setting.color)

    async with ctx.app.rest.trigger_typing(ctx.channel_id):
        try:
            exec(code_func, globals_dict, locals())
            return_value = await locals()["_container"]()
            emb = (
                hikari.Embed(title="Выполнение команды", description = return_value, color=setting.color)
            )
            await ctx.respond(embed=emb)

        except Exception as e:
            emb = (
                hikari.Embed(title="Произошла ошибка", description = e, color=setting.color)
            )
            await ctx.respond(embed=emb)
        


def load(client):
    client.add_plugin(plugin)