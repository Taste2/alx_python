'''
This module is a python file that contains the class definition of a
State and an instance Base = declarative_base():

class:
State: Model of the table states which inherits from Base
 attr:
    id: unigue id of each state
    name: names of the states
'''

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create engine
DATABASE_URI = "mysql://root:St10285515"
engine = create_engine(DATABASE_URI)

# Base class
Base = declarative_base
'''
A base class that serves as the foundation for defining
database models (tables) using the
Object-Relational Mapping (ORM) approach.
'''

# A class to create the tables
class State(Base):
    '''
    A class that models the table 'states', inherited from Base

    Attributes:

        id(int): unique identity number of each state
    
        name(string): name of each state
    '''
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(bind=engine)
