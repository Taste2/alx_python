'''
A script that lists all State objects from the database hbtn_0e_6_usa
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from model_state import State, Base
from sqlalchemy.orm import sessionmaker

# Create engine
DATABASE_URI = "mysql://root:St10285515"
engine = create_engine(DATABASE_URI)

state_obj = State
Base.metadata.create_all(bind=engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

states = session.query(state_obj).all()
for state in states:
    print(state.id, state.name)