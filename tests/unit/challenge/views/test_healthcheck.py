from tests import BaseTestClassTornado


class TestHealthcheck(BaseTestClassTornado):

    def setUp(self):

        super(TestHealthcheck, self).setUp()
        self._url = "/healthcheck"
        self._header = {"content-type": "application/json",
                        }

    def test_healcheck(self):
        """Test healthcheck."""
        response = self.fetch(self._url, method="GET", headers=self._header)
        self.assertEqual(response.code, 200)
