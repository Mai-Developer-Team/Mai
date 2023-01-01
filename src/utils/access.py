import lightbulb

from utils import db


@lightbulb.Check
def alpha_tester(context: lightbulb.Context) -> bool:
    return context.author.id == [364437278728388611, 675714186898309133]

@lightbulb.Check
def beta_tester(context: lightbulb.Context) -> bool:
    guild_tester = db.server(context.get_guild().id)
    owner_boost = db.premium(context.get_guild().owner_id)

    if owner_boost != None and guild_tester["premium"] == 1:
        return context.get_guild().id
