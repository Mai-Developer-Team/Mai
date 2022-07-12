import lightbulb
import hikari

from config import setting
from utils import local

class CustomHelp(lightbulb.BaseHelpCommand):

    async def send_bot_help(self, context):
        guildId = context.get_guild().id
        prefix = setting.prefix

        emb = hikari.Embed(
            color = setting.color
        )
        emb.add_field(
            name = local.help_category_info(guildId),
            value = f"`{prefix}stats`, `{prefix}help`",
            inline=False        
        )
        emb.set_thumbnail("https://cdn.discordapp.com/attachments/996413253456511096/996413330791092285/bd3995a99af0fc2a7a98babb9ca3311e.webp")
        emb.set_footer(text = f'Версия Маи {setting.version}')

        await context.respond(embed=emb)
    
    async def send_plugin_help(self, context, plugin):
        ...

    async def send_command_help(self, context, command):
        guildId = context.get_guild().id

        emb = hikari.Embed(
            color = setting.color
        )

        emb.add_field(
            name = local.help_name_command(guildId),
            value = command.name,
            inline = False
        )
        emb.add_field(
            name = local.help_description_command(guildId),
            value = command.description,
            inline = False
        )

        emb.set_thumbnail("https://cdn.discordapp.com/attachments/996413253456511096/996413330791092285/bd3995a99af0fc2a7a98babb9ca3311e.webp")
        emb.set_footer(text = f'Версия Маи {setting.version}')
        
        await context.respond(embed=emb)

    async def send_group_help(self, context, group):
        ...

    async def object_not_found(self, context, obj):
        guildId = context.get_guild().id

        emb = hikari.Embed(
            description = local.help_err(guildId, obj),
            color = setting.color
        )

        emb.set_thumbnail("https://cdn.discordapp.com/attachments/996413253456511096/996413330791092285/bd3995a99af0fc2a7a98babb9ca3311e.webp")
        emb.set_footer(text = f'Версия Маи {setting.version}')

        await context.respond(embed=emb)


def load(client):
    client.d.old_help = client.help_command
    client.help_command = CustomHelp(client)