from aiogram.types import Message


def msg_analysis(message: Message) -> dict:
    """
    Формирование имени (ссылки) в сообщение от кого форварднуто, от пользователя или канала.
    В случае когда нет информации, предлагаем отправить от своего имени.
    Возвращается словарь:
        - name_fwd: имя-ссылка для TG
        - name_fwd_for_VK: имя-ссылка для VK
        - text_fwd: текст подтверждения отправки сообщения в TG
        - msg_fwd: само сообщение TG
    :param message: Message
    :return: dict
    """

    if message.forward_from:  # сообщение, когда есть от кого форварднуто
        name_fwd = f'от <a href="tg://user?id={message.forward_from.id}">' \
                       f'{message.forward_from.first_name}</a>'
        name_fwd_for_VK = f'от {message.forward_from.first_name}: ' \
                          f'https://t.me/{message.forward_from.username}'
        text_fwd = f'о мой администратор! Это форварднутая вакансия ' \
                   f'<b>"{name_fwd}"</b> и надо разместить ее в основном канале?'
        msg_fwd = message.text

    elif message.forward_from_chat:  # сообщение с канала, когда нет данных от кого форварднуто.
        print('===`````message.forward_from_chat``````===', message.forward_from_chat)
        if message.forward_from_chat.username:
            name_fwd = f'с канала <a href="https://t.me/{message.forward_from_chat.username}' \
                           f'/{message.forward_from_message_id}">{message.forward_from_chat.username}</a>'
            name_fwd_for_VK = f'с канала {message.forward_from_chat.username}: ' \
                              f'https://t.me/{message.forward_from_chat.username}/{message.forward_from_message_id}'
            text_fwd = f'о мой администратор! Это форварднутая вакансия ' \
                       f'<b>"{name_fwd}"</b> и надо разместить ее в основном канале?'
            msg_fwd = message.text

        else:  # сообщение с канала, когда канал закрытый
            name_fwd = f'от <a href="tg://user?id={message.from_user.id}">' \
                       f'{message.from_user.username}</a>'
            name_fwd_for_VK = f'от {message.from_user.first_name}: ' \
                              f'https://t.me/{message.from_user.username}'
            text_fwd = f'о мой администратор! Это частный канал "{message.forward_from_chat.title}"! Не всем доступен!\n' \
                       'Разместить ее в основном канале <b>от своего имени</b>'
            msg_fwd = message.caption
            print('==== caption =====\n', msg_fwd)

    else:  # сообщение когда нет информации и предлагаем отправить от своего имени
        name_fwd = f'от <a href="tg://user?id={message.from_user.id}">' \
                       f'{message.from_user.username}</a>'
        name_fwd_for_VK = f'от {message.from_user.first_name}: ' \
                          f'https://t.me/{message.from_user.username}'
        text_fwd = 'о мой администратор! Что-то написано и не распознано!! (возможно у пользователя ' \
                   'скрыта инфа о себе)\nРазместить ее в основном канале <b>от своего имени</b>'
        msg_fwd = message.text



    # # Формирование текста подтверждения отправки сообщения в TG
    # if message.forward_from or message.forward_from_chat:
    #     text_fwd = f'о мой администратор! Это форварднутая вакансия ' \
    #                f'<b>"{name_fwd}"</b> и надо разместить ее в основном канале?'
    # else:
    #     text_fwd = 'о мой администратор! Что-то написано и не распознано!! (возможно у пользователя ' \
    #                'скрыта инфа о себе, или это частный канал)\nРазместить ее в основном канале <b>от своего имени</b>'

    return {'name_fwd': name_fwd, 'name_fwd_for_VK': name_fwd_for_VK, 'text_fwd': text_fwd, 'msg_fwd': msg_fwd}


