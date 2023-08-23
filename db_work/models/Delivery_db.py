from datetime import datetime

import pymysql
from sqlalchemy import  Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

from .Produkt_db import Product

pymysql.install_as_MySQLdb()
Base = declarative_base()

class Country(Base):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String(100), nullable=False)
    def __repr__(self):
        return self.country

class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(100), nullable=False)
    def __repr__(self):
        return self.city

class Street(Base):
    __tablename__ = 'street'
    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String(100), nullable=False)
    def __repr__(self):
        return self.street

class Delivery(Base):
    __tablename__ = 'delivery'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    tovar_id = Column(Integer, ForeignKey(Product.id))
    tovar = relationship(Product)
    quantity = Column(Integer, nullable=False)

    country_id = Column(Integer, ForeignKey(Country.id))
    country = relationship(Country)
    city_id = Column(Integer, ForeignKey(City.id))
    city = relationship(City)
    street_id = Column(Integer, ForeignKey(Street.id))
    street = relationship(Street)

    house = Column(String(10), nullable=False)
    number = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    user_name = Column(String(255), nullable=False)
    
    stat = Column(String(255), nullable=False)
    date = Column(DateTime, default=datetime.utcnow)




