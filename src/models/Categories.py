from sqlalchemy import Column, String, ForeignKey
from .base import Base, BaseMixin
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER


# Bảng loại sản phẩm
class Categories(Base, BaseMixin):
    __tablename__ = 'Categories'
    category_name = Column(String(255), unique=True)
    products = relationship('Products', back_populates='category', cascade="all, delete-orphan")

    def __eq__(self, other):
        if isinstance(other, Categories):
            return self.category_name == other.category_name
        return False