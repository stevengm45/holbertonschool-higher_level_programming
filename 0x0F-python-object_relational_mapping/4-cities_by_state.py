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

    syntax = 'SELECT cities.id, cities.name, states.name FROM cities JOIN\
    states ON cities.state_id = states.id ORDER BY cities.id'
    database.execute(syntax)

    for column_sql in database:
        print(column_sql)
