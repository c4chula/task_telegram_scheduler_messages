from pyrogram import filters
from pyrogram.handlers.message_handler import MessageHandler

from tg_assistant.assistant.clients import Assistant
from tg_assistant.assistant.plugins.handlers import get_newbies_for_today
from tg_assistant.config import cfg

client = Assistant(
    cfg.api_id,
    cfg.api_hash,
)

client.add_handler(
    MessageHandler(
        get_newbies_for_today,
        filters.command("user_today"),
    ),
)
