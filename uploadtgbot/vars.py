from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Vars:
    CACHE_TIME = int(config("CACHE_TIME", default=5))
    DOWN_PATH = f"{getcwd()}/uploadtgbot/downloads"
    BOT_TOKEN = config("BOT_TOKEN", "5945346287:AAE3gmyeGs-oK2UxcgbTDWjr48an4iv-oSY")
    APP_ID = int(config("API_ID", 22681384))
    API_HASH = config("API_HASH", "14ae45755537c723aab0564a80d723a9")
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", -1001860694129))
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/ !").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="DivideProjectsDiscussion")
    AUTH_CHANNEL = config("AUTH_CHANNEL", -1001523739263)
    OWNER_ID = int(config("OWNER_ID", 5468192421))
    DB_URI = config("DB_URI", "mongodb+srv://aio:aio@aio.5z4gxok.mongodb.net/?retryWrites=true&w=majority")
    CAPTION = config("CAPTION", default="By @DivideProjects")
    VERSION = config("VERSION", default="v1.1 - Stable")
    BOT_USERNAME = config("BOT_USERNAME", "Uploaderv3Bot")
    WORKERS = config("WORKERS", default=8)
    JOIN_CHECK = config("JOIN_CHECK", default=None, cast=config.boolean)
