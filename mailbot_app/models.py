#!./env/bin/python3
## Database Access API
## Importing Own Libraries

## Importing Third Party Libraries
from dotenv import load_dotenv
import datetime
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, DateTime, Float, UniqueConstraint
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Load Environment Variables
# load_dotenv()
# TODO: Replace by Environment Variable DATA_BASE
engine = create_engine('sqlite:///database/database.db', echo=True)

# Database Object
Base = declarative_base()

# Get database connection Session() method
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

# Database Tables' Classes
# Clients
class Client(Base):
    __tablename__ = "client"
    cpf = Column(String, primary_key=True)
    # first_name = Column(String)
    name = Column(String)
    email = Column(String)
    mobile = Column(Integer)
    address = Column(String)
    # orders = relationship('Order', backref="client")
    
    def __repr__(self):
        return "<{}|{}|{}|{}>".format(self.cpf, self.name, self.email, self. mobile)

    # TODO: Treat database errors
    def add(self,session):
        try: 
            # Test Insert Client
            session.add(self)
            session.commit()
            session.close()
            return True
        except:
            session.rollback()
            return False
    
    def getClientByCPF(self,cpf):
        try: 
            # Test Insert Client
            session.add(self)
            session.commit()
            session.close()
            return True
        except:
            return False

# # Shipment
# class Shipment(Base):
#     __tablename__ = "shipment"
#     id = Column(Integer, primary_key=True)
#     method = Column(String, unique=True)
#     orders = relationship('Order', backref="shipment")

# Orders
class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True)
    # first_name = Column(String)
    datetime = Column(DateTime, default=datetime.datetime.utcnow)
    client = Column(String, ForeignKey("client.cpf"))
    shipment_method = Column(String)
    shipment_price = Column(Float)
    subtotal = Column(Float,default=0.00)
    items = relationship('OrderItems', backref="order")
    
    def __repr__(self):
        return "<{}|{}|{}|{}>".format(id, self.datetime, self.client)

    # TODO: Treat database errors
    def add(self,session):
        try: 
            # Test Insert Client
            session.add(self)
            session.commit()
            session.close()
            return True
        except:
            session.rollback()
            return False

# Order Items
class OrderItems(Base):
    __tablename__ = "order_items"
    order_number = Column(Integer, ForeignKey("order.id"), primary_key=True)
    item_id = Column(Integer, primary_key=True)
    description = Column(String, default='')
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0.00)
    address = Column(String)
    
    def __repr__(self):
        return "<{}|{}|{}|{}>".format(self.order_number, self.itenm_id, self.description)


    # TODO: Treat database errors
    def add(self,session):
        try: 
            # Test Insert Client
            session.add(self)
            session.commit()
            session.close()
            return True
        except:
            session.rollback()
            return False




