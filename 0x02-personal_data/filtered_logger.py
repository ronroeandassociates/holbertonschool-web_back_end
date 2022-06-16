#!/usr/bin/env python3
"""
Write a function called filter_datum that returns the log message obfuscated:
"""

import re
import logging
import os
from typing import List
import mysql.connector


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Returns a connector to a secure database
    using server environmental vairables
    """
    env_username = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    env_password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    env_hostName = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    env_dbName = os.environ.get("PERSONAL_DATA_DB_NAME")
    connector = mysql.connector.connect(user=env_username,
                                        password=env_password,
                                        database=env_dbName,
                                        host=env_hostName)
    return connector


def get_logger() -> logging.Logger:
    """
    2 Create logger
    """

    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    stream = logging.StreamHandler()
    stream.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream)
    return logger


def filter_datum(fields: List[str], redaction: str, msg: str,
                 separator: str) -> str:
    """
    fields: list of strings representing all fields to obfuscate
    redaction: string representing by what the field will be obfuscated
    message: string representing the log line
    separator: string representing by which character is separating all
    fields in the log line (message)
    return: string representing the log line obfuscated
    """
    for fields in fields:
        pattern = r'(?<={}=).*?(?={})'.format(fields, separator)
        message = re.sub(pattern, redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: list):
        ''' Initialize the formatter with the fields to redact'''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        ''' Format the log message '''
        msg = super().format(record)
        logList = (filter_datum(self.fields, self.REDACTION,
                                msg, self.SEPARATOR))
        return logList.replace(";", "; ")
