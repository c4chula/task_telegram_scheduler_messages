import uvloop

from tg_assistant.client import client
from tg_assistant.logger import logger

uvloop.install()

if __name__ == "__main__":
    logger.info("telegram client start working!)")
    client.run()
