import vk_api
from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from config import config
from keyboards.inline import keyboard_forward
from utils.misc import msg_analysis
from utils.stateform import StepsForm, ForwardBtn
from utils.text import FOR_POST_VACANCY_TEXT, FOR_POST_RESUME_TEXT, NO_FORWARD_TEXT, MY_SOURCE_TEXT
from aiogram.utils.formatting import Text, Bold
from aiogram.utils import markdown, formatting

adminID = config.adminID
chatID = config.chatID
TOKEN_VK = config.TOKEN_VK.get_secret_value()
groupID_VK = config.groupID_VK


async def to_post_vacancy(call: CallbackQuery, bot: Bot, state: FSMContext):
    if call.data == 'post_vacancy':
        await call.answer()
        await bot.send_message(call.from_user.id,
                               f'Вы выбрали: РАЗМЕСТИТЬ ВАКАНСИЮ')
        await bot.send_message(call.from_user.id,
                               FOR_POST_VACANCY_TEXT, parse_mode=ParseMode.MARKDOWN)
        await state.set_state(StepsForm.GET_JOBS)
# ....


async def to_post_resume(call: CallbackQuery, bot: Bot, state: FSMContext):
    if call.data == 'post_resume':
        await call.answer()
        await bot.send_message(call.from_user.id,
                               f'Вы выбрали: РАЗМЕСТИТЬ РЕЗЮМЕ')
        await bot.send_message(call.from_user.id,
                               FOR_POST_RESUME_TEXT, parse_mode=ParseMode.MARKDOWN)
        await state.set_state(StepsForm.GET_SUMMARY)
# ....


async def forward_msg(message: Message, state: FSMContext):
    if message.from_user.id == adminID:
        name_fwd = msg_analysis(message).get('name_fwd')
        name_fwd_for_VK = msg_analysis(message).get('name_fwd_for_VK')
        text_fwd = msg_analysis(message).get('text_fwd')
        msg_fwd = msg_analysis(message).get('msg_fwd')

        await message.answer(text_fwd, parse_mode=ParseMode.HTML)

        await message.answer(text=f'Итого получаем следующий текст:\n\n #вакансия {name_fwd} '
                                  f'\n\n{msg_fwd}',
                             parse_mode=ParseMode.HTML, disable_web_page_preview=True)
        await message.answer("Подтверждаете отправку?",
                             parse_mode=ParseMode.HTML, reply_markup=keyboard_forward)

        # передача данных для дальнейшего поста через FSM:
        await state.update_data(name_fwd=name_fwd, name_fwd_for_VK=name_fwd_for_VK, msg_fwd=msg_fwd)

        print("====00001 name_fwd=== ", name_fwd)
        # print("====00002 msg_fwd=== ", msg_fwd)

        await state.set_state(ForwardBtn.FORWARD_STATE)
    else:
        await message.reply(NO_FORWARD_TEXT)


async def post_forward_msg(call: CallbackQuery, bot: Bot, state: FSMContext):
    context_data = await state.get_data()  # получение данных с предыдущего этапа "forward_msg"
    name_fwd = context_data.get('name_fwd')
    name_fwd_for_VK = context_data.get('name_fwd_for_VK')
    msg_fwd = context_data.get('msg_fwd')

    print("===1 msg_fwd====", msg_fwd)

    if call.data == 'fwd_no':
        await call.message.edit_reply_markup()
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
        await bot.send_message(chat_id=call.from_user.id,
                               text=f'Вы своей волей отклонили публикацию данного сообщения')
    else:
        pretext = "#вакансия" if call.data == 'fwd_vacancy' else "#резюме"

        vk_session = vk_api.VkApi(token=TOKEN_VK)
        vk_session.method('wall.post',
                          {'owner_id': groupID_VK,
                           'message': f'{pretext} {name_fwd_for_VK}\n\n {msg_fwd}\n\n {MY_SOURCE_TEXT}'})

        await bot.send_message(chat_id=chatID,
                               text=f'{pretext} {name_fwd}\n\n' + msg_fwd,
                               parse_mode=ParseMode.HTML, disable_web_page_preview=True)
        await call.message.edit_reply_markup()
        await bot.send_message(chat_id=call.from_user.id,
                               text=f'О всемогущий,вы подтвердили отправку этой "{pretext}" в основной канал')


# # ====================================================
# # ====================================================
# # ====================================================
        # await state.update_data(name_fwd=name_fwd, name_fwd_for_VK=name_fwd_for_VK, msg_fwd=message.text)
# # ====================================================
        # pretext = "#вакансия"
        # if call.data == 'fwd_vacancy':
        #     pretext = "#вакансия"
        # elif call.data == 'fwd_resume':
        #     pretext = "#резюме"

# # ====================================================
#     if call.data == 'fwd_vacancy':
#         vk_session = vk_api.VkApi(token=TOKEN_VK)
#         vk_session.method('wall.post',
#                           {'owner_id': groupID_VK,
#                            'message': f'#вакансия {name_fwd_for_VK}\n\n {msg_fwd}\n\n {MY_SOURCE_TEXT}'})
#         await bot.send_message(chat_id=chatID,
#                                text=f'#вакансия {name_fwd}\n\n' + msg_fwd,
#                                parse_mode=ParseMode.HTML, disable_web_page_preview=True)
#         await call.message.edit_reply_markup()
#         await bot.send_message(chat_id=call.from_user.id,
#                                text=f'О всемогущий,вы подтвердили отправку этой вакансии в основной канал')
#
#     elif call.data == 'fwd_resume':
#         vk_session = vk_api.VkApi(token=TOKEN_VK)
#         vk_session.method('wall.post',
#                           {'owner_id': groupID_VK,
#                            'message': f'#резюме {name_fwd_for_VK} \n\n {msg_fwd}\n\n {MY_SOURCE_TEXT}'})
#         await bot.send_message(chat_id=chatID,
#                                text=f'#резюме {name_fwd}\n\n' + msg_fwd,
#                                parse_mode=ParseMode.HTML, disable_web_page_preview=True)
#         await call.message.edit_reply_markup()
#         await bot.send_message(chat_id=call.from_user.id,
#                                text=f'О всемогущий,вы подтвердили отправку этого резюме в основной канал')
#
#     elif call.data == 'fwd_no':
#         await call.message.edit_reply_markup()
#         await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
#         await bot.send_message(chat_id=call.from_user.id,
#                                text=f'Вы своей волей отклонили публикацию данного сообщения')
# # ====================================================
        # await call.answer()
# ====================================================
# await state.update_data(name_forward=name_forward, text_forward=text_forward, msg_forward=message.html_text)  # передача значения текста для дальнейшего поста
# vk_session.method('wall.post', {'owner_id': groupID_VK, 'message': f'#вакансия от {name_forward}\n\n' + f'{msg_forward}\n\n' + MY_SOURCE_TEXT})
#         await call.message.answer(text="zzzzzzzzzzzzzzzz")

# ====================================================
# name_fwd_for_VK = f'tg://user?id={message.forward_from.id}'
# name_fwd_for_VK = f'https://t.me/user?id={message.forward_from.id}'
    # print("====name_forward 0 ===", name_forward)
    # print("====msg_forward 2 ===", msg_forward)
    # print("====Call 1 ===", call.from_user)
    # print("====Call 2 ===", call.message)
    # print("====bot 1 ===", bot.__dict__)

# ====================================================
# ====================================================