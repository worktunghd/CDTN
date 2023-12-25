from sqlalchemy import Column, String, ForeignKey, DateTime, DECIMAL, Text
from sqlalchemy.orm import relationship
from .base import Base, BaseMixin
from sqlalchemy.dialects.mysql import INTEGER


# Bảng sản phẩm
class OrderDetail(Base, BaseMixin):
    __tablename__ = 'order_details'
    order_id = Column(INTEGER(unsigned=True), ForeignKey('orders.id', ondelete='CASCADE'))
    product_id = Column(INTEGER(unsigned=True), ForeignKey('products.id'))
    total_price = Column(DECIMAL(18, 0), default=0)
    # số lượng sản phẩm
    quantity_order = Column(INTEGER)
    # Mối quan hệ Many-to-One với Order
    order = relationship('Order', back_populates='order_details', single_parent=True)
    # Mối quan hệ Many-to-One với Product
    product = relationship('Product')
