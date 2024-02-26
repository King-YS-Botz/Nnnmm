import pyrogram, os, asyncio

try: app_id = int(os.environ.get("app_id", None))
except Exception as app_id: print(f"⚠️ App ID Invalid {app_id}")
try: api_hash = os.environ.get("api_hash", None)
except Exception as api_id: print(f"⚠️ Api Hash Invalid {api_hash}")
try: bot_token = os.environ.get("bot_token", None)
except Exception as bot_token: print(f"⚠️ Bot Token Invalid {bot_token}")
try: custom_caption = os.environ.get("custom_caption", "`{file_name}`")
except Exception as custom_caption: print(f"⚠️ Custom Caption Invalid {custom_caption}")

AutoCaptionBot = pyrogram.Client(
   name="AutoCaptionBot", api_id=app_id, api_hash=api_hash, bot_token=bot_token)

start_message = """
<b>👋ʜᴇʟʟᴏ ʙʀᴏᴛʜᴇʀ/sɪsᴛᴇʀ (ᴇxᴄᴇᴘᴛ ᴏɴᴇ ᴍʏ 👸 ǫᴜᴇᴇɴ 😉) \n ᴍʏ ᴅᴇᴀʀ ғʀɪᴇɴᴅ{}</b>
<b>\n\nɪ ᴀᴍ ᴀɴ ᴀᴅᴠᴀᴄᴇ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ᴡɪᴛʜ ᴀᴅᴠᴀɴᴄᴇ ғᴏɴᴛ ғᴇᴀᴛᴜʀᴇ ᴀɴᴅ ᴍᴀɴʏ ᴍᴏʀᴇ</b>
<b>\nɴᴏᴡ ᴀᴛ ᴛʜᴀᴛ ᴛɪᴍᴇ ɪ ᴏɴʟʏ ᴡᴏʀᴋ ɪɴ ᴄʜᴀɴɴᴇʟ ʙᴜᴛ ɪᴛ ɢᴏᴛ ᴜᴘᴅᴀᴛᴇᴅ ᴀʟsᴏ</b>
<b>\nᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴅᴏɴᴛ ᴡᴏʀʀʏ ɪ ʜᴀᴠᴇ sᴏʟᴜᴛɪᴏɴ</b>
<b>\nI ɢɪᴠᴇ ᴄᴀᴘᴛɪᴏɴ ɪɴ ᴍᴏɴᴏ(`ʏs ʙᴏᴛᴢ`) sᴛʏʟᴇ ɴᴏᴡ ʙᴜᴛ \nɪ ᴄᴀɴ ᴀʟsᴏ ɢɪᴠᴇ ʏᴏᴜ ɪɴ ɪᴛᴀʟɪᴄ, ʙᴏʟᴅ, ᴀɴᴅ ʙᴏʟᴅ ɪᴛᴀʟɪᴄ ᴏɴ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴍʏ ɢᴏᴅ😀\n ᴘʀᴇss ᴏɴ ʜᴇʟᴘ ғᴏʀ ᴍᴏʀᴇ<\b>
<b>ᴀʟʟ ᴄᴏᴘʏʀɪɢʜᴛ ᴄʟᴀɪᴍᴇᴅ ʙʏ\n ʏs ʙᴏᴛᴢ™</b>"""

about_message = """
╔════❰ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼📃ᴍʏ ɴᴀᴍᴇ : {}
║┣⪼😎Cʀᴇᴀᴛᴏʀ : [𝖄𝕾_𝕭𝖔𝖙𝖟](https://t.me/Raadhe_Krishnn)
║┣⪼🧒ᴍʏ ʙᴇsᴛ ғʀɪᴇɴᴅ : <a href='tg://settings'>ᴛʜɪs ᴘᴇʀsᴏɴ</a>
║┣⪼📡Hᴏsᴛᴇᴅ ᴏɴ : Aɴʏ Wʜᴇʀᴇ
║┣⪼🗣️Lᴀɴɢᴜᴀɢᴇ : Pʏᴛʜᴏɴ𝟹 & Hᴛᴍʟ
║┣⪼📚Lɪʙʀᴀʀʏ : Pʏʀᴏɢʀᴀᴍ  
║┣⪼🗒️Vᴇʀsɪᴏɴ : 𝟗.𝟓.𝟎 [ᴍᴏsᴛ sᴛᴀʙʟᴇ]
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪
"""

source_message = """
<b>Oʏᴇ Dᴇᴠᴇʟᴏᴘᴇʀ, I ᴀᴍ ɴᴏᴛ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ Pʀᴏᴊᴇᴄᴛ.

ᴍʏ ᴘʀᴏɢʀᴀᴍɪɴɢ ɪs ʜɪᴅᴅᴇɴ ʙʏ ᴍʏ ɢᴏᴅ 

𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐂𝐫𝐞𝐚𝐭𝐞 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭 𝐏𝐚𝐢𝐝 𝐀𝐧𝐝 𝐖𝐚𝐧𝐭 𝐌𝐲 𝐇𝐢𝐝𝐝𝐞𝐧 𝐂𝐨𝐝𝐞 𝐓𝐡𝐞𝐧 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐓𝐨 𝐌𝐲 𝐆𝐨𝐝

ʙᴜʏ ᴄᴏᴅᴇ ғᴏʀ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ 

ᴄᴏɴᴛᴀᴄᴛ - <a href='https://t.me/YS_Contact_RoBot'>𝖄𝕾 𝕮𝖔𝖓𝖙𝖆𝖈𝖙</a></b>
"""

