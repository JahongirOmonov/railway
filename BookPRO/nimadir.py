from aiogram.types import Message
from aiogram import Bot
from pyexpat.errors import messages


async def start_bosganda(message: Message):
    await message.answer("Assalomu alaykum")

async def bot_ishga_tushganda(bot: Bot):
    await bot.send_message(chat_id=8071661785, text="Bot ishga tusshdi")


async def bot_ishdan_toxtaganda(bot: Bot):
    await bot.send_message(chat_id=8071661785, text="Bot ishdan toxtadi")
