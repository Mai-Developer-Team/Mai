import lightbulb

plugin = lightbulb.Plugin("ping")


@plugin.command()
@lightbulb.command("ping", description = "da")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:

    await ctx.respond("pong")


def load(client):
    client.add_plugin(plugin)