# # подпрограмма для переработки текста при наличии символов Markdown
# def to_correct_message(IshodnoeTEXT):
#     GodForTelegramTEXT = IshodnoeTEXT  # базовое присвоение значение - в виде исходного текста. Потом начнем его перепроверки на символы из Markdown
#     # if (GodForTelegramTEXT.count('_')>0): # проверка и замена символов _ кроме как если они парные, и хотя бы один в начале слова - тогда считаем что это Markdown
#     if GodForTelegramTEXT.count('_'): # проверка и замена символов _ кроме как если они парные, и хотя бы один в начале слова - тогда считаем что это Markdown
#         # if not ((' _' in GodForTelegramTEXT)&(GodForTelegramTEXT.count('_') % 2 == 0)):
#         if not ((' _' in GodForTelegramTEXT) & (not GodForTelegramTEXT.count('_') % 2)):
#             print("=====1==== Меняем _ ===========")
#             #т.е. если одновременно (а)символ перед началом слова и (б)число вхождений четное, то в полноценный Markdown, и ничего в сообщении не меняем. Во всех иных случаях делаем замену
#             GodForTelegramTEXT = GodForTelegramTEXT.replace("_", "\_") # замена символов на их коды, чтобы не глючило - в отправляемом тексте
#     if GodForTelegramTEXT.count('*'): # проверка и замена символов _ кроме как если они парные, и хотя бы один в начале слова - тогда считаем что это Markdown
#         if not ((' *' in GodForTelegramTEXT) & (not GodForTelegramTEXT.count('*') % 2)):
#             print("=====1==== Меняем * ===========")
#             #т.е. если одновременно (а)символ перед началом слова и (б)число вхождений четное, то в полноценный Markdown, и ничего в сообщении не меняем. Во всех иных случаях делаем замену
#             GodForTelegramTEXT = GodForTelegramTEXT.replace("*", "\*") # замена символов на их коды, чтобы не глючило - в отправляемом тексте
#     return GodForTelegramTEXT


# ========================================================
# def from_whom_msg_old(username, user_id):
#     from_whom = f"[{username}](https://t.me/{username})"
#     # from_whom = f"[{username}](tg://user?id={str(user_id)})"
#     return from_whom

# ========================================================
# ========================================================
# ===============================
# на случай, если придется менять через коды, сохраню: ("_", "\u005F"), ("#", "\u0023")
# ===============================
    # from_whom = f"[{username}](tg://resolve?domain={username})"
    # from_whom = f"[{username}](tg://channell?id=test_g2024)"
    # from_whom = f"[{username}](tg://channel?username={username})"
    # name_froward = '[' + username + ']''(tg://user?id=' +  str(id) + ')'
# ===============================
# if message.forward_from:  # сообщение, когда есть от кого форварднуто
#     name_forward = f'от <a href="tg://user?id={message.forward_from.id}">' \
#                    f'{message.forward_from.username}</a>'
#     name_fwd_for_VK = f'от пользователя {message.forward_from.first_name}: ' \
#                       f'https://t.me/{message.forward_from.username}'
#     text_forward = f'о мой администратор! Это форварднутая вакансия ' \
#                    f'от <b>"{message.forward_from.first_name}"</b> и надо разместить ее в основном канале?'
#
# elif message.forward_from_chat:  # сообщение с канала, когда нет данных от кого форварднуто.
#     name_forward = f'с <b>канала</b> <a href="https://t.me/{message.forward_from_chat.username}' \
#                    f'/{message.forward_from_message_id}">{message.forward_from_chat.username}</a>'
#     name_fwd_for_VK = f'с канала {message.forward_from_chat.username}: ' \
#                       f'https://t.me/{message.forward_from_chat.username}/{message.forward_from_message_id}'
#     text_forward = f'о мой администратор! Это форварднутая вакансия <b>с канала ' \
#                    f'"{message.forward_from_chat.username}"</b> и надо разместить ее в основном канале?'
#
# else:  # сообщение когда нет информации и предлагаем отправить от своего имени
#     name_forward = f'от <a href="tg://user?id={message.from_user.id}">' \
#                    f'{message.from_user.username}</a>'
#     name_fwd_for_VK = f'от пользователя {message.from_user.first_name}: ' \
#                       f'https://t.me/{message.from_user.username}'
#     text_forward = 'о мой администратор! Что-то написано и не распознано!! (возможно у пользователя ' \
#                    'скрыта инфа о себе)\nРазместить ее в основном канале <b>от своего имени</b>'
# ===============================
# ===============================

