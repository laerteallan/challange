
from challenge.exceptions import InstanceNotFound

from challenge.models.boleto import Boleto
from challenge.models.credit_card import CreditCard
from challenge.models.payments import Payments


__all__ = ["Boleto", "CreditCard"]


class FactoryTypePayment(object):
    """Responsable to instanced class payment correct."""

    @staticmethod
    def get_instance(p_type, *args, **kwargs):
        for klass in Payments.__subclasses__():
            if klass.__type__ == p_type:
                return klass(*args, **kwargs)

        raise InstanceNotFound("Type %s payment implemented!" % p_type)

    @staticmethod
    def list_objects(kwargs):
        """List All objects."""
        payments = Payments()
        return payments.list_objects(kwargs)
