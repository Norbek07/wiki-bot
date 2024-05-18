import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,F #new
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import Message,input_file
from cat import get_cat_image
from wiki import malumot


TOKEN = "7083075969:AAGXj8oUQ_PVxwONVZ47chbiA4xlg-bYtgE"
ADMIN = 1245143580
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, Bu bizning birinchi botimiz"
    await message.answer(text)



@dp.message(Command("cat"))
async def get_cat(message:Message):
    image_content = get_cat_image()
    if image_content:
        await message.answer_document(document=input_file.BufferedInputFile(file=image_content,filename="cat.png"))

@dp.message(F.text)
async def wiki_malumot(message:Message):
    text = message.text
    natija = malumot(text)
    await message.reply(text=natija)


@dp.startup()
async def bot_start():
    await bot.send_message(1245143580,"Botimiz ishga tushdi")

@dp.shutdown()
async def bot_stop():
    await bot.send_message(1245143580,"Xayr")


async def main():
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())