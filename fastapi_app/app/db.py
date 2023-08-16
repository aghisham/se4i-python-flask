"""Init DB"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import app.config as conf


Base = declarative_base()
engine = create_engine(url=conf.SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
DB = SessionLocal()
