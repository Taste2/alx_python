'''
Write a script that takes in an argument and displays all 
values in the states table of hbtn_0e_0_usa 
where name matches the argument.
'''
if __name__ == "__main__":
    import MySQLdb

    # Connect to the database
    connector = MySQLdb.connect(user='root', passwd='St10285515', db='test_2')

    # a cursor to manipulate the database
    db_cur = connector.cursor()

    db_cur.execute("USE test_2")
    searched_state = input("Enter any State: ")
    query = "SELECT * FROM states \
                   WHERE name COLLATE utf8mb4_bin LIKE '{}%'".format(searched_state)
    db_cur.execute(query)
    states_data = db_cur.fetchall()

    for data in states_data:
        print(data)
