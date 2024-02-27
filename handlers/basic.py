from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from keyboards.reply import reply_keyboard
from keyboards.inline import main_inline_keyboard

from utils.text import HELP_TEXT


# ===============================
# сообщение на команду start
async def command_start(message: Message) -> None:
    text_from = '[' + message.from_user.full_name + ']''(tg://user?id='\
                + str(message.from_user.id) + ')'
    await message.answer(f'Привет, {text_from}!\nНачинаем работу 👋\n'
                         f'(Используйте внизу кнопки ЗАПУСК и ПОМОЩЬ)',
                         reply_markup=reply_keyboard, parse_mode=ParseMode.MARKDOWN)


# ===============================
# сообщение на команду help
async def command_help(message: Message):
    await message.answer(HELP_TEXT, disable_web_page_preview=True, reply_markup=reply_keyboard)


# ===============================
# сообщение на команду help, с клавиатуры кнопка "Помощь"
async def keyboard_help(message: Message):
    await message.answer(HELP_TEXT, disable_web_page_preview=True)


# ===============================
# сообщение на кнопку "Запуск"
async def keyboard_start(message: Message):
    await message.answer(f'Что Вы хотите сделать?\nВыберите вариант:',
                         reply_markup=main_inline_keyboard, parse_mode='HTML')


# ===============================
# Эхо для тестов, проверки
# async def echo_handler(message: types.Message) -> None:
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
        await message.send_copy(chat_id=message.chat.id, parse_mode=ParseMode.MARKDOWN)
    except TypeError:
        await message.answer("Nice try!")


# ===============================
# ===============================
# ===============================
# ===============================
    # await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    # await message.answer(f'Это бот раздела "Закупочный хаб ProЗакупки".\n\nОн поможет в размещении вакансии или резюме, а также через него можно связаться с администрацией канала.\nНу и вообще сделать все что надо.\n\nНаши каналы:\n- Новости Интерфакса по закупкам https://t.me/InterfaxProZakupkiNews\n- Работа и Карьера в закупках: Вакансии & Кандидаты https://t.me/jobzakupki\n\nЕсли вдруг бот не запускается, воспользуйтесь командой /start, после чего внизу возникнут кнопки ЗАПУСК (основная часть функционала) и ПОМОЩЬ', disable_web_page_preview=True, reply_markup=reply_keyboard)
# reply_markup=reply_keyboard, parse_mode='Markdown')

# # сообщение на команду start
# async def zapysk(message: Message):
#     # text_from_to_telegram = '[' + def_to_whom_say(message.from_user)[0] + ']''(tg://user?id=' + str(message.from_user.id) + ')'
#     # await message.answer(f'Привет, {text_from_to_telegram}!\nНачинаем работу 👋\n(Используйте внизу кнопки ЗАПУСК и ПОМОЩЬ)', reply_markup=reply_keyboard, parse_mode='Markdown')
#     await message.answer('==Zapusk==')
