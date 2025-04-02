import re
from os import environ
from Script import script

# Regex pattern for validating IDs
id_pattern = re.compile(r'^.\d+$')

# -----------------------------------
# Bot Information
# -----------------------------------
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', '25776734'))
API_HASH = environ.get('API_HASH', '9bb0c527d53d497506baf1bd17d7426c')
BOT_TOKEN = environ.get('BOT_TOKEN', '6572948658:AAG0z6ymFzFrLUdwSjsa7VPysjJ05I4leZw')

# Start Message Pictures (space-separated URLs)
PICS = environ.get('PICS', 'https://graph.org/file/c35b01ee1bfdb1c78c871-33391b6d1aa98667c8.png').split()
SUBSCRIPTION = environ.get('SUBSCRIPTION', 'https://graph.org/file/c35b01ee1bfdb1c78c871-33391b6d1aa98667c8.png')
PAYPICS = environ.get('PAYPICS', 'https://graph.org/file/c35b01ee1bfdb1c78c871-33391b6d1aa98667c8.png').split()

# -----------------------------------
# Admins & Authorized Users
# -----------------------------------
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7798091025 8064881390').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '7798091025 8064881390').split()]
AUTH_USERS = auth_users + ADMINS if auth_users else []

# -----------------------------------
# Channels Configuration
# -----------------------------------
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002605262806'))  # Log channel for user activity
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002487701113').split()]  # File storage channels
FILE_STORE_CHANNEL = [int(ch) for ch in environ.get('FILE_STORE_CHANNEL', '-1002605262806').split()]  # Batch command file store
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for ch in environ.get('DELETE_CHANNELS', '-1002326829401').split()]  # Delete index files
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))  # Index request channel

# Force Subscribe (Auth Channel)
auth_channel = environ.get('AUTH_CHANNEL', '-1002313843759')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
REQUEST_TO_JOIN_MODE = bool(environ.get('REQUEST_TO_JOIN_MODE', False))
TRY_AGAIN_BTN = bool(environ.get('TRY_AGAIN_BTN', True))

# Request & Support Channels
reqst_channel = environ.get('REQST_CHANNEL_ID', '')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002036256358')
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

# -----------------------------------
# MongoDB Configuration
# -----------------------------------
DATABASE_URI = environ.get('DATABASE_URI', 'mongodb+srv://KRISTEENNEW1:KRISTEEEEN1@cluster0.nz4zp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
DATABASE_NAME = environ.get('DATABASE_NAME', 'techvjclonefilterbot')
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'vjcollection')

MULTIPLE_DATABASE = bool(environ.get('MULTIPLE_DATABASE', True))
if MULTIPLE_DATABASE:
    O_DB_URI = environ.get('O_DB_URI', 'mongodb+srv://KRISTEENQ2:KRISTEEEN2@cluster0.7jqbi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    F_DB_URI = environ.get('F_DB_URI', 'mongodb+srv://KRISTEENQ3:KRISTEEEEN@cluster0.luljb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    S_DB_URI = environ.get('S_DB_URI', 'mongodb+srv://KRISTEENQ4:KRISTEEEEEN@cluster0.iqxzy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    USER_DB_URI = DATABASE_URI
    OTHER_DB_URI = O_DB_URI
    FILE_DB_URI = F_DB_URI
    SEC_FILE_DB_URI = S_DB_URI
else:
    USER_DB_URI = DATABASE_URI
    OTHER_DB_URI = DATABASE_URI
    FILE_DB_URI = DATABASE_URI
    SEC_FILE_DB_URI = DATABASE_URI

# -----------------------------------
# Premium & Referral Settings
# -----------------------------------
PREMIUM_AND_REFERAL_MODE = bool(environ.get('PREMIUM_AND_REFERAL_MODE', True))
if PREMIUM_AND_REFERAL_MODE:
    REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '10'))
    REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1month')
    PAYMENT_QR = environ.get('PAYMENT_QR', 'https://graph.org/file/c35b01ee1bfdb1c78c871-33391b6d1aa98667c8.png')
    PAYMENT_TEXT = environ.get('PAYMENT_TEXT', '<b>- ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs - \n\n- 15ʀs - 1 ᴡᴇᴇᴋ\n- 35ʀs - 1 ᴍᴏɴᴛʜs\n- 100ʀs - 3 ᴍᴏɴᴛʜs\n- 180ʀs - 6 ᴍᴏɴᴛʜs\n\n🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🎁\n\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋ\n○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs\n○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ\n○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ\n○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs\n○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs\n○ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ\n○ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ\n\n✨ ᴜᴘɪ ɪᴅ - <code>---</code>\n\nᴄʟɪᴄᴋ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ /myplan\n\n💢 ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ\n\n‼️ ᴀғᴛᴇʀ sᴇɴᴅɪɴɢ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴜs sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ</b>')

# -----------------------------------
# Clone Mode Settings
# -----------------------------------
CLONE_MODE = bool(environ.get('CLONE_MODE', False))
CLONE_DATABASE_URI = environ.get('CLONE_DATABASE_URI', '')
PUBLIC_FILE_CHANNEL = environ.get('PUBLIC_FILE_CHANNEL', 'Dev_Clone_Test')

