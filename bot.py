import asyncio
import os
from aiogram import Bot, Dispatcher, types

API_TOKEN = os.getenv("BOT_TOKEN")  # токен будет через переменную окружения

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Привет 👋 Я живу в облаке и работаю 24/7!")

@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())