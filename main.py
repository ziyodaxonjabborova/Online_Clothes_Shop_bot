from aiogram import Bot,Dispatcher,F
from environs import Env
import logging

import asyncio
import os

from handlers import start_router



dp=Dispatcher()
TOKEN=os.getenv("TOKEN")







async def main():

    bot = Bot(token=TOKEN)
    dp.include_router(start_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
