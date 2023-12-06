from sqlalchemy import Column, String
from .base import Base, BaseMixin
from sqlalchemy.orm import relationship


# Bảng loại sản phẩm
class Category(Base, BaseMixin):
    __tablename__ = 'categories'
    category_name = Column(String(255), unique=True)
    product = relationship('Product', back_populates='category')
