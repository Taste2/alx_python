'''
A script that lists all State objects from the database hbtn_0e_6_usa
'''
if __name__ == "__main__":
    from model_state import State, Base
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    import sys

    path = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                         .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    engine = create_engine(path)
    connection = engine.connect()

    Session = sessionmaker(bind=engine)
    session = Session()
    for name in session.query(State).all():
        print(f"{id}: {name}")
