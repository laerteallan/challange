import copy
import json

import mock

from challenge.service import Singleton
from challenge.exceptions import ParamInvalid
from tests import BaseTestClassTornado


class TestApi(BaseTestClassTornado):

    def setUp(self):
        Singleton.drop()
        super(TestApi, self).setUp()
        self._url = "/v1/api/payments/type/{}"
        self._header = {"content-type": "application/json",
                        }

    @mock.patch("challenge.models.credit_card.CreditCard.create")
    def test_api_payment_card(self, mock_create):
        """Test the list."""
        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "card_name": "CARDNAME",
                 "card_number": "372383317788974",
                 "card_expiration_date": "12/21",
                 "card_cvv": 789,
                 "amount": 1000.89,
                 }
        url = copy.copy(self._url)
        url = url.format("card")
        mock_create.return_value = {"card_flag": "Visa",
                                    "id": 10}
        response = self.fetch(url, headers=self._header, method='POST', body=json.dumps(param))
        self.assertEqual(response.code, 200)
        self.assertTrue(mock_create.called)

    @mock.patch("challenge.models.credit_card.CreditCard.create")
    def test_api_payment_card_create_exception(self, mock_create):
        """Test the list."""
        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "card_name": "CARDNAME",
                 "card_number": "372383317788974",
                 "card_expiration_date": "12/21",
                 "card_cvv": 789,
                 "amount": 1000.89,
                 }
        url = copy.copy(self._url)
        url = url.format("card")
        mock_create.side_effect = Exception("Error inespected")
        response = self.fetch(url, headers=self._header, method='POST', body=json.dumps(param))
        self.assertEqual(response.code, 500)

    @mock.patch("challenge.models.credit_card.CreditCard.create")
    def test_api_payment_card_create_param_invalid(self, mock_create):
        """Test the list."""
        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "card_name": "CARDNAME",
                 "card_number": "372383317788974",
                 "card_expiration_date": "12/21",
                 "card_cvv": 789,
                 "amount": 1000.89,
                 }
        url = copy.copy(self._url)
        url = url.format("card")
        mock_create.side_effect = ParamInvalid("Invalid Param")
        response = self.fetch(url, headers=self._header, method='POST', body=json.dumps(param))
        self.assertEqual(response.code, 400)

    def test_api_payment_card_param_invalid(self):
        """Test the list."""
        param = {"client_id": 10,
                 "name_buyer": "",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "card_name": "CARDNAME",
                 "card_number": "372383317788974",
                 "card_expiration_date": "12/21",
                 "card_cvv": 789,
                 "amount": 1000.89,
                 }
        url = copy.copy(self._url)
        url = url.format("card")
        response = self.fetch(url, headers=self._header, method='POST', body=json.dumps(param))
        self.assertEqual(response.code, 422)

    def test_api_payment_type_invalid(self):
        """Test the list."""
        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "card_name": "CARDNAME",
                 "card_number": "372383317788974",
                 "card_expiration_date": "12/21",
                 "card_cvv": 789,
                 "amount": 1000.89,
                 }
        url = copy.copy(self._url)
        url = url.format("card1")
        response = self.fetch(url, headers=self._header, method='POST', body=json.dumps(param))
        self.assertEqual(response.code, 400)

    @mock.patch("challenge.models.boleto.Boleto.create")
    def test_api_payment_boleto(self, mock_create):
        """Test the list."""
        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "amount": 1000.89,
                 }
        url = copy.copy(self._url)
        url = url.format("boleto")
        mock_create.return_value = {"number": "fadfadsfadsf",
                                    "id": 10}
        response = self.fetch(url, headers=self._header, method='POST', body=json.dumps(param))
        self.assertEqual(response.code, 200)
        self.assertTrue(mock_create.called)

    @mock.patch("challenge.service.factory.FactoryTypePayment.list_objects")
    def test_api_payment_list_objects(self, mock_list_objects):
        """Test the list."""
        url = '/v1/api/payments?value=lae&amount_item=40&page=0&search_by=name&type=card'
        mock_list_objects.return_value = []
        response = self.fetch(url, headers=self._header, method='GET')
        self.assertEqual(response.code, 200)
        self.assertTrue(mock_list_objects.called)
