class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "25764824"
    API_HASH = "637550d4edbe66606d184abbe961d0f5"

    CASH_API_KEY = "XEC8UHG583MJ62SU"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://ohpofzjg:Js2CV1rrbOEtrz6L5D7asL3MgqObXaLq@queenie.db.elephantsql.com/ohpofzjg"  # A sql database url from elephantsql.com

    EVENT_LOGS = "-1001645899463"  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Arunkumar:arunhald@cluster0.n5oxsxc.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "Tamilchat_TGK"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5698992270:AAFlxK8tnbM2VvxQ8wK4AkB_oyh-BtSys5E"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID = "868753606"  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [868753606 6249522771 5259528159 6211613888]  # User id of sudo users
    DEV_USERS = [868753606 6249522771 5259528159 6211613888]  # User id of dev users
    DEMONS = [868753606]  # User id of support users
    TIGERS = [868753606]  # User id of tiger users
    WOLVES = [868753606]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
