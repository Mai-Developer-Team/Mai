import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("TOKEN")

debug = False
version = "3.0.0.dev1"
prefix = "m"
devprefix = "m#"
color = 0x2f3136


plugins = [
    "plugins.ping",
    "plugins.eval"
]

