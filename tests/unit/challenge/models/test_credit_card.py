
import mock

from challenge.exceptions import ParamInvalid, CreditCartdInvalid
from challenge.models.credit_card import CreditCard
from challenge.models.payments import STATUS_SUCCESS
from tests import BaseTestClass


class TestPaymentCreditCardModel(BaseTestClass):
    """Test pyament CreditCard."""

    @mock.patch("challenge.models.credit_card.CreditCard._commit")
    def test_create_american_express(self, mock_commit):
        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "card_name": "CARDNAME",
                 "card_number": "372383317788974",
                 "card_expiration_date": "12/21",
                 "card_cvv": "789",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        card = CreditCard()
        result = card.create(param)
        self.assertTrue(mock_commit.called)
        self.assertEqual(result["card_flag"], "American Express")

    def test_create_card_name_null(self):
        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "card_name": "",
                 "card_number": "372383317788974",
                 "card_expiration_date": "12/21",
                 "card_cvv": "789",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        card = CreditCard()
        with self.assertRaises(ParamInvalid):
            card.create(param)

    def test_create_card_number_null(self):
        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "card_name": "name card",
                 "card_number": "",
                 "card_expiration_date": "12/21",
                 "card_cvv": "789",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        card = CreditCard()
        with self.assertRaises(CreditCartdInvalid):
            card.create(param)

    def test_create_card_expiration_date_null(self):
        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "card_name": "name card",
                 "card_number": "372383317788974",
                 "card_expiration_date": "",
                 "card_cvv": "789",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        card = CreditCard()
        with self.assertRaises(ParamInvalid):
            card.create(param)

    def test_create_card_cvv_null(self):
        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "card_name": "name card",
                 "card_number": "372383317788974",
                 "card_expiration_date": "12/21",
                 "card_cvv": "",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        card = CreditCard()
        with self.assertRaises(ParamInvalid):
            card.create(param)

    @mock.patch("challenge.models.credit_card.CreditCard._commit")
    def test_create_visa(self, mock_commit):
        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "card_name": "CARDNAME",
                 "card_number": "4539017137903692",
                 "card_expiration_date": "12/21",
                 "card_cvv": "789",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        card = CreditCard()
        result = card.create(param)
        self.assertTrue(mock_commit.called)
        self.assertEqual(result["card_flag"], "Visa")

    @mock.patch("challenge.models.credit_card.CreditCard._commit")
    def test_create_mastercard(self, mock_commit):
        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "card_name": "CARDNAME",
                 "card_number": "5472674868244427",
                 "card_expiration_date": "12/21",
                 "card_cvv": "789",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        card = CreditCard()
        result = card.create(param)
        self.assertTrue(mock_commit.called)
        self.assertEqual(result["card_flag"], "Mastercard")

    @mock.patch("challenge.models.credit_card.CreditCard._commit")
    def test_create_dinnes_club(self, mock_commit):
        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "card_name": "CARDNAME",
                 "card_number": "30150159349486",
                 "card_expiration_date": "12/21",
                 "card_cvv": "789",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        card = CreditCard()
        result = card.create(param)
        self.assertTrue(mock_commit.called)
        self.assertEqual(result["card_flag"], "Diners Club")

    @mock.patch("challenge.models.credit_card.CreditCard._commit")
    def test_create_discover(self, mock_commit):
        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "card_name": "CARDNAME",
                 "card_number": "6011740382108707",
                 "card_expiration_date": "12/21",
                 "card_cvv": "789",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        card = CreditCard()
        result = card.create(param)
        self.assertTrue(mock_commit.called)
        self.assertEqual(result["card_flag"], "Discover")

    @mock.patch("challenge.models.credit_card.CreditCard._commit")
    def test_create_not_identify(self, mock_commit):
        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "card_name": "CARDNAME",
                 "card_number": "3337668087991628",
                 "card_expiration_date": "12/21",
                 "card_cvv": "789",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        card = CreditCard()
        result = card.create(param)
        self.assertTrue(mock_commit.called)
        self.assertEqual(result["card_flag"], "Not Identify")

    @mock.patch("challenge.models.credit_card.CreditCard._commit")
    def test_create_jcb(self, mock_commit):
        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "card_name": "CARDNAME",
                 "card_number": "180047681417625",
                 "card_expiration_date": "12/21",
                 "card_cvv": "789",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        card = CreditCard()
        result = card.create(param)
        self.assertTrue(mock_commit.called)
        self.assertEqual(result["card_flag"], "JCB")

    def test_get_info_dict(self):
        """Test set default params."""

        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "card_name": "CARDNAME",
                 "card_number": "180047681417625",
                 "card_expiration_date": "12/21",
                 "card_cvv": 789,
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        payment = CreditCard()
        payment.create(param)
        result = payment.get_info_dict()
        self.assertEqual(result["client_id"], param["client_id"])
        self.assertEqual(result["name_buyer"], param["name_buyer"])
        self.assertEqual(result["email_buyer"], param["email_buyer"])
        self.assertEqual(result["cpf_buyer"], param["cpf_buyer"])
        self.assertEqual(float(result["amount"]), param["amount"])
        self.assertEqual(result["status"], "SUCCESS")
        self.assertEqual(result["card_name"], param["card_name"])
        self.assertEqual(result["card_number"], param["card_number"])
        self.assertEqual(result["card_flag"], "JCB")
        self.assertEqual(result["card_expiration_date"], param["card_expiration_date"])
        self.assertEqual(result["card_cvv"], param["card_cvv"])
