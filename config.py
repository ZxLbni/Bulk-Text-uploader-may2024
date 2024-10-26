import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7625505683:AAEzjTsK1mslDxJLDM_XRSzuMUtT2Ir2dLc")
    API_ID = int(os.environ.get("API_ID", "22419004"))
    API_HASH = os.environ.get("API_HASH", "34982b52c4a83c2af3ce8f4fe12fe4e1")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6742022802")
