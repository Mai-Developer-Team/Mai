import lightbulb

from utils import db

#доступ, который затрагивает использование команд на уровне разработки
@lightbulb.Check
def alpha_tester(context: lightbulb.Context) -> bool:
    return context.author.id == 364437278728388611

@lightbulb.Check
def beta_tester(context: lightbulb.Context) -> bool:
    guild_tester = db.server(context.get_guild().id)
    owner_boost = db.premium(context.get_guild().owner_id)

    if owner_boost != None and guild_tester["premium"] == 1:
        return context.get_guild().id

#доступ, на уровне настроек сервера пользователей
@lightbulb.Check
def disable_command(context: lightbulb.Context) -> bool:
    guild_setting = db.server(context.get_guild().id)
    
    if guild_setting["disableCommand"] == False:
        return context.get_guild().id