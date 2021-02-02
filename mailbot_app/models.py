#!./env/bin/python3
## Database Access API
## Importing Own Libraries

## Importing Third Party Libraries
from dotenv import load_dotenv
import datetime
import sqlite3
from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime, Float, UniqueConstraint
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

# Set Database path (.env)
Database = declarative_base()

# Database Tables' Classes
# Clients
class Client(Database):
    __tablename__ = "client"
    cpf = Column(String, primary_key=True)
    # first_name = Column(String)
    name = Column(String)
    email = Column(String)
    mobile = Column(String)
    address = Column(String)
    
# Shipment
class Shipment(Database):
    shipment_id = Column(Integer, primary_key=True)
    method = Column(String, unique=True)
    price = Column(Float,default=0.00)

# Orders
class Order(Database):
    __tablename__ = "order"
    order_number = Column(Integer, primary_key=True)
    # first_name = Column(String)
    datetime = Column(DateTime, default=datetime.datetime.utcnow)
    shipment_method = Column(String, ForeignKey("shipment.method"))
    shipment_price = Column(Float)
    subtotal = Column(Float,default=0.00)
    items = Column(Float,default=0.00)

# Order Items
class OrderItems(Database):
    __tablename__ = "order_items"
    order_number = Column(String, ForeignKey("client.cpf"))
    item_id = Column(Integer,nullable=False)
    description = Column(String, default='')
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0.00)
    address = Column(String)
    UniqueConstraint("order_number", "item_id", name='uix_1')

