import logging
import random

from sqlalchemy import Column, ForeignKeyConstraint, Integer, String
from sqlalchemy.orm import relationship

from .payments import STATUS_SUCCESS, Payments

log = logging.getLogger(__file__)


class Boleto(Payments):
    """Model table Boleto payments."""

    __tablename__ = 'boletos'
    __type__ = 'boleto'

    id = Column(Integer, primary_key=True)
    number = Column(String(55), nullable=False)

    payments = relationship("Payments",
                            uselist=False,
                            single_parent=True,
                            cascade="all, delete, delete-orphan",
                            post_update=True
                            )
    __table_args__ = (ForeignKeyConstraint([id], ["payments.id"]),
                      {})
    __mapper_args__ = {'polymorphic_identity': 'bo'}

    def __init__(self):
        Payments.__init__(self)

    def __set_number(self):
        """Set number boleto."""
        self.number = random.randint(1, 101)

    def create(self, kwargs):
        """Create Payment Boleto."""
        name_buyer = kwargs.get("name_buyer")
        kwargs.update({"status": STATUS_SUCCESS})
        self.add_params_default(kwargs)
        self.__set_number()
        self._commit(self)
        log.info('Payment Boleto with sucess. %s ' % name_buyer)
        return {"number": self.number,
                "id": self.id}

    def get_info_dict(self):
        """Get Info object."""
        defaul_parms = super(Boleto, self).get_info_dict()
        result = {"number": self.number,
                  "type": "Boleto"
                  }
        result.update(defaul_parms)
        return result
