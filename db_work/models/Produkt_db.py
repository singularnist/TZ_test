from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL, DateTime
from datetime import datetime


Base = declarative_base()
class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    title = Column(String(255), nullable=False)
    price = Column(DECIMAL(10, 2),nullable=False)
    color = Column(String(50),nullable=False)
    weight = Column(DECIMAL(10, 2),nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<product %r>' % self.id
