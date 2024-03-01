import vk_api
from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from config import config
from keyboards.inline import keyboard_forward
from utils.misc import msg_analysis
from utils.stateform import ForwardBtn
from utils.text import NO_FORWARD_TEXT, MY_SOURCE_TEXT


adminID = config.adminID
chatID = config.chatID
TOKEN_VK = config.TOKEN_VK.get_secret_value()
groupID_VK = config.groupID_VK


async def forward_msg(message: Message, state: FSMContext):
    if message.from_user.id == adminID:
        msg_data = msg_analysis(message)  # получение подготовленных данных
        name_fwd = msg_data.get('name_fwd')
        name_fwd_for_VK = msg_data.get('name_fwd_for_VK')
        text_fwd = msg_data.get('text_fwd')
        msg_fwd = msg_data.get('msg_fwd')

        await message.answer(text_fwd, parse_mode=ParseMode.HTML)
        await message.answer(text=f'Итого получаем следующий текст:\n\n '
                                  f'#вакансия {name_fwd} \n\n {msg_fwd}',
                             parse_mode=ParseMode.HTML, disable_web_page_preview=True)
        await message.answer("Подтверждаете отправку?",
                             parse_mode=ParseMode.HTML, reply_markup=keyboard_forward)

        # передача данных для дальнейшего поста через FSM:
        await state.update_data(name_fwd=name_fwd, name_fwd_for_VK=name_fwd_for_VK, msg_fwd=msg_fwd)
        await state.set_state(ForwardBtn.FORWARD_STATE)
    else:
        await message.reply(NO_FORWARD_TEXT)


async def post_forward_msg(call: CallbackQuery, bot: Bot, state: FSMContext):
    context_data = await state.get_data()  # получение данных с предыдущего этапа "forward_msg"
    name_fwd = context_data.get('name_fwd')
    name_fwd_for_VK = context_data.get('name_fwd_for_VK')
    msg_fwd = context_data.get('msg_fwd')

    # Удаляем пред. сообщение с клавиатурой подтверждения
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

    if call.data == 'fwd_no':
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

        await bot.send_message(chat_id=call.from_user.id,
                               text=f'О всемогущий,вы подтвердили отправку "{pretext}" в основной канал')


# ============================================
        # await call.message.edit_reply_markup()
        # await call.message.delete_reply_markup()
# ============================================
# ============================================
# ============================================