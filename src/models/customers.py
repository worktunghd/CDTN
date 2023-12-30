from sqlalchemy import Column, String, DECIMAL, ForeignKey
from .base import Base, BaseMixin
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER

class Customers(Base, BaseMixin):
    __tablename__ = 'Customers'
    customer_name = Column(String(255), unique=True)
    phone_number = Column(String(255))
    total_spending = Column(DECIMAL(30, 0), default=0)
    customer_category_id = Column(INTEGER(unsigned=True), ForeignKey('CustomerCategories.id'))
    customer_categories = relationship('CustomerCategories', back_populates='customers')
    orders = relationship('Orders', back_populates='customer', cascade="all, delete-orphan")

