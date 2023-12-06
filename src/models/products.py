from sqlalchemy import Column, String, ForeignKey, DateTime, DECIMAL, Text
from sqlalchemy.orm import relationship
from .base import Base, BaseMixin
from sqlalchemy.dialects.mysql import INTEGER


# Bảng sản phẩm
class Product(Base, BaseMixin):
    __tablename__ = 'products'
    product_name = Column(String(255))
    # mã sản phẩm
    product_code = Column(String(255), unique=True)
    # ảnh sản phẩm
    product_image = relationship('Image', back_populates='product')
    # khuyến mãi
    promotion_price = Column(DECIMAL(18, 0), default=0)
    # loại sản phẩm
    category_id = Column(INTEGER(unsigned=True), ForeignKey('categories.id'))
    category = relationship('Category', back_populates='product')
    # mã phân loại sản phẩm
    item_classification = relationship('ItemClassification', back_populates='product')
    # ngày sản xuất
    manufacture_date = Column(DateTime(timezone=True))
    # giá
    price = Column(String(255))
    # số lượng
    quantity = Column(INTEGER)
    # mô tả
    description = Column(Text)
