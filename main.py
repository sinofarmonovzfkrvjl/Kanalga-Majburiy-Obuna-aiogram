from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio
import logging
import dotenv
import os

dotenv.load_dotenv()

bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher()

@dp.startup()
async def on_startup():
    print("Bot is started")

@dp.message(CommandStart())
async def start(message: types.Message):
    is_member = await bot.get_chat_member(chat_id="-1001954730128", user_id=message.from_user.id)
    if is_member.status == 'left':
        await message.answer("Kanalga obuna bo'ling")
    else:
        await message.answer(f"Salom {message.from_user.full_name}")

async def main():
    await dp.start_polling(bot)

logging.basicConfig(level=logging.INFO)
asyncio.run(main())