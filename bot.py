import asyncio
import os
from aiogram import Bot, Dispatcher, types

API_TOKEN = os.getenv("BOT_TOKEN")
print(">>> BOT_TOKEN из Railway:", API_TOKEN)  # проверка

if not API_TOKEN:
    raise ValueError("❌ Переменная BOT_TOKEN не найдена! Добавь её в Railway Variables")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("✅ Бот успешно запущен на Railway!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())