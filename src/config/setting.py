import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("TOKEN")
debug = False
version = "3.0.0.dev1"
prefix = "m"
devprefix = "m#"


plugins = [
    "plugins.ping"
]

