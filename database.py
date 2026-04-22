from sqlalchemy import create_engine
from models import Base, User, Task

engine = create_engine("sqlite:///todo.db", echo=True)
#Creates an engine (an sql file - todo.db) in which the databases will be stored

def create_db():
    Base.metadata.create_all(engine)
    #Creates the databases of the Task and User classes and transfers them into todo.db

if __name__ == "__main__":
    create_db()