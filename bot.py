import asyncio
import os
import sys
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

# Загрузка токена
API_TOKEN = os.getenv("BOT_TOKEN")

if not API_TOKEN:
    print("❌ Ошибка: BOT_TOKEN не найден!")
    print("💡 Добавьте переменную BOT_TOKEN в Railway Variables")
    sys.exit(1)

# Инициализация бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("🚀 Бот успешно запущен на Railway!\n\n"
                        "Используйте /help для списка команд")

@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer("📋 Доступные команды:\n"
                        "/start - Запустить бота\n"
                        "/help - Помощь\n"
                        "/info - Информация о боте")

@dp.message(Command("info"))
async def info_command(message: Message):
    await message.answer("🤖 Этот бот работает на:\n"
                        "• Платформа: Railway\n"
                        "• Фреймворк: aiogram 3.x\n"
                        "• Язык: Python 3.11+")

async def main():
    print("✅ BOT_TOKEN загружен успешно")
    print("🚀 Запуск бота...")
    
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Бот остановлен пользователем")