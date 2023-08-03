
import sys

from dotenv import dotenv_values
from flask import Flask, request
from jinja2 import Environment, PackageLoader

import data

cfg = dotenv_values(".env")

sys.path.append(f"{cfg['APP_HOME']}")

courtbot = Flask(__name__)
application = courtbot
env = Environment(loader=PackageLoader('courtbot'))

# when running the CourtBotUI application:
#
# 127.0.0.1 - - [21/Jun/2023 12:09:16] "GET /getAllNames HTTP/1.1" 404 -
# 127.0.0.1 - - [21/Jun/2023 12:09:33] "GET /getAppearances HTTP/1.1" 404 -


@courtbot.route(f"/{cfg['WWW']}")
@courtbot.route(f"/{cfg['WWW']}/")
def courtbot_main():
    main = env.get_template('courtbot_main.html')
    context = data.courtbot_main()
    return main.render(**context)


@courtbot.route(f"/{cfg['WWW']}getRandom")
def courtbot_random():
    return data.find_random()


@courtbot.route(f"/{cfg['WWW']}getAppearances")
def courtbot_appearances():
    return data.find_appearances(request.args)


@courtbot.route(f"/{cfg['WWW']}register")
def courtbot_register(params):
    return data.register_appearances(request.args)


if __name__ == '__main__':
    courtbot.run(port=8080)

