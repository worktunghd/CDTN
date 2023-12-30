from sqlalchemy import Column, String, DECIMAL, ForeignKey
from .base import Base, BaseMixin
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER


# Hạng khách hàng
class CustomerCategories(Base, BaseMixin):
    __tablename__ = 'CustomerCategories'
    category_name = Column(String(255))
    code = Column(String(255), unique=True)
    min_spending = Column(DECIMAL(18, 0), default=0)
    discount_percentage = Column(String(255))
    customers = relationship('Customers', back_populates='customer_categories')
