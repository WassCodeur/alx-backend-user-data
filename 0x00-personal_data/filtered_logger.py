#!/usr/bin/env python3
"""personal data"""
import logging
import re
from typing import List


PII_FIELDS = ("name", "phone", "ssn", "password", "ip")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """log message obfuscated

    Arguments
    ---------
    fields: List
    redaction: str
    message: str
    separator: str

    Return
    ------
    """
    for field in fields:
        pattern = f"{field}=.*?{separator}"
        message = re.sub(pattern, f"{field}={redaction}{separator}", message)
    return message


def get_logger() -> logging.Logger:
    """get logger

    Arguments
    ---------
    None

    Return
    ------
    logging.logger
    """
    logger = logging.getLogger('user_data')
    logger.propagate = False
    logger.setLevel(logging.INFO)
    h = logging.StreamHandler()
    h.setFormatter(RedactingFormatter())
    logger.addHandler(h)

    return logger


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format a given record

        Arguments
        ---------
        record: logging.LogRecord

        Return
        ------
        str
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
