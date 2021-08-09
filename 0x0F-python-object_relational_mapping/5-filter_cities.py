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

    query = 'SELECT cities.name FROM cities JOIN states\
    ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id'
    database.execute(query, (state, ))

    result = [i[0] for i in database]
    print(', '.join(result))
