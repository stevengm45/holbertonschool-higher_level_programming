#!/usr/bin/python3
""" function that filter states"""


from sys import argv
import MySQLdb as mysql

if __name__ == '__main__':
    state = argv[4]

    connection = mysql.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    database = connection.cursor()

    syntax = 'SELECT states.id, states.name FROM states WHERE\
    states.name = %s ORDER BY states.id'
    database.execute(syntax, (state, ))

    for column_sql in database:
        print(column_sql)
