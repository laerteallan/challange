import datetime
import logging
import re

from sqlalchemy import Column, ForeignKeyConstraint, Integer, String
from sqlalchemy.orm import relationship

from challenge.exceptions import CreditCartdInvalid, ParamInvalid, ExpirationDateExceeded

from .payments import STATUS_SUCCESS, Payments

log = logging.getLogger(__file__)

BRANDS = {
    'Visa': re.compile(r'^4[0-9]{6,}$'),
    'Mastercard': re.compile(
        r'^5[1-5][0-9]{5,}|222[1-9][0-9]{3,}|22[3-9][0-9]{4,}|2[3-6][0-9]{5,}|27[01][0-9]{4,}|2720[0-9]{3,}$',
        re.VERBOSE),
    'American Express': re.compile(r'^3[47][0-9]{5,}$'),
    'Diners Club': re.compile(r'^3(?:0[0-5]|[68][0-9])[0-9]{4,}$'),
    'Discover': re.compile(r'^6(?:011|5[0-9]{2})[0-9]{3,}$'),
    'JCB': re.compile('^(?:2131|1800|35[0-9]{3})[0-9]{3,}$')}


class CreditCard(Payments):
    """Model table creditCard payments."""

    __tablename__ = 'credits_cards'
    __type__ = 'card'

    id = Column(Integer, primary_key=True)
    card_name = Column(String(65), nullable=False)
    card_number = Column(String(19), nullable=False)
    card_expiration_date = Column(String(7), nullable=False)
    card_flag = Column(String(35), nullable=False)
    card_cvv = Column(Integer, nullable=False)

    payment = relationship("Payments",
                           uselist=False,
                           single_parent=True,
                           cascade="all, delete, delete-orphan",
                           post_update=True
                           )

    __table_args__ = (ForeignKeyConstraint([id], ["payments.id"]),
                      {})
    __mapper_args__ = {'polymorphic_identity': 'cd'}

    def __init__(self):
        Payments.__init__(self)

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
        if not p_number or not self.__check_validate_credit_card(p_number):
            raise CreditCartdInvalid("Credit Card Invalid")

    @staticmethod
    def __check_provider(number):
        """Checks a credit card number and returns a matching brand name."""
        for brand, regexp in BRANDS.items():
            if regexp.match(number):
                return brand
        return 'Not Identify'

    def __validate_date_expiration(self, p_value):
        try:

            date_format = '%m/%y'
            result = datetime.datetime.strptime(p_value, date_format)
            now = datetime.datetime.now()
            if now > result:
                raise ExpirationDateExceeded("Expiration Date Exceeded")
        except ValueError:
            raise ParamInvalid("time data '12310/19' does not match format '%m/%y'")

    def __set_card_name(self, p_value):
        """Set card name."""
        if not p_value:
            raise ParamInvalid("Card Name can't null.")
        self.card_name = p_value

    def __set_card_number(self, p_value):
        """Set card number."""
        self.__validate_credit_card(p_value)
        self.card_number = p_value

    def __set_flag_card(self, p_value):
        """Set Flag card."""
        self.card_flag = self.__check_provider(p_value)

    def __set_card_expiration_date(self, p_value):
        """Set card expiration."""
        if not p_value:
            raise ParamInvalid("Card Expiration date can't null.")
        self.__validate_date_expiration(p_value)
        self.card_expiration_date = p_value

    def __set_card_cvv(self, p_value):
        """Set card_cvv buyer."""
        if not p_value:
            raise ParamInvalid("Card CV invalid. %s" % p_value)
        self.card_cvv = p_value

    def create(self, kwargs):
        """Create Payment credit_card."""
        name_buyer = kwargs.get("name_buyer")
        card_name = kwargs.get("card_name")
        card_number = kwargs.get("card_number").strip(" ")
        card_expiration_date = kwargs.get("card_expiration_date")
        card_cvv = kwargs.get("card_cvv")
        kwargs.update({"status": STATUS_SUCCESS})
        self.add_params_default(kwargs)
        self.__set_card_number(card_number)
        self.__set_flag_card(card_number)
        self.__set_card_cvv(card_cvv)
        self.__set_card_expiration_date(card_expiration_date)
        self.__set_card_name(card_name)
        self._commit(self)
        log.info('Payment credit card with sucess. %s' % name_buyer)
        return {"card_flag": self.card_flag,
                "id": self.id}

    def get_info_dict(self):
        """Get Info object."""
        defaul_parms = super(CreditCard, self).get_info_dict()
        result = {"card_name": self.card_name,
                  "type": "Credit Card",
                  "card_number": self.card_number,
                  "card_flag": self.card_flag,
                  "card_expiration_date": self.card_expiration_date,
                  "card_cvv": self.card_cvv}
        result.update(defaul_parms)
        return result
