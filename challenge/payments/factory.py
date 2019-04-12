
from challenge.exceptions import InstanceNotFound

from . import AbstractTypePayment
from .boleto import Boleto
from .credit_card import Card

__all__ = ["Boleto", "Card"]


class FactoryTypePayment(object):
    """Responsable to instanced class payment correct."""

    @staticmethod
    def get_instance(p_type, *args, **kwargs):
        for klass in AbstractTypePayment.__subclasses__():
            if klass.__type__ == p_type:
                return klass(*args, **kwargs)

        raise InstanceNotFound("Type %s payment implemented!" % p_type)
