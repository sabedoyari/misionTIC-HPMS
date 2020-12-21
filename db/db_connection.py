from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_url = "postgresql://user:password@host:port/name_db"
engine = create_engine(database_url)