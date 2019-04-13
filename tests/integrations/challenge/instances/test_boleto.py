
from challenge.models.payments import STATUS_SUCCESS
from challenge.service.factory import FactoryTypePayment
from tests import BaseTestClass


class TestPaymentCreditCardModel(BaseTestClass):
    """Test pyament CreditCard."""

    def test_create(self):
        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}

        instance = FactoryTypePayment.get_instance("boleto")
        result = instance.create(param)
        result = instance.get_info_dict()
        self.assertEqual(result["client_id"], param["client_id"])
        self.assertEqual(result["name_buyer"], param["name_buyer"])
        self.assertEqual(result["email_buyer"], param["email_buyer"])
        self.assertEqual(result["cpf_buyer"], param["cpf_buyer"])
        self.assertEqual(float(result["amount"]), param["amount"])
        self.assertEqual(result["status"], "SUCCESS")
