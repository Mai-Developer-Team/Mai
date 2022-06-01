import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("TOKEN")
debug = True
version = "3.0.0dev"
prefix = "m"
devprefix = "m#"