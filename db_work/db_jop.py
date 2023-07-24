from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Country, City, Street, Product,Delivery, AdminUser, Base
import pymysql

pymysql.install_as_MySQLdb()
user = 'user_shop'
password = 'user_shop'
database = 'new_test'
host = '172.20.0.2'  # IP-адреса контейнера MySQL
port = '3306'  # Порт MySQL


db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"


engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session_1 = Session()


# Base.metadata.create_all(engine)