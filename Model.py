import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "frontend_users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=True, index=True)
    last_name = Column(String, nullable=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False, index=True)
    phone = Column(Integer, nullable=False, index=True)
    fuid = Column(String, nullable=False, index=True)
    created_at = Column(DateTime, index=True, default=datetime.datetime.now())
    updated_at = Column(DateTime, index=True, default=datetime.datetime.now())
    status = Column(Integer, index=True, nullable=False,default=1)


# class LoginModel(Base):
#     __tablename__="login_user_tokens"
    