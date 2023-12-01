# Task Telegram Bot Scheduler

Воронка начинается после первого сообщения от клиента. *Пояснение: бот проверяет есть ли человек в БД, и если нет, то регистрирует его в БД и начинается воронка*

Через какое время | Сообщения, которые отправляет с момента последнего
через 10 минут | "Добрый день!"
через 90 минут | "Подготовила для вас материал"
Сразу после | "Отправка любого фото"
Через 2 часа, если не найден в истории сообщений триггер "Хорошего дня" (от лица нашего аккаунта) | "Скоро вернусь с новым материалом!"

Язык программирования: `python`
СУБД: `sqlite3`
ORM: `sqlalchemy`
Telegram: `pyrogram`
Логгер: `loguru`

- Использовать в качестве бота Person Account
- Бот проверяет есть ли человек в БД (Если нет, то создает)
- Выполнение задачи строго через единтсвенный while True task, который создаёте вместе с запуском клиента. Без scheduler, без asyncio.sleep(90 * 60) и тд.
- Логировать каждую успешную отправку сообщения с помощью loguru
- Сделать возможность просмотра кол-во зарегистрированный людей в БД за сегодня с помощью отправки команды /users_today в избранное аккаунта.
- Проблема scheduler: нужно помнить, что сообщение не всегда может быть доставлено (ТГ может выдать как PeerFlood, как другое нечто).
- Проблема asyncio.sleep(...): при перезапуске всё слетит.
