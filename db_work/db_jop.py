import os

import pymysql
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import AdminUser, Base, City, Country, Delivery, Product, Street

pymysql.install_as_MySQLdb()
load_dotenv()

db_url = f"mysql+pymysql://{os.getenv('USER_DB')}:{os.getenv('PASS_DB')}@{os.getenv('HOST')}:{os.getenv('PORT')}/{os.getenv('TZ_DB')}"


engine = create_engine(db_url)

Session = sessionmaker(bind=engine)

session_1 = Session()


# Base.metadata.create_all(engine)
