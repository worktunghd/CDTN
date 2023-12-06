from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER
from .base import Base, BaseMixin

# Bảng hình ảnh sản phẩm
class Image(Base, BaseMixin):
    __tablename__ = 'images'
    image_url = Column(String(255))
    product_id = Column(INTEGER(unsigned=True), ForeignKey('products.id'))
    product = relationship('Product', back_populates='product_image')
