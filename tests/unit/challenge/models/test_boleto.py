import mock

from challenge.models.boleto import Boleto
from challenge.models.payments import STATUS_SUCCESS
from tests import BaseTestClass


class TestPaymentBoletoModel(BaseTestClass):
    """Test pyament Boleto."""
    @mock.patch("challenge.models.boleto.Boleto._commit")
    def test_create(self, mock_commit):
        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        boleto = Boleto()
        boleto.create(param)
        self.assertTrue(mock_commit.called)

    def test_get_info_dict(self):
        """Test set default params."""

        param = {"client_id": 10,
                 "name_buyer": "Name buyer",
                 "email_buyer": "teste@mail.com",
                 "cpf_buyer": "09185485617",
                 "amount": 1000.89,
                 "status": STATUS_SUCCESS}
        payment = Boleto()
        payment.create(param)
        result = payment.get_info_dict()
        self.assertEqual(result["client_id"], param["client_id"])
        self.assertEqual(result["name_buyer"], param["name_buyer"])
        self.assertEqual(result["email_buyer"], param["email_buyer"])
        self.assertEqual(result["cpf_buyer"], param["cpf_buyer"])
        self.assertEqual(float(result["amount"]), param["amount"])
        self.assertEqual(result["status"], "SUCCESS")
        self.assertIsNotNone(result["number"])
