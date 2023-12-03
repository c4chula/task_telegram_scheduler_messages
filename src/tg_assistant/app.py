import uvloop

uvloop.install()

from tg_assistant.client import client  # noqa: E402

if __name__ == "__main__":
    client.run()
