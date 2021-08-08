#!/usr/bin/python3
"""Function select states"""
from sys import argv
import MySQLdb as mysql

if __name__ == '__main__':
    connection = mysql.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    database = connection.cursor()

    database.execute(
        "SELECT states.id, states.name FROM states ORDER BY states.id"
    )
    for column_sql in database:
        print(column_sql)