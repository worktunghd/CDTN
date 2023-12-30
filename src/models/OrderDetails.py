from sqlalchemy import Column, String, ForeignKey, DateTime, DECIMAL, Text
from sqlalchemy.orm import relationship
from .base import Base, BaseMixin
from sqlalchemy.dialects.mysql import INTEGER


# Bảng sản phẩm
class OrderDetails(Base, BaseMixin):
    __tablename__ = 'OrderDetails'
    order_id = Column(INTEGER(unsigned=True), ForeignKey('Orders.id', ondelete='CASCADE'))
    product_id = Column(INTEGER(unsigned=True), ForeignKey('Products.id'))
    total_with_discount = Column(DECIMAL(18, 0), default=0)
    # số lượng sản phẩm
    quantity = Column(INTEGER)
    # Mối quan hệ Many-to-One với Order
    order = relationship('Orders', back_populates='order_details', single_parent=True)
    # Mối quan hệ Many-to-One với Product
    product = relationship('Products')
