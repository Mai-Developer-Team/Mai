import melisa 

from config import setting

if setting.debug == False:
    info = "INFO"
    prefix = setting.prefix 
    token = setting.token
else:
    info = "DEBUG"
    prefix = setting.devprefix
    token = setting.token #yes


client = melisa.Client(
    token,
    intents = [
        melisa.Intents.GUILD_MEMBERS,
        melisa.Intents.GUILD_MESSAGES
    ],
    activity = melisa.presence.Activity(setting.version, type = melisa.ActivityType.COMPETING),
    logs = info
)


client.run_autosharded()
