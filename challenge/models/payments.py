import logging

from sqlalchemy import Column, Float, Integer, Sequence, String, func

from challenge.exceptions import ParamInvalid

from . import BaseModel

STATUS_SUCCESS = 1
STATUS_CANCELLED = 2

STATUS = {STATUS_SUCCESS: "SUCCESS",
          STATUS_CANCELLED: "CANCELLED"}

TYPE_PAYMENT = {"card": "cd",
                "boleto": "bo"}

log = logging.getLogger(__file__)


class Payments(BaseModel):
    """Model table Payments."""
    __type__ = 'payment'
    __tablename__ = 'payments'
    id = Column(Integer,
                Sequence('ger_payments_id'),
                primary_key=True)
    client_id = Column(Integer, nullable=False)
    name_buyer = Column(String(65), nullable=False)
    email_buyer = Column(String(80), nullable=False)
    status = Column(Integer, nullable=False)
    cpf_buyer = Column(String(11), nullable=False)
    amount = Column(Float, nullable=False)
    type_payment = Column(String(2))

    __mapper_args__ = {'polymorphic_identity': 'pa',
                       'polymorphic_on': type_payment
                       }

    def __init__(self):
        BaseModel.__init__(self)

    def __set_client_id(self, p_value):
        """Set id client."""
        if not p_value:
            raise ParamInvalid("Client id can't null.")
        self.client_id = p_value

    def __set_name_buyer(self, p_value):
        """Set name buye."""
        if not p_value:
            raise ParamInvalid("Name can't null.")
        self.name_buyer = p_value

    def __set_email_buyer(self, p_value):
        """Set email buyer."""
        if not p_value:
            raise ParamInvalid("Email can't null.")
        self.email_buyer = p_value

    def __set_cpf_buyer(self, p_value):
        """Set cpf buyer."""
        if not p_value:
            raise ParamInvalid("CPF can't null.")
        self.cpf_buyer = p_value

    def __set_status(self, p_value):
        """Set status buyer."""
        if p_value not in STATUS.keys():
            raise ParamInvalid("Status invalid. %s" % p_value)
        self.status = p_value

    def __set_amount(self, p_value):
        """Set amount."""
        if not p_value:
            raise ParamInvalid("Amount invalid")
        self.amount = p_value

    def __get_type_payment(self, p_type):
        """Return type payment."""
        if p_type not in TYPE_PAYMENT:
            raise ParamInvalid("Type Payament Invalid")
        return TYPE_PAYMENT[p_type]

    def add_params_default(self, kwargs):
        """Add payment."""
        client_id = kwargs.get("client_id")
        name_buyer = kwargs.get("name_buyer")
        email_buyer = kwargs.get("email_buyer")
        cpf_buyer = kwargs.get("cpf_buyer")
        amount = kwargs.get("amount")
        status = kwargs.get("status")
        self.__set_client_id(client_id)
        self.__set_name_buyer(name_buyer)
        self.__set_cpf_buyer(cpf_buyer)
        self.__set_status(status)
        self.__set_amount(amount)
        self.__set_email_buyer(email_buyer)

    def create(self, kwargs):
        log.info("Call methot not implemented. Param %s" % kwargs)
        raise NotImplementedError

    def get_info_dict(self):
        """Return all info in dict."""
        return {"client_id": self.client_id,
                "id": self.id,
                "name_buyer": self.name_buyer,
                "email_buyer": self.email_buyer,
                "status": STATUS.get(self.status),
                "cpf_buyer": self.cpf_buyer,
                "amount": "%.2f" % round(self.amount, 2)}

    def __get_options_search(self, search_by, value, p_type):
        """Query to search."""
        value = str(value).lower()
        query = self.session.query(Payments)
        if p_type:
            type_payment = self.__get_type_payment(p_type)
            query = self.session.query(Payments).filter_by(type_payment=type_payment)
        param = {"name": query.filter(func.lower(Payments.name_buyer).like("%{}%".format(value))),
                 "id": query.filter_by(id=value),
                 "cpf_buyer": query.filter_by(cpf_buyer=value)
                 }
        if search_by not in param:
            raise ParamInvalid("Param Invalid %s" % search_by)

        return param[search_by]

    def list_objects(self, kwargs):
        """List all clients."""
        amount_item = kwargs.get("amount_item", 0)
        page = kwargs.get("page", 0)
        value = kwargs.get("value", "")
        search_by = kwargs.get("search_by", "name")
        type_payment = kwargs.get("type", "")
        query = self.__get_options_search(search_by, value, type_payment)
        query = query.limit(amount_item).offset(page * amount_item)
        payments = []
        for payment in query:
            payments.append(payment.get_info_dict())
        return payments
