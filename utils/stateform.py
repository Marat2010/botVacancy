from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    GET_JOBS = State()  # 1‑й шаг для отправки вакансии - предложили ввести ее описание
    GET_SUMMARY = State()  # 1‑й шаг для отправки резюме - предложили ввести его описание
    GET_OFFER = State()  # 1‑й шаг для отправки услуг - предложили ввести его описание
    GET_OTHER = State()  # 1‑й шаг для отправки иных сообщений - предложили ввести его описание


class ForwardBtn(StatesGroup):
    FORWARD_STATE = State()  # шаг для отправки Форварднутого сообщения - ввели текст и подтверждаем его отправку

