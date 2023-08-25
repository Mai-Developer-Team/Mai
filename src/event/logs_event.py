import hikari
import lightbulb


from config import setting
from utils import local, db

plugin = lightbulb.Plugin("logs_event")


@plugin.listener(hikari.MemberCreateEvent)
async def member_join(event: hikari.MemberCreateEvent):
    logs_channel = await event.app.rest.fetch_channel(1122951720444624980)
    user = event.user
    guild = event.get_guild()

    if guild.id == event.member.guild_id:
        if user.is_bot == False:
            embed = (
                hikari.Embed(
                    title = "LOGS | Новый пользователь",
                    color = setting.color
                )
                .add_field(name="Пользователь", value=f"{user.username} | {user.mention}")
                .add_field(name="Дата регистрации", value = f"<t:{round(user.created_at.timestamp())}:D>")
                .set_thumbnail(user.avatar_url)
            )
        else:
            embed = (
                hikari.Embed(
                    title="LOGS | Новый бот",
                    color=setting.color
                )
                .add_field(name="Бот", value=f"{user.username} | {user.mention}")
                .add_field(name="Дата регистрации", value=f"<t:{round(user.created_at.timestamp())}:D>")
                .set_thumbnail(user.avatar_url)
            )
        await logs_channel.send(embed = embed)



@plugin.listener(hikari.MemberDeleteEvent)
async def member_leave(event: hikari.MemberDeleteEvent):
    logs_channel = await event.app.rest.fetch_channel(1122951720444624980)
    user = event.user
    guild = event.get_guild()

    if guild.id == event.old_member.guild_id:
        if user.is_bot == False:
            embed = (
                hikari.Embed(
                    title="LOGS | Пользователь вышел со сервера",
                    color=setting.color
                )
                .add_field(name="Пользователь", value=f"{user.username} | {user.mention}")
                .add_field(name="Дата регистрации", value=f"<t:{round(user.created_at.timestamp())}:D>")
                .add_field(name="Зашел на сервер", value=f"<t:{round(event.old_member.joined_at.timestamp())}:D>")
                .set_thumbnail(user.avatar_url)
            )
        else:
            embed = (
                hikari.Embed(
                    title="LOGS | Отключение бота от сервера",
                    color=setting.color
                )
                .add_field(name="Бот", value=f"{user.username} | {user.mention}")
                .add_field(name="Дата регистрации", value=f"<t:{round(user.created_at.timestamp())}:D>")
                .add_field(name="Добавление на сервер", value=f"<t:{round(event.old_member.joined_at.timestamp())}:D>")
                .set_thumbnail(user.avatar_url)
            )
        await logs_channel.send(embed=embed)


@plugin.listener(hikari.VoiceStateUpdateEvent)
async def voice_join(event: hikari.VoiceStateUpdateEvent):
    logs_channel = await event.app.rest.fetch_channel(1122951720444624980)
    user = event.state.user_id
    guild = event.state.guild_id
    member = await event.app.rest.fetch_user(user)

    if guild == 992117772521836674:

        if event.old_state == None:
            emb = (
                hikari.Embed(
                    title="LOGS | Голосовой чат",
                    description="Пользователь зашел в голосовой чат",
                    color = setting.color
                )
                .add_field(name="Пользователь", value=f"{member.username} | {member.mention}")
                .add_field(name="Голосовой канал", value=f"<#{event.state.channel_id}>")
                .set_thumbnail(member.avatar_url)
            )
        else:
            emb = (
                hikari.Embed(
                    title="LOGS | Голосовой чат",
                    description="Пользователь вышел из голосового чата",
                    color = setting.color
                )
                .add_field(name="Пользователь", value=f"{member.username} | {member.mention}")
                .add_field(name="Голосовой канал", value=f"<#{event.old_state.channel_id}>")
                .set_thumbnail(member.avatar_url)
            )

        await logs_channel.send(embed = emb)


@plugin.listener(hikari.InviteCreateEvent)
async def invite_create(event: hikari.InviteCreateEvent):
    logs_channel = await event.app.rest.fetch_channel(1122951720444624980)
    invite = event.invite

    if invite.expires_at != None: t = f"<t:{round(invite.expires_at.timestamp())}:R>"
    else: t = "∞"

    if invite.max_uses != None: u = invite.max_uses
    else: u = "Без ограничений"

    emb = (
        hikari.Embed(
            title="LOGS | Создан новое приглашение",
            color=setting.color
        )
        .add_field(name="Приглашение", value=f"https://discord.gg/{invite.code}")
        .add_field(name="Канал", value=f"<#{invite.channel_id}>")
        .add_field(name="Максимальное использование", value=u)
        .add_field(name="Время использования", value=t)
    )

    await logs_channel.send(embed = emb)


@plugin.listener(hikari.InviteDeleteEvent)
async def invite_delete(event: hikari.InviteDeleteEvent):
    logs_channel = await event.app.rest.fetch_channel(1122951720444624980)
    invite = event.old_invite

    if invite.expires_at != None:
        t = f"<t:{round(invite.expires_at.timestamp())}:R>"
    else:
        t = "∞"

    if invite.max_uses != None:
        u = invite.max_uses
    else:
        u = "Без ограничений"

    if invite.max_uses != None: q = invite.max_uses
    else: q = "Не разу"

    emb = (
        hikari.Embed(
            title="LOGS | Удалено приглашение",
            color=setting.color
        )
        .add_field(name="Приглашение", value=f"https://discord.gg/{invite.code}")
        .add_field(name="Канал", value=f"<#{invite.channel_id}>")
        .add_field(name="Максимальное использование", value=u)
        .add_field(name="Воспользовалось", value=q)
        .add_field(name="Время использования", value=t)
    )

    await logs_channel.send(embed=emb)


def load(client):
    client.add_plugin(plugin)
