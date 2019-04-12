
import re

from challenge.exceptions import CreditCartdInvalid

from . import AbstractTypePayment

BRANDS = {
    'Visa': re.compile(r'^4[0-9]{6,}$'),
    'Mastercard': re.compile(
        r'^5[1-5][0-9]{5,}|222[1-9][0-9]{3,}|22[3-9][0-9]{4,}|2[3-6][0-9]{5,}|27[01][0-9]{4,}|2720[0-9]{3,}$',
        re.VERBOSE),
    'American Express': re.compile(r'^3[47][0-9]{5,}$'),
    'Diners Club': re.compile(r'^3(?:0[0-5]|[68][0-9])[0-9]{4,}$'),
    'Discover': re.compile(r'^6(?:011|5[0-9]{2})[0-9]{3,}$'),
    'JCB': re.compile('^(?:2131|1800|35[0-9]{3})[0-9]{3,}$')}


class Card(AbstractTypePayment):
    """Class payment Boleto."""
    __type__ = 'card'

    @staticmethod
    def __check_validate_credit_card(card_number):
        """Validate Credit Card."""
        def digits_of(n):
            return [int(d) for d in str(n)]
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10 == 0

    def __validate_credit_card(self, p_number):
        """Validate credit card."""
        if not self.__check_validate_credit_card(p_number):
            raise CreditCartdInvalid("Credit Card Invalid")

    @staticmethod
    def __check_provider(number):
        """Checks a credit card number and returns a matching brand name."""
        for brand, regexp in BRANDS.items():
            if regexp.match(number):
                return brand
        return 'Not Identify'

    def create(self, param):
        """Create payment."""
        number = param.get("card_number").strip(" ")
        self.__validate_credit_card(number)
        flag = self.__check_provider(number)

        return {"type card": flag}
