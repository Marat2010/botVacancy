import logging

import aiogram.filters
from aiohttp import web

from aiogram import Bot, Dispatcher, Router, F
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from config import config
from handlers.callback import forward_msg, post_forward_msg
from utils.commands import set_commands
from handlers.basic import command_start, command_help, keyboard_help, keyboard_start
from utils.stateform import ForwardBtn

# TOKEN_TG = getenv("BOT_TOKEN")
TOKEN_TG = config.TOKEN_TG.get_secret_value()
# WEB_SERVER_HOST = "127.0.0.1"
WEB_SERVER_HOST = config.WEB_SERVER_HOST
# WEB_SERVER_PORT = 8080
WEB_SERVER_PORT = config.WEB_SERVER_PORT
# WEBHOOK_PATH = "/webhook"
WEBHOOK_PATH = config.WEBHOOK_PATH
# Secret key to validate requests from Telegram (optional)
WEBHOOK_SECRET = "my-secret"

# BASE_WEBHOOK_URL = "https://aiogram.dev/"
BASE_WEBHOOK_URL = config.BASE_WEBHOOK_URL

# All handlers should be attached to the Router (or Dispatcher)
router = Router()


async def on_startup(bot: Bot) -> None:
    await bot.set_webhook(f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}", secret_token=WEBHOOK_SECRET)
    await set_commands(bot)
    await bot.send_message(config.adminID, text='Бот запущен')


async def on_shutdown(bot: Bot) -> None:
    logging.warning('Shutting down..')
    # insert code here to run it before shutdown
    await bot.send_message(config.adminID, text='Бот ушел спать')
    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()
    logging.warning('Bye!')


def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    # bot = Bot(TOKEN_TG, parse_mode=ParseMode.HTML)
    bot = Bot(TOKEN_TG)

    # Create aiohttp.web.Application instance
    app = web.Application()

    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=WEBHOOK_SECRET,
    )
    # Register webhook handler on application
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)

    # Mount dispatcher startup and shutdown hooks to aiohttp application
    setup_application(app, dp, bot=bot)

    # Register startup hook to initialize webhook
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    # Register basic handlers
    dp.message.register(command_start, aiogram.filters.CommandStart())
    dp.message.register(command_help, aiogram.filters.Command(commands='help'))
    dp.message.register(keyboard_help, F.text == 'Помощь')
    dp.message.register(keyboard_start, F.text == 'Запуск')

    dp.message.register(forward_msg)
    dp.callback_query.register(post_forward_msg, ForwardBtn.FORWARD_STATE)
    # ...

    # And finally start webserver
    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - %(name)s - '
                               '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
                        )

    main()


# ===============================================================
    # dp.callback_query.register(post_forward_msg, ADMINBTN.FRORWARD_STATE1)

    # dp.callback_query.register(to_post_vacancy, to_post_resume)
    # dp.callback_query.register(to_post_resume, to_post_vacancy)
    # dp.callback_query.register(to_post_resume)


    # ...

    # dp.message.register(echo_handler)

    # dp.message.register(zapysk, aiogram.filters.Command(commands='start'))
    # dp.message.register(ans_help, F.text == 'Помощь')
    # dp.message.register(ans_start, F.text == 'Запуск')
    # dp.callback_query.register(get_job, get_summary)
    # dp.callback_query.register(get_summary, get_job)
    # dp.callback_query.register(get_offer_work, get_other)
    # dp.callback_query.register(get_other, get_offer_work)

# ===============================================================