help_message = """ ᴛᴏ ᴀᴅᴅ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ғᴏʟʟᴏᴡs ᴛʜᴇ ɢɪʙᴇɴ sᴛᴇᴘ :-

sᴛᴇᴘ 𝟷:- ᴊᴏɪɴ ᴛʜᴇ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴛʜᴇ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ

sᴛᴇᴘ 𝟸:- sᴛᴇᴘ ᴛᴡᴏ ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ, ɪɴ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʀᴇɴᴀᴍᴇ ᴛʜᴇ ғɪʟᴇs.

ɴᴏᴡ ʏᴏᴜ ʀ ᴡᴏʀᴋ ɪs sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴏɴᴇ. 

ᴍʏ ᴄᴜʀʀᴇɴᴛ ᴄᴀᴘᴛɪᴏɴ ɪs ex is :- 

ʏᴏᴜʀ ғɪʟᴇ/ᴠɪᴅᴇᴏ

📁 Fɪʟᴇ Nᴀᴍᴇ » `Lucifer_2017_S02_E10_18_Part_1_720p_HEVC_HDRip_Dual_Audio_Hindi.mkv`

⚙ Sɪᴢᴇ » __984.95 ᴍʙ__ """

@AutoCaptionBot.on_message(pyrogram.filters.private & pyrogram.filters.command(["start"]))
def start_command(bot, update):
  update.reply(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBot.on_callback_query(pyrogram.filters.regex("start"))
def strat_callback(bot, update):
  update.message.edit(start_message.format(update.from_user.mention), reply_markup=start_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBot.on_callback_query(pyrogram.filters.regex("about"))
def about_callback(bot, update): 
  bot = bot.get_me()
  update.message.edit(about_message.format(version=pyrogram.__version__, username=bot.mention), reply_markup=about_buttons(bot, update.message), parse_mode=pyrogram.enums.ParseMode.HTML, disable_web_page_preview=True)

@AutoCaptionBot.on_message(pyrogram.filters.channel)
def edit_caption(bot, update: pyrogram.types.Message):
  if os.environ.get("custom_caption"):
      motech, _ = get_file_details(update)
      converted_file_size = get_size(motech.file_size)
      try:
          try: update.edit(custom_caption.format(file_name=motech.file_name, file_size=converted_file_size))
          except pyrogram.errors.FloodWait as FloodWait:
              asyncio.sleep(FloodWait.value)
              update.edit(custom_caption.format(mote, file_name=motech.file_name, file_size=motech.file_size))
      except pyrogram.errors.MessageNotModified: pass 
  else:
      return
  
#size convertion
def get_size(size):
    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])
    
def get_file_details(update: pyrogram.types.Message):
  if update.media:
    for message_type in (
        "photo",
        "animation",
        "audio",
        "document",
        "video",
        "video_note",
        "voice",
        # "contact",
        # "dice",
        # "poll",
        # "location",
        # "venue",
        "sticker"
    ):
        obj = getattr(update, message_type)
        if obj:
            return obj, obj.file_id

def start_buttons(bot, update):
  bot = bot.get_me()
  buttons = [[
   pyrogram.types.InlineKeyboardButton("🌀 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ 🌀", url=f"http://t.me/{bot.username}?startchannel=true")
   ],[
   pyrogram.types.InlineKeyboardButton("💠ᴀʙᴏᴜᴛ💠", callback_data="about")
   ],[      

pyrogram.types.InlineKeyboardButton("💠ᴀʙᴏᴜᴛ💠", callback_data="help")
   ],[
   pyrogram.types.InlineKeyboardButton("📢ᴜᴘᴅᴀᴛᴇ📢", url="t.me/YS_Botz_Update")
   ],[pyrogram.types.InlineKeyboardButton("💞sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ💕", url="https://t.me/YS_BOT_DISSCUSION")
   ]]
  return pyrogram.types.InlineKeyboardMarkup(buttons)

def about_buttons(bot, update):
   bot = bot.get_me()
   buttons = [
    [
      pyrogram.types.InlineKeyboardButton("❇️ʜᴏᴍᴇ ❇", callback_data="start")
    ],
    [
      pyrogram.types.InlineKeyboardButton("♻️sᴏᴜʀᴄᴇ♻", callback_data="source"), 
      pyrogram.types.InlineKeyboardButton("♨️ ᴄʟᴏsᴇ ♨", callback_data="close")
    ]
  ]
  return pyrogram.types.InlineKeyboardMarkup(buttons) 

def source_buttons(bot, update):
   bot = bot.get_me()
   buttons = [
    [
      pyrogram.types.InlineKeyboardButton("❇️ʜᴏᴍᴇ ❇", callback_data="start")
    ],
    [
      pyrogram.types.InlineKeyboardButton("🔅 ᴀʙᴏᴜᴛ 🔅", callback_data="about"), 
      pyrogram.types.InlineKeyboardButton("♨️ ᴄʟᴏsᴇ ♨", callback_data="close")
    ],[
      pyrogram.types.InlineKeyboardButton("Oᴡɴᴇʀ♂️", url="t.me/Raadhe_Krishnn")
    ]
  ]
  return pyrogram.types.InlineKeyboardMarkup(buttons) 
  
print("Telegram AutoCaption Bot mode by YS bot developerr")
print("Bot Created By YS Botz")

AutoCaptionBot.run()
