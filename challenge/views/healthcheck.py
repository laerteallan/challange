
import logging

from challenge.config import get_config
from challenge.views import ApiJsonHandler

config_challenge = get_config()

logger = logging.getLogger(__name__)


class HealthcheckApi(ApiJsonHandler):
    __urls__ = ['/healthcheck']

    async def get(self):
        data = {
            'status': 'ok',
        }

        logger.info('response healthcheck {}'.format(data))
        self.success(200, data)
