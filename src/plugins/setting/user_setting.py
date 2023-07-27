import hikari 
import lightbulb
import miru

import datetime

from config import setting
from utils import db

plugin = lightbulb.Plugin("user_setting")


class UserSettingModal(miru.Modal):
    bio = miru.TextInput(label="О себе", style=hikari.TextInputStyle.PARAGRAPH, max_length=32)

    async def callback(self, ctx: miru.ModalContext) -> None:
        if not db.user(ctx.author.id):
            await ctx.respond(f"Вы еще ни разу не прописывали `/userinfo`", flags=hikari.MessageFlag.EPHEMERAL)
        else:
            if db.user(ctx.author.id)["bio"] == None:
                await ctx.respond(f"Ваша новая биография: **{self.bio.value}**", flags=hikari.MessageFlag.EPHEMERAL)
                db.db.user.update_one(
                { "id": ctx.author.id }, 
                { 
                    "$set": {
                        "bio": self.bio.value
                        }
                }
                
            )
            else:
                await ctx.respond(f"Ваша обновленная биография: **{self.bio.value}**", flags=hikari.MessageFlag.EPHEMERAL)
                db.db.user.update_one(
                { "id": ctx.author.id }, 
                { 
                    "$set": {
                        "bio": self.bio.value
                        }
                }
                )

class PromoModal(miru.Modal):
    namePromo = miru.TextInput(label="Введите промокод", style=hikari.TextInputStyle.PARAGRAPH, max_length=32)

    async def callback(self, ctx: miru.ModalContext) -> None:
        p = db.promo({"name": self.namePromo.value})


class UserSettingButton(miru.View):

    @miru.button(label = "О себе", style = hikari.ButtonStyle.SUCCESS)
    async def setting_bio(self, button: miru.Button, ctx: miru.ViewContext):
        modal = UserSettingModal(title="Написать биографию для /userinfo")
        await ctx.respond_with_modal(modal)
    
    @miru.button(label = "Промокод", style = hikari.ButtonStyle.SUCCESS, disabled=True)
    async def setting_promo(self, button: miru.Button, ctx: miru.ViewContext):
        modal = PromoModal(title="Воспользоваться промокодом")
        await ctx.respond_with_modal(modal)
    
    @miru.button(label = "Оповещение", style = hikari.ButtonStyle.SECONDARY)
    async def setting_nothing(self, button: miru.Button, ctx: miru.ViewContext):
        class UserSettingNothing(miru.View):
            if db.user(ctx.author.id)["nothing"] == False:
                @miru.button(label = "Включить", style = hikari.ButtonStyle.DANGER)
                async def enable_nothing(self, button: miru.Button, ctx: miru.ViewContext):
                    db.db.user.update_one(
                        { "id": ctx.author.id },
                        {
                            "$set": {
                                "nothing": True
                            }
                        }
                        )
                    await ctx.respond("**Оповещение включены**", flags=hikari.MessageFlag.EPHEMERAL)
            if db.user(ctx.author.id)["nothing"] == True:
                @miru.button(label = "Выключить", style = hikari.ButtonStyle.SUCCESS)
                async def disable_nothing(self, button: miru.Button, ctx: miru.ViewContext):
                    db.db.user.update_one(
                        { "id": ctx.author.id },
                        {
                            "$set": {
                                "nothing": False
                            }
                        }
                        )
                    await ctx.respond("**Оповещение выключены**", flags=hikari.MessageFlag.EPHEMERAL)

        emb = hikari.Embed(
            title="Настройки оповещения",
            description="Оповещения нужны для **получения буста, об заходе человека из черного списка и успешном апе на BotiCord**",
            color=setting.color
        )
        emb.set_footer(
            text = "Данная команда является только пользовательская и переводится не будет!"
        )

        button = UserSettingNothing()
        msg = await ctx.respond(embed=emb, components=button, flags=hikari.MessageFlag.EPHEMERAL)
        await button.start(msg)



@plugin.command()
@lightbulb.command("user_setting", "Настройка профиля")
@lightbulb.implements(lightbulb.SlashCommand)
async def user_setting(ctx: lightbulb.Context) -> None:

    emb = hikari.Embed(
        title="Настройки профиля в /userinfo и /profile",
        description="Здесь можете **поставить/поменять** биографию, **включить/выключить** оповещение от бота и воспользоваться **промокодом**",
        color=setting.color
    )
    emb.set_footer(
        text = "Данная команда является только пользовательская и переводится не будет!"
        )

    button = UserSettingButton()
    msg = await ctx.respond(embed=emb, components=button, flags=hikari.MessageFlag.EPHEMERAL)
    await button.start(msg)


def load(client):
    client.add_plugin(plugin)
