import copy
import logging

from webargs import ValidationError, fields
from webargs.tornadoparser import parser

from challenge.exceptions import ERRORS_CHALLENGE, TypePaymentNotFound
from challenge.service.factory import FactoryTypePayment
from challenge.views.v1 import ViewsChallenge

logger = logging.getLogger(__file__)


def validate_field_null(value):
    if not value:
        raise ValidationError("Param Invalid")


class Api(ViewsChallenge):
    __urls__ = ["{}/api/payments/type/(?P<type_payment>[a-zA-Z0-9]+)/?".format(ViewsChallenge._version)]
    __contract_default = {"client_id": fields.Int(required=True, validate=validate_field_null),
                          "name_buyer": fields.Str(required=True, validate=validate_field_null),
                          "email_buyer": fields.Email(required=True),
                          "cpf_buyer": fields.Str(required=True, validate=validate_field_null),
                          "amount": fields.Float(required=True),
                          }
    __contract_boleto = copy.copy(__contract_default)

    __contract_card = copy.copy(__contract_default)
    __contract_card.update({"card_name": fields.Str(required=True, validate=validate_field_null),
                            "card_number": fields.Str(required=True, validate=validate_field_null),
                            "card_expiration_date": fields.Str(required=True, validate=validate_field_null),
                            "card_cvv": fields.Int(required=True, validate=validate_field_null),
                            })
    __type_paymends = {"card": __contract_card,
                       "boleto": __contract_boleto}

    def __get_instance(self, p_type):
        """Return instance payment."""
        return FactoryTypePayment.get_instance(p_type)

    def __get_param_parser(self, p_type):
        if p_type not in self.__type_paymends.keys():
            raise TypePaymentNotFound("Payment not found %s" % p_type)
        return parser.parse(self.__type_paymends[p_type], self.request)

    async def post(self, type_payment):
        """Post to create payment."""
        try:
            param = self.__get_param_parser(type_payment)
            instance = self.__get_instance(type_payment)
            await self._execute_method(instance.create, param)
        except ERRORS_CHALLENGE as error:
            logger.exception(str(error))
            self.error(400, str(error))


class ViewListPayments(ViewsChallenge):
    """List Payments."""

    __urls__ = ["{}/api/payments".format(ViewsChallenge._version)]
    param_search_by = {"search_by": fields.Str(required=True, validate=validate_field_null),
                       "value": fields.Str(required=True, validate=validate_field_null),
                       "page": fields.Int(required=True, default=0),
                       "amount_item": fields.Int(required=True, default=20),
                       }

    async def get(self):
        """List all payments by params."""
        params = parser.parse(self.param_search_by, self.request, locations=("querystring", "json"))
        await self._execute_method(FactoryTypePayment.list_objects, params)
