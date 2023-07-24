from sqlalchemy import ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, DECIMAL, DateTime
from datetime import datetime
import pymysql

pymysql.install_as_MySQLdb()
Base = declarative_base()
class Country(Base):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String(255), nullable=False)
    def __repr__(self):
        return '<country %r>' % self.id

class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(255), nullable=False)
    def __repr__(self):
        return '<city %r>' % self.id

class Street(Base):
    __tablename__ = 'street'
    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String(255), nullable=False)
    def __repr__(self):
        return '<sity %r>' % self.id

class Delivery(Base):
    __tablename__ = 'delivery'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    quantity = Column(Integer, nullable=False)
    country_id = Column(Integer, ForeignKey('country.id'), nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    street_id = Column(Integer, ForeignKey('street.id'), nullable=False)
    house = Column(String(10), nullable=False)
    number = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    user_name = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    color = Column(String(255), nullable=False)
    weight = Column(DECIMAL(10, 2), nullable=False)
    price = Column(DECIMAL, nullable=False)
    stat = Column(String(255), nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

    # Встановлюємо зв'язок між екземплярами класів, а не ID
    country = relationship("Country", foreign_keys=[country_id])
    city = relationship("City", foreign_keys=[city_id])
    street = relationship("Street", foreign_keys=[street_id])
