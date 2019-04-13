import mock

from challenge.exceptions import InstanceNotFound
from challenge.models.credit_card import CreditCard
from challenge.service.factory import FactoryTypePayment
from tests import BaseTestClass


class TestFactoryModel(BaseTestClass):

    def test_get_instance(self):
        instance = FactoryTypePayment.get_instance("card")
        self.assertIsInstance(instance, CreditCard)

    def test_get_instance_instance_invalid(self):
        with self.assertRaises(InstanceNotFound):
            FactoryTypePayment.get_instance("testeste")

    @mock.patch("challenge.service.factory.Payments.list_objects")
    def test_list_objects(self, mock_list_objects):
        param_search = {"amount_item": 10,
                        "page": 0,
                        "value": "test",
                        "search_by": "name",
                        "type": "card"}
        FactoryTypePayment.list_objects(param_search)
        self.assertTrue(mock_list_objects.called)
