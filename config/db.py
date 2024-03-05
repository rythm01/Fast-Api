from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote
from sqlalchemy.orm import sessionmaker

# Original password: Ridham@693#
encoded_password = quote("Ridham@693#")

DATABASE_URL = f"mysql://root:{encoded_password}@localhost:3306/sample"

engine = create_engine(DATABASE_URL, pool_pre_ping=True, pool_recycle=3600)
meta = MetaData()
conn = engine.connect()

#Base = declarative_base(metadata=meta)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    import models  # Import the module where your tables are defined
    meta.create_all(bind=engine)
