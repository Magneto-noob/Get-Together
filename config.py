# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "15523035"))
API_HASH = getenv("API_HASH", "33a37e968712427c2e7971cb03f341b3")
BOT_TOKEN = getenv("BOT_TOKEN", "6326888965:AAH95RvB9G9tjK0G-exAR2dCVeJEwcBrRIs")
OWNER_ID = int(getenv("OWNER_ID", "910674886"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://TGBot:Save@koyeb.vvt99ro.mongodb.net/?retryWrites=true&w=majority&appName=Koyeb")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002193752822"))
FORCESUB = getenv("FORCESUB", "GetAnyContent")
