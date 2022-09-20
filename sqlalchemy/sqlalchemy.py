from sqlalchemy import declarative_base
from sqlalchemy import Column, String,DataTime,Integer,create_engine
from  datetime import datetime
import os

Base_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = "sqlite:///" + os.path.join(Base_DIR, 'ourDb.db')

Base = declarative_base()

engine = create_engine(connection_string, echo = True)

class User(Base):
	__tablename__ = users
	id = Column(Integer(), primary_key=True)
	Username = Column(String)
	fullname = Column(String)
	nickname = Column(String)
	datetime = Column(DateTime(), default=datetime.utcnow)

newUser = User(id =1, Username = "stephen", fullname = "stephen Kihuni", nickname = "stevo")
print(newUser)
