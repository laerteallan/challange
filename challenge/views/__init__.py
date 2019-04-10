
import logging
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

from tornado.concurrent import Future, chain_future
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler

from challenge.config import get_config
from challenge.exceptions import ERRORS_CHALLENGE

COUNT_CPU = multiprocessing.cpu_count()
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

    def _execute_ioloop(self, func, *args):
        """Execute method ioloop."""
        pool = ThreadPoolExecutor(max_workers=COUNT_CPU)
        old_future = pool.submit(func, *args)
        new_future = Future()
        IOLoop.current().add_future(old_future, lambda fut: chain_future(fut, new_future))
        return new_future

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
            result = await self._execute_ioloop(p_method, p_param)
            self.success(200, result)
        except ERRORS_CHALLENGE as error:
            logger.exception(str(error))
            self.error(400, str(error))
        except Exception as error:
            logger.exception(str(error))
            self.error(500, self._message_error_default)
