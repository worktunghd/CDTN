from sqlalchemy import Column, String, ForeignKey, DateTime, DECIMAL, Text
from sqlalchemy.orm import relationship
from .base import Base, BaseMixin
from sqlalchemy.dialects.mysql import INTEGER


# Bảng sản phẩm
class OrderDetail(Base, BaseMixin):
    __tablename__ = 'order_details'
    order_id = Column(INTEGER(unsigned=True), ForeignKey('orders.id'))
    product_id = Column(INTEGER(unsigned=True), ForeignKey('products.id'))
    # Mối quan hệ Many-to-One với Order
    order = relationship('Order', back_populates='order_details')
    # Mối quan hệ Many-to-One với Product
    product = relationship('Product')
