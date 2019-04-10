import datetime
import json
import logging
import socket


class JsonFormatter(logging.Formatter):
    """
    Format logs for send to StackDriver.
    exmple to use:
    logger.info('sent to log stack', extra={'msisdn': msisdn, 'carrier': 'carrier'})
    """

    def format(self, record):
        super(JsonFormatter, self).format(record)
        data = {
            'level': record.levelname,
            'date': datetime.datetime.fromtimestamp(record.created).strftime("%Y-%m-%d %H:%M:%S.%f"),
            'file': record.pathname,
            'server': socket.gethostname(),
            'name': record.name,
            'line': record.lineno,
            'message': record.msg,
            'exception': record.exc_text,
            'pid': record.process,
            'function': record.funcName,
        }
        return json.dumps(data)
