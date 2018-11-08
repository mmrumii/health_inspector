import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask_login import UserMixin

Base = declarative_base()

class User(UserMixin, Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(50), nullable = False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(80), unique=False)
    username = Column(String(50), unique=True)
    phone = Column(String(50), unique=True)
    password = Column(String(80), nullable=False)


#Always stay at the end of the file
engine = create_engine('sqlite:///health.db')
Base.metadata.create_all(engine)

