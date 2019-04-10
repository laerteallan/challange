
import logging

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler

from challenge.config import get_config
from challenge.exceptions import ERRORS_CHALLENGE

config_ = get_config()
logger = logging.getLogger(__file__)


class ApiJsonHandler(RequestHandler):
    """Class default to create views."""

    def initialize(self):
        self.set_header("Content-Type", "application/json")

    @property
    def _message_error_default(self):
        """Error Internal Server."""
        return "Error Internal Server"

    async def _execute_ioloop_current(self, func, *args):
        resutl = await IOLoop.current().run_in_executor(None, func, *args)
        return resutl

    def write_error(self, status_code, **kwargs):
        self.clear()
        self.set_status(status_code)
        exception = str(kwargs["exc_info"][1])

        self.error(status_code, exception)

    def __message_default(self, type_message, status_code, message):
        result = {"status": type_message, "message": message}
        self.set_status(status_code)
        self.write(result)
        self.finish()

    def success(self, status_code, message):
        self.__message_default("success", status_code, message)

    def error(self, status_code, message):
        self.__message_default("error", status_code, message)

    async def _execute_method(self, p_method, p_param):
        """Execute method of instance."""
        try:
            result = await self._execute_ioloop_current(p_method, p_param)
            self.success(200, result)
        except ERRORS_CHALLENGE as error:
            logger.exception(str(error))
            self.error(400, str(error))
        except Exception as error:
            logger.exception(str(error))
            self.error(500, self._message_error_default)
