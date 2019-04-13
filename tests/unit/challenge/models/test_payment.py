import mock

from challenge.exceptions import ParamInvalid
from challenge.models.payments import STATUS_SUCCESS, Payments
from tests import BaseTestClass


class TestPaymentModel(BaseTestClass):

    def test_add_params_default(self):
        """Test set default params."""

        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        payment = Payments()
        payment.add_params_default(param)
        self.assertEqual(payment.client_id, param["client_id"])
        self.assertEqual(payment.name_buyer, param["name_buyer"])
        self.assertEqual(payment.email_buyer, param["email_buyer"])
        self.assertEqual(payment.cpf_buyer, param["cpf_buyer"])
        self.assertEqual(payment.amount, param["amount"])
        self.assertEqual(payment.status, param["status"])

    def test_add_params_default_client_id_null(self):
        """Test set client id null."""

        param = {"client_id": "",
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        payment = Payments()
        with self.assertRaises(ParamInvalid):
            payment.add_params_default(param)

    def test_add_params_default_name_buyer_null(self):
        """Test set name buyer null."""

        param = {"client_id": 10,
                 "name_buyer": "",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        payment = Payments()
        with self.assertRaises(ParamInvalid):
            payment.add_params_default(param)

    def test_add_params_default_email_null(self):
        """Test set email null."""

        param = {"client_id": 10,
                 "name_buyer": "Name test",
                 "email_buyer": "",
                 "cpf_buyer": "09185485617",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        payment = Payments()
        with self.assertRaises(ParamInvalid):
            payment.add_params_default(param)

    def test_add_params_default_cpf_null(self):
        """Test set cpf null."""

        param = {"client_id": 10,
                 "name_buyer": "Name test",
                 "email_buyer": "teste@email.com",
                 "cpf_buyer": "",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        payment = Payments()
        with self.assertRaises(ParamInvalid):
            payment.add_params_default(param)

    def test_add_params_default_amount_null(self):
        """Test set amount null."""

        param = {"client_id": 10,
                 "name_buyer": "Name test",
                 "email_buyer": "teste@email.com",
                 "cpf_buyer": "09170085618",
                 "amount": "",
                 "status": STATUS_SUCCESS}
        payment = Payments()
        with self.assertRaises(ParamInvalid):
            payment.add_params_default(param)

    def test_add_params_default_status_null(self):
        """Test set status null."""

        param = {"client_id": 10,
                 "name_buyer": "Name test",
                 "email_buyer": "teste@email.com",
                 "cpf_buyer": "09170085618",
                 "amount": 10.87,
                 "status": ""}
        payment = Payments()
        with self.assertRaises(ParamInvalid):
            payment.add_params_default(param)

    def test_create(self):
        """Test create."""

        payment = Payments()
        with self.assertRaises(NotImplementedError):
            param = {"tese": ""}
            payment.create(param)

    def test_get_info_dict(self):
        """Test set default params."""

        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        payment = Payments()
        payment.add_params_default(param)
        result = payment.get_info_dict()
        self.assertEqual(result["client_id"], param["client_id"])
        self.assertEqual(result["name_buyer"], param["name_buyer"])
        self.assertEqual(result["email_buyer"], param["email_buyer"])
        self.assertEqual(result["cpf_buyer"], param["cpf_buyer"])
        self.assertEqual(float(result["amount"]), param["amount"])
        self.assertEqual(result["status"], "SUCCESS")

    @mock.patch("challenge.models.payments.Payments.session")
    def test_list_objects(self, mock_session):
        """Test set default params."""
        param_search = {"amount_item": 10,
                        "page": 0,
                        "value": "test",
                        "search_by": "name",
                        "type": "card"}

        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        mock_payment_real = Payments()
        mock_payment_real.add_params_default(param)
        mock_session.query().filter_by().filter().limit().offset.return_value = [mock_payment_real]
        payment = Payments()
        value = payment.list_objects(param_search)
        self.assertIsInstance(value, list)

    def test_list_objects_type_payment_invalid(self):
        """Test set param type payment invalid."""
        param = {"amount_item": 10,
                 "page": 0,
                 "value": "test",
                 "search_by": "name",
                 "type": "teste"}
        payment = Payments()
        with self.assertRaises(ParamInvalid):
            payment.list_objects(param)

    def test_list_objects_search_by_invalid(self):
        """Test set param type payment invalid."""
        param = {"amount_item": 10,
                 "page": 0,
                 "value": "test",
                 "search_by": "teste",
                 "type": "card"}
        payment = Payments()
        with self.assertRaises(ParamInvalid):
            payment.list_objects(param)
