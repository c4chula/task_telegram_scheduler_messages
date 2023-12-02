import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()


@dataclass(slots=True)
class Config:
    api_id: int = int(os.environ.get("TELEGRAM_API_ID", ""))
    api_hash: str = os.environ.get("TELEGRAM_API_HASH", "")


cfg = Config()
