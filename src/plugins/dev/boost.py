import lightbulb
import hikari

from config import setting
from utils import db

import datetime


plugin = lightbulb.Plugin("boost", default_enabled_guilds=setting.guild_id)


@plugin.command()
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.command("Выдача прeмиум", "Выдать премиум пользователю")
@lightbulb.implements(lightbulb.UserCommand)
async def boost(ctx: lightbulb.Context) -> None:
    user = ctx.options.target
    premium = db.premium(user.id)
    
    if premium is None:
        '''
        Ебитесь сами, почему здесь так)
        '''
        db.db.premium.insert_one(
            {
                "expireAt": datetime.datetime.now() + datetime.timedelta(hours = -3, days = 30), 
                "originalDate": datetime.datetime.now() + datetime.timedelta(days = 30),
                "id": user.id
            }
        )

        if db.user(user.id)["badge"] == None:
            db.db.user.update_one(
                { "id": user.id }, 
                { 
                    "$set": {
                        "badge":"<:support:1062013867762389072>"
                        }
                }
                
            )

        await ctx.respond(f"Было выдано 30 дней подписки пользователю {user}", flags=hikari.MessageFlag.EPHEMERAL)

        await user.send(embed = (hikari.Embed(
            title = "Оповещение", 
            description=f'Вам была выдана подписка до **{datetime.datetime.strftime(db.premium(user.id)["originalDate"].replace(microsecond=0), "%d.%m.%Y")}**.\nСпасибо за покупку и поддержку бота!',
            color=setting.color
            )
            .set_image("https://i.pinimg.com/originals/c0/1d/02/c01d02a50d9f84de5ad8919241ebe42e.gif")
            ))
    else:
        await ctx.respond(f"Я не могу выдать подписку {user}, т.к у него уже есть", flags=hikari.MessageFlag.EPHEMERAL)


def load(client):
    client.add_plugin(plugin)