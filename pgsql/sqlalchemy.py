__author__ = 'neuraxis'
import sqlalchemy
from sqlalchemy import create_engine

#from sqlalchemy.ext.declarative import *

#Create a  DBAPI connection

engine = sqlalchemy.create_engine('postgresql://postgres:M4lh4v0C@192.168.0.103:5432/raspy')

#Declare an instance of the Base class for mapping tables

Base = declarative_base()

#Map a table to a class by inheriting base class

class Customer(Base):

     __tablename__ = 'customer'

     id = Column(Integer, primary_key=True)
     name = Column(String(1000), nullable=False)
     email = Column(String, unique=True)

     def __init__(self, name, email):
       self.name = name
       self.email = email

#Create the table using the metadata attribute of the base class
Base.metadata.create_all(engine)

"""SQLAlchemy SESSIONS

Sessions give you access to Transactions, whereby on success  you can commit the transaction or rollback one incase you encounter an error """

Session = sessionmaker(bind=engine)
session = Session()

#Insert multiple data in this session, similarly you can delete
customer = Customer(name='Linux', email='linux@example.com')
customer2=Customer(name='Python', email='python@example.com')

session.add(customer)
session.add(customer2)

try:
 session.commit()
#You can catch exceptions with  SQLAlchemyError base class
except SQLAlchemyError as e:
 session.rollback()
 print (str(e))

#Get data
for customer in session.query(Customer).all():
  print ("name of the customer is" ,customer.name)
  print ("email id of the customer is" ,customer.email)

#Close the connection
engine.dispose()