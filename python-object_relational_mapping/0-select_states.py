'''
This program lists all states from the database hbtn_0e_0_usa
'''
import MySQLdb
if __name__ == "__main__":

    # Connect to the database
    connector = MySQLdb.connect(user='root', passwd='St10285515', db='test_0')

    # a cursor to manipulate the database
    db_cur = connector.cursor()

    db_cur.execute("USE test_0")
    db_cur.execute("SELECT name FROM states ORDER BY states.id")
