import lightbulb

plugin = lightbulb.Plugin("ping")


@plugin.command()
@lightbulb.command("ping")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:

    await ctx.send("pong")


plugin.command(ping)

