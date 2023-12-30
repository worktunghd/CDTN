from sqlalchemy import Column, String, INTEGER
from .base import Base, BaseMixin
from sqlalchemy.orm import relationship
from src.enums.enums import UserRole

class Employees(Base, BaseMixin):
    __tablename__ = 'Employees'
    username = Column(String(255), unique=True)
    citizen_id = Column(String(255), unique=True, nullable=True)
    employee_name = Column(String(255))
    password = Column(String(255))
    role = Column(INTEGER, default=UserRole.EMPLOYEE.value)
