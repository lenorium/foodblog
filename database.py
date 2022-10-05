from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import os


class DbInstance:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DbInstance, cls).__new__(cls)

            db_url = 'sqlite:///' + os.getenv('db_name')
            cls._instance.engine = create_engine(db_url, echo=bool(os.getenv('db_log')))
            cls._instance.session_maker = sessionmaker(bind=cls._instance.engine)
            Base.metadata.create_all(cls._instance.engine)
        return cls._instance
