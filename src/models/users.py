from sqlalchemy import Column, String, INTEGER
from .base import Base, BaseMixin
from sqlalchemy.orm import relationship
from src.enums.enums import UserRole

class User(Base, BaseMixin):
    __tablename__ = 'users'
    username = Column(String(255), unique=True)
    name = Column(String(255))
    password = Column(String(255))
    level = Column(INTEGER, default=UserRole.EMPLOYEE.value)
