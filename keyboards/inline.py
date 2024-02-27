from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# главное меню на вопрос ЧТО ВЫ ХОТИТЕ СДЕЛАТЬ?
main_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text='🔎 Разместить вакансию',
                callback_data='post_vacancy'
            ),
            InlineKeyboardButton(
                text='✍ Разместить резюме',
                callback_data='post_resume'
            )
        ],
        [
            InlineKeyboardButton(
                text='⚡ Предложить работы/услуги в сфере закупок',
                callback_data='offer_work'
            )
        ],
        [
            InlineKeyboardButton(
                text='🔔 Иное сообщение в канал',
                callback_data='other_message'
            )
        ],
        [
            InlineKeyboardButton(
                text='❓ Нужна помощь',
                callback_data='need_help'
            ),
            InlineKeyboardButton(
                text='☎ Связаться с админом',
                callback_data='msg_admin'
            )
       ]
],)

# меню подтверждения отправки Форвардных сообщений от Админа
keyboard_forward = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Да, ВАКАНСИЯ ✅',
            callback_data='fwd_vacancy'
        ),
        InlineKeyboardButton(
            text='Нет, НЕ РАЗМЕЩАТЬ ❌',
            callback_data='fwd_no'
        ),
    ],
    [
        InlineKeyboardButton(
            text='Нет, разместить как РЕЗЮМЕ',
            callback_data='fwd_resume'
        )
    ]
])

# # ========================================
# # меню подтверждения отправки ВАКАНСИИ
# keyboard_vacancy = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(
#             text='Да',
#             callback_data='YesVacancy'
#         ),
#         InlineKeyboardButton(
#             text='No',
#             callback_data='NoVacancy'
#         )
#     ]
# ])
#
# # меню подтверждения отправки РЕЗЮМЕ
# keyboard_resume = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(
#             text='Да',
#             callback_data='YesResume'
#         ),
#         InlineKeyboardButton(
#             text='No',
#             callback_data='NoResume'
#         )
#     ]
# ])
#
# # меню подтверждения отправки УСЛУГ
# keyboard_other_work = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(
#             text='Да',
#             callback_data='YesOtherWork'
#         ),
#         InlineKeyboardButton(
#             text='No',
#             callback_data='NoOtherWork'
#         )
#     ]
# ])
#
# # меню подтверждения отправки ИНЫХ СООБЩЕНИЙ
# keyboard_other_msg = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(
#             text='Да',
#             callback_data='YesOtherMsg'
#         ),
#         InlineKeyboardButton(
#             text='No',
#             callback_data='NoOtherMsg'
#         )
#     ]
# ])
#
# # меню подтверждения отправки СООБЩЕНИЙ АДМИНИСТРАТОРУ
# keyboard_msg_admin = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(
#             text='Да',
#             callback_data='YesMsgAdmin'
#         ),
#         InlineKeyboardButton(
#             text='Нет',
#             callback_data='NoMsgAdmin'
#         )
#     ]
# ])
