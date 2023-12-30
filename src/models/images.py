from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER
from .base import Base, BaseMixin

# Bảng hình ảnh sản phẩm
class Images(Base, BaseMixin):
    __tablename__ = 'Images'
    image_url = Column(String(255))
    product_id = Column(INTEGER(unsigned=True), ForeignKey('Products.id', ondelete='CASCADE'))
    product = relationship('Products', back_populates='product_image', single_parent=True)
