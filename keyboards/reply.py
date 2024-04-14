from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# команды внизу экрана бота, как базовые для его запуска: там где две большие кнопки

reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Запуск'),
            KeyboardButton(text='Помощь'),
            # KeyboardButton(text='Разное misc')
        ]
    ], resize_keyboard=True)

