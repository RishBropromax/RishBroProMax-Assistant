import os
import pyrogram
from config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

HELP_TEXT = f"""
Hey there... π

**πΈ I have some fun and useful tools. π»
So you can get a help about them. π**

  Click " /help "

||π Thank you for use my bot
Stay with me forever... β€οΈβπ₯||

**[Rishmika Sandanu](https://t.me/{Config.C_CHANNEL})**

"""

HELP_TEXT2 = f"""
Hey there... βοΈ

**πΈ I have some fun and useful tools. π»
So you can get a help about them. π**

||π Thank you for use my bot
Stay with me forever... β€οΈβπ₯||

**[Rishmika Sandanu](https://t.me/{Config.C_CHANNEL})**

"""
CLOSE_BUTTONS = [
	[
	InlineKeyboardButton('Closing..', callback_data='stats_callback'),
	],
]

CLOSE_TEXT = """ποΈοΈ Closing... π«"""

SONG_TEXT = """

**π§ Help For Song Download π§**

**Available Commands**

β₯ `/song {song name}` - Download a song simply.
β₯ `/song {youtube link}` - Download song using youtube link.

"""
LOGO_TEXT = """

**π Help For Logo Make π**

**Available Commands**

β₯ `/logo {text}`  - Create Simple Random Logos
β₯ `/mlogo {text}` - Write Something
β₯ `/xlogo {text}` - Create SriLankan Mask Logo

"""
QUOTE_TEXT = """
**π¬ Help for Quote π¬**

**Available Commands**

β₯ `/q` - Reply to a message to make it quote.

"""
URL_TEXT = """

**π§ Help for Link Shorten. π§**

**Available Commands**

β₯ `/url {Link}` - Link Shorten

"""
COVID_TEXT = """
**π§° Help for Covid π§°**

**Available Commands**

β₯ `/covid` - Get the Covid status of Sri Lanka π±π°


"""
HACK_TEXT = """

**πΈ Help for Hack πΈ**

**Available Commands**

β₯ `/hack`

"""

HELP_BUTTONS = [
	[
	InlineKeyboardButton("πUrlπ", callback_data='url'),
	],
	[
	InlineKeyboardButton("π₯Logoπ₯", callback_data='logo'),
	],
	[
	InlineKeyboardButton("π΅Songπ΅", callback_data='song'),
	],
	[
	InlineKeyboardButton("π§¬Covidπ§¬", callback_data='covid'),
	],
	[
	InlineKeyboardButton("πΊQuoteπΊ", callback_data='quote'),
	],
	[
	InlineKeyboardButton("βοΈSMS-BomberβοΈ", callback_data='otpbomber'),
	],
	[
	InlineKeyboardButton("π Hackπ ", callback_data='hack'),
	],
	[
	InlineKeyboardButton(text='Close π', callback_data='close'),
	],
]

SMS_TEXT = """

**π« Help for SMS-Bomber π«**

**Available Commands**

β₯ `/otpbomber {phone number}`

"""

START_MESSAGE_BUTTONS = [
	[
	InlineKeyboardButton('βοΈββββββStatsββββββββοΈ', callback_data='stats_callback'),
	],
	[
	InlineKeyboardButton('βοΈ CHANNEL βοΈ', url=f'https://t.me/{Config.CHANNEL}'),
	InlineKeyboardButton('π Discussion π', url=f'https://t.me/{Config.GROUP}'),
	],
	[
	InlineKeyboardButton(text='πΊ Help πΊ', callback_data='helpmenu'),
	],
	[
	InlineKeyboardButton(text='Close π', callback_data='close'),
	],
	[
	InlineKeyboardButton(text='β Add Me to Your Group β', url=f'http://t.me/{Config.BOT_USERNAME}?startgroup=true'),
	],
]

BACK_BUTTONS = [
	[
	InlineKeyboardButton('π Back', callback_data="Back"),
	],
]

HELP_BACK_BUTTONS = [
	[
	InlineKeyboardButton('π Back', callback_data="helpback"),
	],
]

FTEXT = f" **π«Access Deniedπ«** \n \nYou Must Join Our Channel To Use Me. So, Please Join it & Try Again. βοΈ"

CAPTION_TEXT = [
	[
	InlineKeyboardButton("πJoin Channel", url=f"https://t.me/{Config.CHANNEL}"),
	],
]

VISIT_PM = [
	[
	InlineKeyboardButton('βοΈβββββββββββββββοΈ', callback_data='stats_callback'),
	],
	[
	InlineKeyboardButton('βοΈ Visit PM βοΈ', url=f'https://t.me/{Config.BOT_USERNAME}?start'),
	],
]

LOGO = """

BOT FUCKING STATED

"""
