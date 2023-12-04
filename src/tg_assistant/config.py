import os

from dotenv import load_dotenv

load_dotenv()


class TelegramConfig:
    api_id: int = int(os.environ.get("TELEGRAM_API_ID", ""))
    api_hash: str = os.environ.get("TELEGRAM_API_HASH", "")


class PostgresSettings:
    db_name: str = os.environ.get("DB_NAME", "")
    db_user: str = os.environ.get("DB_USER", "")
    db_password: str = os.environ.get("DB_PASSWORD", "")
    db_host: str = os.environ.get("DB_HOST", "")
    db_port: str = os.environ.get("DB_PORT", "")

    def get_db_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


class Config(
    TelegramConfig,
    PostgresSettings,
):
    ...


cfg = Config()
