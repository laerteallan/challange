
from challenge.models.payments import STATUS_SUCCESS
from challenge.service.factory import FactoryTypePayment
from tests import BaseTestClass


class TestPayment(BaseTestClass):
    """Test pyament CreditCard."""

    def test_list_object(self):
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
        result_create = instance.create(param)
        param_search = {"amount_item": 10,
                        "page": 0,
                        "value": param["name_buyer"][:3],
                        "search_by": "name",
                        "type": "card"}
        result = FactoryTypePayment.list_objects(param_search)
        self.assertIsNotNone(result)
        self.assertEqual(result[0]["name_buyer"], param["name_buyer"])
        self.assertEqual(result[0]["cpf_buyer"], param["cpf_buyer"])

        param_search.update({"value": result_create["id"],
                             "search_by": "id"})
        result = FactoryTypePayment.list_objects(param_search)
        self.assertIsNotNone(result)
        self.assertEqual(result[0]["id"], result_create["id"])

        param_search.update({"value": param["cpf_buyer"],
                             "search_by": "cpf_buyer"})
        result = FactoryTypePayment.list_objects(param_search)
        self.assertIsNotNone(result)
        self.assertEqual(result[0]["cpf_buyer"], param["cpf_buyer"])
