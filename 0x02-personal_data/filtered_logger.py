#!/usr/bin/env python3
"""
 PII_FIELDS - a list of fields to redact
 REDACTION - a string to replace the PII_FIELDS with
 """

from typing import List
import re
import logging
import os
import mysql.connector


PII_FIELDS = ("phone", "ssn", "password", "email", "name")


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
    """ Creates a logger with a StreamHandler"""
    log_obj = logging.getLogger("user_data")
    log_obj.setLevel(logging.INFO)
    log_obj.propagate = False
    stream = logging.StreamHandler()
    stream.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    log_obj.addHandler(stream)
    return log_obj


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Task 0"""
    for field in fields:
        pattern = f"(?<={field}=).+?(?={separator})"
        message = re.sub(pattern, redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    """def format(self, record: logging.LogRecord) -> str:
        Formatter = logging.Formatter(self.FORMAT)
        record = Formatter.format(record)
        return filter_datum(self.fields, self.REDACTION, str(record).replace(
            self.SEPARATOR, self.SEPARATOR + ' '), self.SEPARATOR)"""

    def format(self, record: logging.LogRecord) -> str:
        """[summary]"""
        Formatter = logging.Formatter(self.FORMAT)
        record = Formatter.format(record)
        return filter_datum(self.fields, self.REDACTION,
                            str(record), self.SEPARATOR)


if __name__ == '__main__':
    def main():
        """Summary"""
        db_connector = get_db()
        db_cursor = db_connector.cursor()
        query = ("SELECT * FROM users")
        db_cursor.execute(query)
        fields = [str(item[0]) for item in db_cursor.description]

        for result in db_cursor:
            string = ''
            for field_pos, item in enumerate(result):
                string = string + fields[field_pos] + '=' + str(item) + '; '
            logger = get_logger()
            logger.info(string)
    main()
