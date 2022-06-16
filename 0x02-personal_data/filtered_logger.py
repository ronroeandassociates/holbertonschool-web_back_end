#!/usr/bin/env python3
"""
0 Regex-ing
Write a function called filter_datum that returns the log message obfuscated:
"""

import re
import logging
from typing import list
import mysql.connector
from os import environ

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')
"""
1 Log formatter
"""


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: list):
        ''' Initialize the formatter with the fields to redact'''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        ''' Format the log message '''
        msg = super().format(record)
        return filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str, separator: str)->str:
    """
    fields: list of strings representing all fields to obfuscate
    return: string representing the log line obfuscated
    """
    for fields in fields:
        regexString = f"(?<={fields}=).*?(?={separator})"
        message = re.sub(regexString, redaction, message)
    return message


def get_logger() -> logging.Logger:
    """
    2 Create logger
    """

    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    formatter = RedactingFormatter(PII_FIELDS)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.propagate = False
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    3 Create database connection
    Connect to a secure holberton database to read a users table.
    The database is protected by a username and password that are
    stored in environment variables
    """
    db = mysql.connector.connect(
        db_user = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
        db_passwd = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
        db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
        database = os.getenv('PERSONAL_DATA_DB_NAME', 'personal_data')
    return db


def main():
    """Connects to db, gets info, and displays it"""
    logger = get_logger()
    db = get_db()

    # create cursor, execute queries in all rows
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")

    for row in cursor:
        # list of tuples
        tupleList = row.items()
        # transform to list of strings with PII_FIELDS
        str = "; ".join(f"{tuple[0]}={tuple[1]}" for tuple in tupleList)
        logger.info(str)

    db.close()


if __name__ == "__main__":
    main()
