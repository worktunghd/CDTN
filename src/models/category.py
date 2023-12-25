from sqlalchemy import Column, String
from .base import Base, BaseMixin
from sqlalchemy.orm import relationship


# Bảng loại sản phẩm
class Category(Base, BaseMixin):
    __tablename__ = 'categories'
    category_name = Column(String(255), unique=True)
    products = relationship('Product', back_populates='category', cascade="all, delete-orphan")

    def __eq__(self, other):
        if isinstance(other, Category):
            return self.category_name == other.category_name
        return False