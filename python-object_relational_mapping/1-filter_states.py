'''
Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
'''
if __name__ == "__main__":
    import MySQLdb
    # Connect to the database
    connector = MySQLdb.connect(user='root', passwd='St10285515', db='test_1')

    # a cursor to manipulate the database
    db_cur = connector.cursor()

    db_cur.execute("USE test_1")
    db_cur.execute("SELECT * FROM states WHERE UPPER(name) LIKE 'N%'")
    states_data = db_cur.fetchall()

    for data in states_data:
        print(data)
