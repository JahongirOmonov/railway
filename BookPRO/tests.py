import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from nimadir import start_bosganda, bot_ishga_tushganda, bot_ishdan_toxtaganda
from aiogram.filters import CommandStart


dp = Dispatcher()
TOKEN = "8459503640:AAGzg_HIEcL1nJjgxxgVgrKgd1_SYXBgu-8"


async def main():
    dp.startup.register(bot_ishga_tushganda)
    dp.message.register(start_bosganda, CommandStart())
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.shutdown.register(bot_ishdan_toxtaganda)
    await dp.start_polling(bot)


asyncio.run(main())



