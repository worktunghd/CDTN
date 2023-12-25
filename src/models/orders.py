from sqlalchemy import Column, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from .base import Base, BaseMixin
from sqlalchemy.dialects.mysql import INTEGER


# Bảng sản phẩm
class Order(Base, BaseMixin):
    __tablename__ = 'orders'
    # mã đơn hàng
    order_code = Column(String(255), unique=True)
    customer_id = Column(INTEGER(unsigned=True), ForeignKey('customers.id', ondelete='CASCADE'))
    # người đặt
    customer = relationship('Customer', back_populates='orders', single_parent=True)
    order_details = relationship('OrderDetail', back_populates='order', cascade="all, delete-orphan")
    # tổng giá tiền
    original_price = Column(String(255))
    discount = Column(INTEGER, default=0)
    final_price = Column(String(255))
    # số lượng sản phẩm
    quantity = Column(INTEGER)
    # trạng thái đơn hàng
    status = Column(INTEGER)
