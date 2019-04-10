

from challenge.service import Singleton
from tests import BaseTestClassTornado


class TestApi(BaseTestClassTornado):

    def setUp(self):
        Singleton.drop()
        super(TestApi, self).setUp()
        self._url = "/v1/api?partner={}&pageNumber={}"
        self._header = {"content-type": "application/json",
                        }

    def test_list(self):
        """Test the list."""
        pass
