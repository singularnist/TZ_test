from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin

Base = declarative_base()
class AdminUser(Base, UserMixin):
    __tablename__ = 'adminuser'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)

    def __repr__(self):
        return '<adminsser %r>' % self.id

    def verify_password(self, password):
        return password == self.password_hash