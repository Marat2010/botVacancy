from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


# команды внизу экрана бота, как базовые для его запуска: там где три полоски
async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Запуск бота'
        ),
        BotCommand(
            command='help',
            description='помощь'
        ),
        BotCommand(
            command='misc',
            description='разное'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())

