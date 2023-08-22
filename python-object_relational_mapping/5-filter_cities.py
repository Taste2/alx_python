'''
a script that takes in the name of a state as an
argument and lists all cities of that state,
using the database hbtn_0e_4_usa
'''
if __name__ == "__main__":
    import MySQLdb
    import sys
    

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_searched = sys.argv[4]
    
    # Connect to the database
    connector = MySQLdb.connect(user=user, passwd=password, db=database)

    # a cursor to manipulate the database
    db_cur = connector.cursor()
    db_cur.execute("SELECT cities.id, cities.name, state_searched.id \
                   FROM cities, state_searched \
                   WHERE states_id = state_searched.id ORDER BY cities.id")
    states_data = db_cur.fetchall()

    for data in states_data:
        print(data)