# -----------------------------------
# Links
# -----------------------------------
GRP_LNK = environ.get('GRP_LNK', 'https://telegram.me/+LGFFsf2VvJszMTc1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://telegram.me/mihir_ax')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Suport_Dev77_xD')
OWNER_LNK = environ.get('OWNER_LNK', 'https://telegram.me/mihir_ax')

# -----------------------------------
# Feature Flags
# -----------------------------------
AI_SPELL_CHECK = bool(environ.get('AI_SPELL_CHECK', True))
PM_SEARCH = bool(environ.get('PM_SEARCH', True))
BUTTON_MODE = bool(environ.get('BUTTON_MODE', False))
MAX_BTN = bool(environ.get('MAX_BTN', True))
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', False))
IMDB = bool(environ.get('IMDB', False))
AUTO_FFILTER = bool(environ.get('AUTO_FFILTER', True))
AUTO_DELETE = bool(environ.get('AUTO_DELETE', True))
LONG_IMDB_DESCRIPTION = bool(environ.get('LONG_IMDB_DESCRIPTION', False))
SPELL_CHECK_REPLY = bool(environ.get('SPELL_CHECK_REPLY', True))
MELCOW_NEW_USERS = bool(environ.get('MELCOW_NEW_USERS', False))
PROTECT_CONTENT = bool(environ.get('PROTECT_CONTENT', False))
PUBLIC_FILE_STORE = bool(environ.get('PUBLIC_FILE_STORE', True))
NO_RESULTS_MSG = bool(environ.get('NO_RESULTS_MSG', False))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

# -----------------------------------
# Token Verification Settings
# -----------------------------------
VERIFY = bool(environ.get('VERIFY', True))
VERIFY_SHORTLINK_URL = environ.get('VERIFY_SHORTLINK_URL', 'shortxlinks.com')
VERIFY_SHORTLINK_API = environ.get('VERIFY_SHORTLINK_API', '37191a6d435c63b283f8aa3e53cdbaedf62c0a1d')
VERIFY_TUTORIAL = environ.get('VERIFY_TUTORIAL', 'https://t.me/HowToVerify_xD/27')
MULTIPLE_SHORTNER = False
VERIFY_SHORTLINK_URL_2 = 'vipcpm.in'
VERIFY_SHORTLINK_API_2 = '9c12045dc1cad72346928e2de68ae5638acb25d2'

VERIFY_SECOND_SHORTNER = bool(environ.get('VERIFY_SECOND_SHORTNER', False))
VERIFY_SND_SHORTLINK_URL = environ.get('VERIFY_SND_SHORTLINK_URL', '')
VERIFY_SND_SHORTLINK_API = environ.get('VERIFY_SND_SHORTLINK_API', '')

# -----------------------------------
# Shortlink Settings
# -----------------------------------
SHORTLINK_MODE = bool(environ.get('SHORTLINK_MODE', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')
TUTORIAL = environ.get('TUTORIAL', 'https://telegram.me/')

# -----------------------------------
# Miscellaneous Settings
# -----------------------------------
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
MAX_B_TN = environ.get('MAX_B_TN', '5'))
PORT = environ.get('PORT', '8080')
MSG_ALRT = environ.get('MSG_ALRT', '🔥 ᴍᴀɪ ᴋᴀʙʜɪ ᴊʜᴜᴋᴇɢᴀ ɴᴀʜɪ 🔥')
CUSTOM_FILE_CAPTION = environ.get('CUSTOM_FILE_CAPTION', f'{script.CAPTION}')
BATCH_FILE_CAPTION = environ.get('BATCH_FILE_CAPTION', CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
MAX_LIST_ELM = environ.get('MAX_LIST_ELM', None)

# -----------------------------------
# Filter Options
# -----------------------------------
LANGUAGES = ['malayalam', 'mal', 'tamil', 'tam', 'english', 'eng', 'hindi', 'hin', 'telugu', 'tel', 'kannada', 'kan']
SEASONS = [f'season {i}' for i in range(1, 11)]
EPISODES = [f'E{i:02d}' for i in range(1, 41)]
QUALITIES = ['360p', '480p', '720p', '1080p', '1440p', '2160p']
YEARS = [str(year) for year in range(1900, 2026)]

# -----------------------------------
# Streaming & Download Settings
# -----------------------------------
STREAM_MODE = bool(environ.get('STREAM_MODE', True))
if STREAM_MODE:
    MULTI_CLIENT = False
    SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
    PING_INTERVAL = int(environ.get('PING_INTERVAL', '1200'))
    ON_HEROKU = 'DYNO' in environ
    URL = environ.get('URL', ' ')

# -----------------------------------
# Additional Features
# -----------------------------------
RENAME_MODE = bool(environ.get('RENAME_MODE', False))
AUTO_APPROVE_MODE = bool(environ.get('AUTO_APPROVE_MODE', False))
REACTIONS = ['😱', '😈', '🎉', '⚡️', '😎', '🏆', '🔥', '👻']
