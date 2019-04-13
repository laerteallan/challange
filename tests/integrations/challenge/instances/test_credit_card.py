
from challenge.models.payments import STATUS_SUCCESS
from challenge.service.factory import FactoryTypePayment
from tests import BaseTestClass


class TestPaymentCreditCardModel(BaseTestClass):
    """Test pyament CreditCard."""

    def test_create_american_express(self):
        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "card_name": "CARDNAME",
                 "card_number": "372383317788974",
                 "card_expiration_date": "12/21",
                 "card_cvv": 789,
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}

        instance = FactoryTypePayment.get_instance("card")
        result = instance.create(param)
        self.assertEqual(result["card_flag"], "American Express")
        result = instance.get_info_dict()
        self.assertEqual(result["client_id"], param["client_id"])
        self.assertEqual(result["name_buyer"], param["name_buyer"])
        self.assertEqual(result["email_buyer"], param["email_buyer"])
        self.assertEqual(result["cpf_buyer"], param["cpf_buyer"])
        self.assertEqual(float(result["amount"]), param["amount"])
        self.assertEqual(result["status"], "SUCCESS")
        self.assertEqual(result["card_name"], param["card_name"])
        self.assertEqual(result["card_number"], param["card_number"])
        self.assertEqual(result["card_flag"], "American Express")
        self.assertEqual(result["card_expiration_date"], param["card_expiration_date"])
        self.assertEqual(result["card_cvv"], param["card_cvv"])
