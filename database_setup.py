import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask_login import UserMixin

Base = declarative_base()


class Users(UserMixin, Base):
    __tablename__ = 'Users'

    UserIDNumber = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    FullName = Column(String(50), nullable=False)
    UserType = Column(String(10), nullable=False)
    EmailAddress = Column(String(80), unique=False)
    Username = Column(String(50), unique=True)
    Password = Column(String(80), nullable=False)

    def get_id(self):
        return self.UserIDNumber

#Always stay at the end of the file
engine = create_engine('sqlite:///health.db')
Base.metadata.create_all(engine)

