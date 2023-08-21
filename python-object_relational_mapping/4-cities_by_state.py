'''
Write a script that lists all cities from the database hbtn_0e_4_usa
'''
if __name__ == "__main__":
    import MySQLdb
    # Connect to the database
    connector = MySQLdb.connect(user='root', passwd='St10285515', db='test_4')

    # a cursor to manipulate the database
    db_cur = connector.cursor()
    db_cur.execute("SELECT cities.id, cities.name, states.name \
                   FROM cities, states \
                   WHERE states.id = state_id ORDER BY cities.id")
    states_data = db_cur.fetchall()

    for data in states_data:
        print(data)
