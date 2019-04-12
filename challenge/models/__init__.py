
from challenge.config import get_config
from sqlalchemy import Column, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

from .orm import Orm

config_neighbors = get_config()
Base = declarative_base()


class BaseModel(Base):
    """Defaut Classe to tables of system."""

    __abstract__ = True
    __TYPE__ = "abstract"
    date_created = Column(DateTime,
                          default=func.current_timestamp())
    date_modified = Column(DateTime,
                           default=func.current_timestamp(),
                           onupdate=func.current_timestamp())

    @property
    def __orm(self):
        return Orm()

    @property
    def session(self):
        return self.__orm.session

    def remove_session(self):
        """Method clear session sqlalchemy."""
        self.__orm.remove_session()

    def _commit(self, p_object):
        """Add in database."""
        self.__orm.object_commit(p_object)

    def _delete_object(self, p_object):
        """Delete a object in database"""
        self.__orm.delete_object(p_object)
