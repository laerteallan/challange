import importlib
import inspect
import logging
import pkgutil

import tornado.escape
import tornado.ioloop
import tornado.web
from tornado.httpserver import HTTPServer
from tornado.web import Application

from challenge.config import get_config
from challenge.exceptions import ErrorStartTornado

config_challenge = get_config()
log = logging.getLogger(__file__)


class Server:

    def __init__(self, port=8889, base_config={}, instances=1, type_start="developer"):
        self.__port = int(port)
        self.__base_config = base_config
        self.__instance = int(instances)
        self.__type_start = type_start

    @staticmethod
    def __gen_submodule_names(package):
        for item in pkgutil.walk_packages(
                path=package.__path__,
                prefix=package.__name__ + '.',
                onerror=lambda x: None):
            modname = item[1]
            yield modname

    @staticmethod
    def __prepare_url(module, routes):
        for item in inspect.getmembers(module, inspect.isclass):
            module_search = item[0]
            if "__urls__" in vars(getattr(module, module_search)):
                module_real = getattr(module, module_search)
                for url in module_real.__urls__:
                    routes.append((url, module_real))

        return routes

    def __get_urls(self, views):
        routes = []
        gen = self.__gen_submodule_names(views)
        for sub_modules in gen:
            module = importlib.import_module(sub_modules)
            routes = self.__prepare_url(module, routes)

        return routes

    def make_app(self, views):
        routes = self.__get_urls(views)
        self.__base_config.update({"compress_response": True})
        app = Application(routes, **self.__base_config)
        return app

    def start(self, views):
        try:
            log.info("starting server")
            app = self.make_app(views)
            server = HTTPServer(app)
            server.bind(self.__port)
            server.start(self.__instance)
            tornado.ioloop.IOLoop.instance().start()
        except Exception as error:
            log.exception(str(error), exc_info=True)
            raise ErrorStartTornado(str(error))
