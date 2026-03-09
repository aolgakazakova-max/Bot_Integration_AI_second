from aiogram import Bot, Dispatcher
import asyncio
import logging
from config import BOT_TOKEN


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    await  dp.start_polling(bot)


asyncio.run(main())