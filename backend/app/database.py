import os

import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def get_db_url():
    drivername = os.environ['DRIVER_NAME']
    username = os.environ['DB_USER']
    password = os.environ['DB_PASSWORD']
    host = os.environ['DB_HOST']
    port = os.environ['DB_PORT']
    dbname = os.environ['DB_NAME']

    password = urllib.parse.quote(password, safe="")
    url = '{}://{}:{}@{}:{}/{}'.format(drivername, username, password, host, port, dbname)

    return url


engine = create_engine(get_db_url(), encoding='utf-8')



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
