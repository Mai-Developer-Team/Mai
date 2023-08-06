import lightbulb
import hikari

import yookassa
from yookassa import Configuration
import uuid

from config import setting
from utils import db

plugin = lightbulb.Plugin("pay_boost", default_enabled_guilds=setting.guild_id)
Configuration.configure(setting.id_shop, setting.secret_key)


@plugin.command()
@lightbulb.option(
    "term",
    "выбирите срок покупки подписки",
    type = hikari.OptionType.STRING,
    choices= [
        "1 месяц",
        "3 месяца",
        "6 месяцев",
        "1 год"
    ]
)
@lightbulb.command("pay_boost", "покупка подписки")
@lightbulb.implements(lightbulb.SlashCommand)
async def pay_boost(ctx: lightbulb.Context) -> None:
    d = (await plugin.bot.rest.fetch_messages(ctx.channel_id).limit(1))[0]

    idempotence_key = str(uuid.uuid4())

    payment = yookassa.Payment.create({
        "amount": {
            "value": "49.0",
            "currency": "RUB"
        },
        "payment_method_data": {
            "type": "bank_card"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": f"https://discord.com/channels/{ctx.get_guild().id}/{d.channel_id}/{d.id}"
        },
        "description": "Заказ №1"
    }, idempotence_key)

    confirmation_url = payment.confirmation.confirmation_url

    await ctx.respond("ссылка на оплату " + confirmation_url)


def load(client):
    client.add_plugin(plugin)