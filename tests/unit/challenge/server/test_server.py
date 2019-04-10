
import mock
from tornado.web import Application

from challenge.exceptions import ErrorStartTornado
from challenge.server import Server
from challenge import views
from tests import BaseTestClass


class TestServer(BaseTestClass):

    """Class for test the methods module server."""

    @mock.patch('challenge.server.tornado.ioloop')
    def test_server(self, mock_ioloop):
        """TODO: Docstring for test_server_make.

        :arg1: TODO
        :returns: TODO

        """
        server = Server()
        self.assertIsInstance(server.make_app(views), Application)
        server.start(views)
        self.assertTrue(mock_ioloop.IOLoop.instance().start.called)

    @mock.patch('challenge.server.tornado.ioloop')
    def test_server_error_start(self, mock_ioloop):
        """TODO: Docstring for test_server_make.

        :arg1: TODO
        :returns: TODO

        """
        mock_ioloop.side_effect = Exception("teste")
        with self.assertRaises(ErrorStartTornado):
            server = Server()
            server.start(views)
            self.assertTrue(mock_ioloop.IOLoop.instance().start.called)
