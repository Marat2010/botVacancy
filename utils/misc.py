from aiogram.types import Message


def msg_analysis(message: Message) -> dict:
    """
    Анализ объекта "Message" для формирования имени (ссылки) в сообщение от кого форварднуто,
    от пользователя, канала или закрытого канала. А также формирования сообщения.
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
        msg_fwd = message.html_text

    elif message.forward_from_chat:  # сообщение с канала, когда нет данных от кого форварднуто.

        if message.forward_from_chat.username:
            name_fwd = f'с канала <a href="https://t.me/{message.forward_from_chat.username}' \
                           f'/{message.forward_from_message_id}">{message.forward_from_chat.username}</a>'
            name_fwd_for_VK = f'с канала {message.forward_from_chat.username}: ' \
                              f'https://t.me/{message.forward_from_chat.username}/{message.forward_from_message_id}'
            text_fwd = f'о мой администратор! Это форварднутая вакансия ' \
                       f'<b>"{name_fwd}"</b> и надо разместить ее в основном канале?'
            # msg_fwd = message.text
            msg_fwd = message.html_text

        else:  # сообщение с канала, когда канал закрытый (сообщение в "message.caption")
            name_fwd = f'от <a href="tg://user?id={message.from_user.id}">' \
                       f'{message.from_user.username}</a>'
            name_fwd_for_VK = f'от {message.from_user.first_name}: ' \
                              f'https://t.me/{message.from_user.username}'
            text_fwd = f'о мой администратор! Это частный канал "{message.forward_from_chat.title}"!' \
                       f' <b>Не всем доступен!</b>\n Разместить ее в основном канале <b>от своего имени</b>'
            msg_fwd = message.caption

    else:  # сообщение когда нет информации и предлагаем отправить от своего имени
        name_fwd = f'от <a href="tg://user?id={message.from_user.id}">' \
                       f'{message.from_user.username}</a>'
        name_fwd_for_VK = f'от {message.from_user.first_name}: ' \
                          f'https://t.me/{message.from_user.username}'
        text_fwd = 'о мой администратор! Что-то написано и не распознано!! (возможно у пользователя ' \
                   'скрыта инфа о себе)\nРазместить ее в основном канале <b>от своего имени</b>'
        msg_fwd = message.html_text

    return {'name_fwd': name_fwd, 'name_fwd_for_VK': name_fwd_for_VK,
            'text_fwd': text_fwd, 'msg_fwd': msg_fwd}


