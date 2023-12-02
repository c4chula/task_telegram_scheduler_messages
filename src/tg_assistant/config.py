import os

from dotenv import load_dotenv

load_dotenv()


class TelegramConfig:
    api_id: int = int(os.environ.get("TELEGRAM_API_ID", ""))
    api_hash: str = os.environ.get("TELEGRAM_API_HASH", "")


class DatabaseConfig:
    sqlite_url: str = os.environ.get("SQLITE_URL", "sqlite+aiosqlite://")


class Config(
    TelegramConfig,
    DatabaseConfig,
):
    ...


cfg = Config()
