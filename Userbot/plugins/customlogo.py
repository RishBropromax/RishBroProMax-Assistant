import re
from Userbot import bot
from io import BytesIO
from requests import get
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
from os import getenv
from PIL import Image, ImageDraw, ImageFont
import random
import requests
import shutil
from config import Config

repmark = InlineKeyboardMarkup(
      [
        [
        InlineKeyboardButton(text="π‘ Bot π‘", url=f"http://t.me/{Config.BOT_USERNAME}") 
        ],
        [
         InlineKeyboardButton(text="β­ Join β­", url=f"https://t.me/{Config.CHANNEL}")
        ]
      ]
    )

imgcaption = f"""

**βοΈ Logo Created Successfully β**

"""


@bot.on_message(filters.command("xlogo") & ~filters.forwarded)
async def logomake(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("Please give a text.\nEx:`/logo Fuck` ")
    else:
        pass
    m = await message.reply('Designing your logo...wait!')
   await m.edit("Logo in processing...\n\n[ββββββββββ] 0%")
    await m.edit("Logo in processing...\n\n[ββββββββββ] 20%")
    await m.edit("Logo in processing...\n\n[ββββββββββ] 40%")
    await m.edit("Logo in processing...\n\n[ββββββββββ] 60%")
    await m.edit("Logo in processing...\n\n[ββββββββββ] 80%")
    await m.edit("Logo in processing...\n\n[ββββββββββ] 100%")
    await m.edit("π§©Exproting On Pixellab Sever...")
    await m.edit("π§βπ»Saving On ImRishmika Sever...")
    await m.edit("π€Removing Logo Watermark...")
    await m.edit("π€ Uploading...")
    text = message.text.split(None, 1)[1]
    Image_STD = Image.open("./Userbot/resources/maskbg.jpg")
    Image_font = ImageFont.truetype("./Userbot/resources/Flashing.otf", 220)
    Image_font2 = ImageFont.truetype("./Userbot/resources/Flashing.otf", 100)
    Image_text = f"."
    Image_edit = ImageDraw.Draw(Image_STD)
    image_width, image_height = Image_STD.size
    Image_edit.text((600, 600), text, (255, 255, 255), anchor="mt", font = Image_font)
    Image_STD.save("masklogo.jpg")
    await message.reply_photo(
                photo=f"masklogo.jpg",
                caption=imgcaption,
                reply_markup = repmark,
            )
    await m.delete()

@bot.on_message(filters.command("mlogo") & ~filters.forwarded)
async def logomake(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("Please give a text.\nEx:`/mlogo XXXXXX` ")
    else:
        pass
    m = await message.reply('Designing your logo...wait!')
    await m.edit("Logo in processing...\n\n[ββββββββββ] 0%")
    await m.edit("Logo in processing...\n\n[ββββββββββ] 20%")
    await m.edit("Logo in processing...\n\n[ββββββββββ] 40%")
    await m.edit("Logo in processing...\n\n[ββββββββββ] 60%")
    await m.edit("Logo in processing...\n\n[ββββββββββ] 80%")
    await m.edit("Logo in processing...\n\n[ββββββββββ] 100%")
    await m.edit("π§©Exproting On Pixellab Sever...")
    await m.edit("π§βπ»Saving On ImRishmika Sever...")
    await m.edit("π€Removing Logo Watermark...")
    await m.edit("π€ Uploading...")
    text = message.text.split(None, 1)[1]
    img = Image.open("./Userbot/resources/maskbg.jpg")
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./Userbot/resources/Flashing.otf", 400)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=0, stroke_fill="yellow")
    img.save("masklogo2.jpg")
    await message.reply_photo(
                photo=f"masklogo2.jpg",
                caption=imgcaption,
                reply_markup = repmark
            )
    await m.delete()


@bot.on_message(filters.command("logo") & ~filters.forwarded)
async def logomake(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("Please give a text.\nEx:`/plogo Sexy` ")
    else:
        pass
    m = await message.reply('Designing your logo...wait!')
   await m.edit("Logo in processing...\n\n[ββββββββββ] 0%")
    await m.edit("Logo in processing...\n\n[ββββββββββ] 20%")
    await m.edit("Logo in processing...\n\n[ββββββββββ] 40%")
    await m.edit("Logo in processing...\n\n[ββββββββββ] 60%")
    await m.edit("Logo in processing...\n\n[ββββββββββ] 80%")
    await m.edit("Logo in processing...\n\n[ββββββββββ] 100%")
    await m.edit("π§©Exproting On Pixellab Sever...")
    await m.edit("π§βπ»Saving On ImRishmika Sever...")
    await m.edit("π€Removing Logo Watermark...")
    await m.edit("π€ Uploading...")
    text = message.text.split(None, 1)[1]
    img = Image.open("./Userbot/resources/20220404_091513.jpg")
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("./Userbot/resources/The Humble.ttf", 370)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="white", stroke_width=4, stroke_fill="magenta")
    img.save("plogo.jpg")
    await message.reply_photo(
                photo=f"plogo.jpg",
                caption=imgcaption,
                reply_markup = repmark
            )
    await m.delete()

