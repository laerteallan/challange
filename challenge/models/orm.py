
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from challenge.service import Singleton
from challenge.config import get_config

config = get_config()


class Orm(metaclass=Singleton):
    """Relation Object."""
    __TYPE__ = "abstract"

    def __init__(self):
        self.__engine = create_engine(config.SQLALCHEMY_DATABASE_URI,
                                      pool_pre_ping=True,
                                      pool_size=config.SQLALCHEMY_POOL_SIZE,
                                      )
        self.__db_session = scoped_session(sessionmaker(autocommit=False,
                                                        autoflush=False,
                                                        bind=self.__engine))

    @property
    def session(self):
        """Property db_session."""
        return self.__db_session

    @property
    def engine(self):
        """Property engine."""
        return self.__engine

    def __commit(self):
        """Commit in Database"""
        try:
            self.session.flush()
            self.session.commit()
        except Exception as error:
            self.session.rollback()
            self.session.expunge_all()
            raise error

    def object_commit(self, p_object):
        """Add object of the database."""
        self.session.add(p_object)
        self.__commit()

    def delete_object(self, p_object):
        """Delete object of the database."""
        self.session.delete(p_object)
        self.__commit()

    def remove_session(self):
        self.__db_session.remove()

    def test_connection_database(self):
        """Test connection test_connection_database."""
        result = ""
        with self.__engine.connect() as conn:
            result = conn.execute("SELECT * FROM pg_stat_activity")

        return result
