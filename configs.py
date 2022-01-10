# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
**Tʜɪs ɪs Pᴇʀᴍᴀɴᴇɴᴛ Fɪʟᴇs Sᴛᴏʀᴇ Bᴏᴛ!**
**Sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ I ᴡɪʟʟ sᴀᴠᴇ ɪᴛ ɪɴ ᴍʏ Dᴀᴛᴀʙᴀsᴇ.**

🤖 **Mʏ Nᴀᴍᴇ: CTP File Store**

🧑🏻‍💻 **ᴅᴇᴠᴇʟᴏᴘᴇʀ: @SF_Captain**

👥 **Gʀᴏᴜᴘ: @CTP_Requests**

📢 **Mᴏᴠɪᴇs: @CTP_Official**
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **ᴅᴇᴠᴇʟᴏᴘᴇʀ: @SF_Captain** 😏

**Iғ ʜᴀᴠᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ʀᴇɢᴀʀᴅɪɴɢ ᴜsɪɴɢ ᴍᴇ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ Mʏ Bᴏss - @Sf_Captain**

**Aʟsᴏ ʀᴇᴍᴇᴍʙᴇʀ ᴛʜᴀᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴡɪʟʟ Dᴇʟᴇᴛᴇ Aᴅᴜʟᴛ Cᴏɴᴛᴇɴᴛs ғʀᴏᴍ Dᴀᴛᴀʙᴀsᴇ. Sᴏ ʙᴇᴛᴛᴇʀ ᴅᴏɴ'ᴛ Sᴛᴏʀᴇ Tʜᴏsᴇ Kɪɴᴅ ᴏғ Tʜɪɴɢs**
"""
	HOME_TEXT = """
**Hi**, [{}](tg://user?id={})\n\n**I'ᴍ ғɪʟᴇs Sᴛᴏʀᴇ ʙᴏᴛ 🏪**

**Hᴇʀᴇ ʏᴏᴜ sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇs ᴛʜᴇɴ I ᴡɪʟʟ ɢɪᴠᴇ ᴛʜᴇ ᴘᴇʀᴍᴀɴᴇɴᴛ Sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ** . 😁.
"""
