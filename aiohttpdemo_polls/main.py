import logging
import sys

import aiohttp_jinja2
import jinja2
from aiohttp import web

from aiohttpdemo_polls import db
from aiohttpdemo_polls import middlewares
from aiohttpdemo_polls import routes
from aiohttpdemo_polls import settings

def main():
    logging.basicConfig(level=logging.DEBUG)

    app = web.Application()
    app['config'] = settings.CONFIG

    aiohttp_jinja2.setup(
        app, loader=jinja2.PackageLoader('aiohttpdemo_polls', 'templates'))

    app.on_startup.append(db.init_pg)
    app.on_cleanup.append(db.close_pg)

    routes.setup_routes(app)

    middlewares.setup_middlewares(app)

    web.run_app(app)


if __name__ == '__main__':
    main()
