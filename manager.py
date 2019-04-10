import sys

from challenge import views
from challenge.config import get_config
from challenge.server import Server

config_challenge = get_config()


def start():
    server = Server(instances=config_challenge.AMOUNT_PROCESS, port=config_challenge.PORT_SERVER)
    server.start(views)


def main(p_params):
    """Principal function."""
    if "start" in p_params:
        start()


if __name__ == '__main__':
    main(sys.argv[1:])
