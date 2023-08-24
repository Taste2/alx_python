'''
A script that lists all State objects from the database hbtn_0e_6_usa
'''
from model_state import State, Base
from sqlalchemy.orm import sessionmaker

for id, name in session.query(State.id, State.name):
    print(f"{id}: {name}")