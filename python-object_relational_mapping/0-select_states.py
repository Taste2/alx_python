'''
This program lists all states from the database hbtn_0e_0_usa
'''

import MySQLdb

#Connect to the database
connector = MySQLdb.connect(user='root', passwd='St10285515', db='hbtn_0e_0_usa')

# a cursor to manipulate the database
db_cur = connector.cursor()

db_cur.execute("USE hbtn_0e_usa")
db_cur.execute("SELECT name FROM states ORDER BY states.id")