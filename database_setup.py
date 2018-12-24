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

class Service(Base):
    __tablename__ = 'Service'

    ServiceID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ServiceName = Column(String(100), nullable=False)
    Location = Column(String(20), nullable=False)
    DetailsLocation = Column(String(100), nullable=False)
    HospitalName = Column(String(100), nullable=False)
    Price = Column(Integer, nullable=True)
    Phone = Column(String(20), nullable=True)
    ServiceOwner = Column(Integer, ForeignKey(Users.UserIDNumber))
    Users = relationship(Users)


class Comment(Base):
    __tablename__ = 'Comment'

    CommentID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    CommentText = Column(String(500), nullable=False)
    ServiceID = Column(Integer, ForeignKey(Service.ServiceID))
    Service = relationship(Service)
    UserIDNumber = Column(Integer,ForeignKey(Users.UserIDNumber))
    Users = relationship(Users)



#Always stay at the end of the file
engine = create_engine('sqlite:///health.db')
Base.metadata.create_all(engine)
