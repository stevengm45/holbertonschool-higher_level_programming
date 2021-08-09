#!/usr/bin/python3
""" function that filter states"""


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

    syntax = 'SELECT states.id, states.name FROM states WHERE\
    states.name = \'{:s}\' ORDER BY states.id'.format(argv[4])
    database.execute(syntax)

    for column_sql in database:
        if (column_sql[1] == argv[4]):
            print(column_sql)
