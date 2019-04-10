import importlib
import logging
import logging.config
import os


class ConfigDefault:
    """Class with default settings"""
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    URL_S3_ZAP = os.environ.get(
        "URL_S3_ZAP",
        "http://grupozap-code-challenge.s3-website-us-east-1.amazonaws.com/sources/source-2.json")
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    AMOUNT_PROCESS = os.environ.get('AMOUNT_PROCESS', 1)
    PORT_SERVER = os.environ.get('PORT_SERVER', 8889)
    APPLICATION_ENV = os.environ.get('APPLICATION_ENV', 'Homol')
    PROPAGATE_LOG = os.environ.get('PROPAGATE_LOG', False)
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%s'
            },
            'json': {
                'class': 'challenge.config.formatter_json.JsonFormatter',
                'datefmt': "%Y-%m-%d %H:%M:%S"
            },

        },
        'handlers': {

            'integration_handler': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'json',
            },
            'dev_null': {
                'class': 'logging.NullHandler'
            }
        },
        'loggers': {

            '': {
                'level': LOG_LEVEL,
                'handlers': ['integration_handler'],
                'propagate': PROPAGATE_LOG,
            },

        },

    }


class TestingConfig(ConfigDefault):
    """Settings tests"""
    LOG_LEVEL = logging.CRITICAL


class HomolConfig(ConfigDefault):
    """Homol Settings"""
    LOG_LEVEL = logging.INFO


class ProductionConfig(ConfigDefault):
    """Production Settings"""
    LOGS_LEVEL = logging.ERROR
    URL_MODULE_ADMINISTRATIVE = os.environ.get("URL_MODULE_ADMINISTRATIVE")


def get_config():
    """Create object the of enviroment choiced"""
    config_var = os.getenv('APPLICATION_ENV', 'Homol')
    enviroment = "{}Config".format(config_var)
    config_challenge = getattr(importlib.import_module("challenge.config"), enviroment)
    logging.config.dictConfig(config_challenge.LOGGING)
    return config_challenge
