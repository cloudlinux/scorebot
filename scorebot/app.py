from aiohttp import web
from scorebot.api.api import get_app

if __name__ == "__main__":
    web.run_app(get_app(), port=8080)
