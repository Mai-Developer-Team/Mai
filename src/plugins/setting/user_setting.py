import hikari 
import lightbulb
import miru

from config import setting
from utils import local, db

plugin = lightbulb.Plugin("user_setting", default_enabled_guilds=setting.guild_id)


class UserSettingModal(miru.Modal):
    bio = miru.TextInput(label="О себе", style=hikari.TextInputStyle.PARAGRAPH)

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

class UserSettingButton(miru.View):

    @miru.button(label = "О себе", style = hikari.ButtonStyle.SUCCESS)
    async def setting_bio(self, button: miru.Button, ctx: miru.ViewContext):
        modal = UserSettingModal(title="Написать биографию для /userinfo")
        await ctx.respond_with_modal(modal)


@plugin.command()
@lightbulb.command("user_setting", "Настройка профиля")
@lightbulb.implements(lightbulb.SlashCommand)
async def user_setting(ctx: lightbulb.Context) -> None:

    button = UserSettingButton()
    msg = await ctx.respond("test", components=button, flags=hikari.MessageFlag.EPHEMERAL)
    await button.start(msg)


def load(client):
    client.add_plugin(plugin)
