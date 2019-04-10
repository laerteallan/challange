
from challenge.exceptions import (ErrorStartTornado, GenericError,
                                  InstanceNotFound, ParamInvalid)
from tests import BaseTestClass


class TestException(BaseTestClass):

    """Class for test the methods module exception."""

    def test_class_param_invalid(self):
        """Test class ParamInvalid.
        :returns: Exception

        """
        with self.assertRaises(Exception):
            raise ParamInvalid("teste")

    def test_class_erros_start_tornado(self):
        """Test class ErrorStartTornado.
        :returns: Exception

        """
        with self.assertRaises(Exception):
            raise ErrorStartTornado("teste")

    def test_class_generic_error(self):
        """Test class ParamInvalid.
        :returns: Exception

        """
        with self.assertRaises(Exception):
            msg = "error teste"
            raise GenericError(msg, 500, {"status": "ok"})

    def test_generic_error_with_class(self):
        """Test class ParamInvalid.
        :returns: Exception

        """
        status_code = 500
        payload = {"status": "ok"}
        msg = "error teste"
        error = GenericError(msg, status_code, payload)
        self.assertEqual(error.status_code, status_code)
        self.assertEqual(error.payload, payload)
        self.assertIsInstance(error.to_dict(), dict)

    def test_class_instance_not_found(self):
        """Test class ParamInvalid.
        :returns: Exception

        """
        with self.assertRaises(Exception):
            msg = "error teste"
            raise InstanceNotFound(msg, 500, {"status": "ok"})
