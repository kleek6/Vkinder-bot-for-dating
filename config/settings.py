"""
Описание возможных значений:
False - нет, True - да
'' - строка, само содержимое пишется между кавычками
"""

ACCESS_TOKEN_GROUP = '' # Вставьте свой токен от сообщества

ACCESS_TOKEN_USER = '' # Вставьте свой токен пользователя




# Файлы параметров
LEXICON_FILE_NAME = 'cfg/lexicon.json'  # лексикон чат бота
ANSWER_FILE_NAME = 'cfg/answers.json'  # ответы для команд чат бота
VK_GUIDE_FILE_NAME = 'cfg/vk_guide.json'  # справочник ВК

# Данные для базы данных PostgreSQL
DATABASE_SETTINGS = ('DATABASE_NAME', 'HOST', 5432, 'USER', 'PASSWORD')
DATABASE_CHARSET = 'utf8mb4'  # utf8mb4, latin1 и т.д.
DATABASE_REWRITE = False  # перезаписывать и пересоздать все таблицы БД при запуске бота
DATABASE_JSON = 'database/temp'  # путь для json файлов, в случае неработоспособности БД


# Терминальное логирование
LOG_MESSAGES = True  # нужно ли писать получаемые сообщения в лог
LOG_COMMANDS = True  # нужно ли писать выполняемые команды в лог

# Настройки поиска и вывода данных ВК
YEAR_OFFSET = 1  # параметры поиска контактов по возрасту +/- YEAR_OFFSET
COUNT_RECORDS = 5  # количество найденных контактов, передаваемых за один раз пользователю