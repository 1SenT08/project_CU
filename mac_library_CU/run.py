import asyncio
from app.handlers import router
from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook

from config import BOT_TOKEN
from app.database.create_tables import async_main

async def main():
    await async_main()

    bot = Bot(token=BOT_TOKEN)
    await bot(DeleteWebhook(drop_pending_updates=True))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот завершил свою работу.')
