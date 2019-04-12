import random

from . import AbstractTypePayment


class Boleto(AbstractTypePayment):
    """Class payment Boleto."""
    __type__ = 'boleto'

    def __generate_number_boleto(self):
        return random.randint(1, 101)

    def create(self, param):
        """Method create payment boleto."""
        import pdb; pdb.set_trace()  # XXX BREAKPOINT

        return self.__generate_number_boleto()
