import sys
from challenge import views
from challenge.config import get_config
from challenge.server import Server

from challenge.models import Base
from challenge.models.orm import Orm

config_challenge = get_config()


def init_db(orm):
    """Create Database."""
    import challenge.models.payments
    import challenge.models.boleto
    import challenge.models.credit_card
    Base.metadata.create_all(bind=orm.engine)


def delete_all(orm):
    """Delete all database."""
    # Base.metadata.reflect(bind=engine, extend_existing=True)
    Base.metadata.drop_all(bind=orm.engine)
    # db_session.expunge_all()


def start():
    server = Server(instances=config_challenge.AMOUNT_PROCESS, port=config_challenge.PORT_SERVER)
    server.start(views)


def main(p_params):
    """Principal function."""
    if "start" in p_params:
        start()
    if "create" in p_params:
        if len(p_params) < 1:
            raise Exception("Not found url database.")
        orm = Orm()
        init_db(orm)


if __name__ == '__main__':
    main(sys.argv[1:])
