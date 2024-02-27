from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    # === Telegram ===
    # Желательно вместо str использовать SecretStr для конфиденциальных данных, например, токена бота
    TOKEN_TG: SecretStr
    adminID: int
    chatID: int

    admin_chat: int
    admin_chat2: int = -0  # Если нет данных в ".env", то берется по умолчанию "-0"

    # === Telegram settings (WEB SERVER) ===
    WEB_SERVER_HOST: str = "127.0.0.1"  # Если нет данных в ".env", то берется по умолчанию "127.0.0.1"
    WEB_SERVER_PORT: int = 8080
    WEBHOOK_PATH: str = "/webhook"
    BASE_WEBHOOK_URL: str = "https://c859-178-204-157-185.ngrok-free.app"
    # on_Alwaysdata: bool = True
    # Переменная для локального запуска не нужна, если в ".env" нет переменных "WEB_SERVER_HOST", "WEB_SE ..
    # или они закомментированы, то берутся значения по умолчанию, которые прописаны здесь "127.0.0.1", "8080 ..

    # === VK ===
    TOKEN_VK: SecretStr
    groupID_VK: int

    # Начиная со второй версии pydantic, настройки класса настроек задаются через model_config
    # В данном случае будет использоваться файла .env, который будет прочитан с кодировкой UTF-8
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')
    # Пример пути файла на 2 уровня вверх: env_file='../../.env', или в "utils":  env_file='utils/.env'
    # ДАННЫЕ БЕРУТСЯ СНАЧАЛА из переменных окружения, если их там нет, то из файла ".env"


# При импорте файла сразу создастся и провалидируется объект конфига, который можно импортировать из разных мест
config = Settings()

print("=== Настройки: ===")
[print(i) for i in config]


# ================================================
# if config.on_Alwaysdata:
#     config.WEB_SERVER_HOST = '::'
#     config.WEB_SERVER_PORT = 8350
#     config.WEBHOOK_PATH = "/bot"
#     config.BASE_WEBHOOK_URL = "https://mara.alwaysdata.net"
# else:
#     config.WEB_SERVER_HOST = "127.0.0.1"
#     config.WEB_SERVER_PORT = 8080
#     config.WEBHOOK_PATH = "/webhook"
#     config.BASE_WEBHOOK_URL = "https://3848-178-205-237-188.ngrok-free.app"
# ================================================


