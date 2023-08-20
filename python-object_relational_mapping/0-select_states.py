'''
This program lists all states from the database hbtn_0e_0_usa
'''
if __name__ == "__main__":
    import MySQLdb
    # Connect to the database
    connector = MySQLdb.connect(user='stephen', passwd='password', db='test_0')

    # a cursor to manipulate the database
    db_cur = connector.cursor()

    db_cur.execute("CREATE USER IF NOT EXISTS 'stephen'@'localhost'")
    db_cur.execute("SET PASSWORD FOR 'stephen'@'localhost' = 'password")
    db_cur.execute("GRANT ALL PRIVILEGES ON *.* TO 'stephen'@'localhost'")
    db_cur.execute("USE test_0")
    db_cur.execute("SELECT * FROM states")
    states_data = db_cur.fetchall()

    for data in states_data:
        print(data)
