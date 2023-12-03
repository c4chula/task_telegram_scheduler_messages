import sys

from loguru import logger

logger.add(sys.stdout, format="{time} | {level: <8} | {message}", level="DEBUG")
logger.add(
    "logs.log",
    format="{time} | {level: <8} | {name: ^15} | {function: ^15} | {line: >3} | {message}",
    rotation="9:00",
    compression="zip",
    level="INFO",
)
