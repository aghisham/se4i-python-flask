"""Init App"""
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import app.config as conf


app = FastAPI(
    title=conf.APP_NAME,
    version=conf.APP_VERSION,
    description=conf.APP_DESCRIPTION,
    debug=conf.DEBUG,
)

engine = create_engine(url=conf.SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


from app.controllers import *
