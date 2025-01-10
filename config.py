import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 27758016
API_HASH = "8d34cfffe27ab461eabbf0091b1a27df"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "8007775153:AAFGtvkherSCW7MOgmg9bmF9tY2DmdSmTMQ"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://tennyson2002:tennyson2002@cluster0.h1vm3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60000))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002250226716"))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = 7224419362

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Marwin2002/AmritaM",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/The_Architect04")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Team_Supporty")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/Privacy-Policy-for-AviaxMusic-08-14")


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 805))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQEksaEAmh8NemJ-8rt-7LsJvmnJzRkH8A5VB9DsUQYuY7NvihFNzrYMIfneF2s-eB6TY9BFmpoICga-pZBcipLXAiQ1FSsJxSLpGt9n-sisrJ8weWdHNfr193ld8dc4BmKzgueN0fp_6x2qwjMZ-yn9MAds-pIlN5bQm3Cl-rZ94W-SbMQSjitOyHiO05ki8ybZ_gobmyXuZ3Op5XgIEvEw9Y0mcHCStzEMu5r8PqEH0lW-Jf3nzPZ-HriqgXcwUysAMGC99M4JhM43LmCtrjeoFuSLIQG3kX4T0z5m6chDLjwO0gN6y63HLlBDiMfYulPWydLZF2zVWbMgACYHFkYoCHJIRwAAAAHMEry6AA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/rEw.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/r2A.jpg"
)
PLAYLIST_IMG_URL = "https://envs.sh/rw8.jpg"
STATS_IMG_URL = "https://envs.sh/r2j.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
TELEGRAM_VIDEO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
