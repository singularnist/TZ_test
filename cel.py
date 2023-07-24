from celery import Celery
import logging
from db_work.models.Delivery_db import Delivery
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pymysql

pymysql.install_as_MySQLdb()
app = Celery('cel', broker='redis://my_redis_container:6379/0', backend='redis://my_redis_container:6379/0')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('celery.log')
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)

@app.task
def compare_values(x, y):
    user = 'user_shop'
    password = 'user_shop'
    database = 'new_test'
    host = '172.20.0.2'  # IP-адреса контейнера MySQL
    port = '3306'
    db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    orders = session.query(Delivery).get(x)
    db_status = orders.stat
    print(db_status)
    if y != db_status:
        logger.info(f'Замовлення {x} змінило статус {db_status}')
        print(f'Замовлення {x} змінило статус {db_status}')
        return db_status  # Повернути статус
    else:
        compare_values.apply_async(args=[x, y], countdown=30)
if __name__=='__main__':
    app.start()