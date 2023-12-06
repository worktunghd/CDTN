from sqlalchemy import Column, String, ForeignKey, DateTime, DECIMAL, Text
from sqlalchemy.orm import relationship
from .base import Base, BaseMixin
from sqlalchemy.dialects.mysql import INTEGER


# Bảng sản phẩm
class Order(Base, BaseMixin):
    __tablename__ = 'orders'
    # mã đơn hàng
    order_code = Column(String(255), unique=True)
    user_id = Column(INTEGER(unsigned=True), ForeignKey('users.id'))
    # người đặt
    user = relationship('User', back_populates='orders')
    order_details = relationship('OrderDetail', back_populates='order')
    # tổng giá tiền
    price = Column(String(255))
    # ngày đặt hàng
    order_date = Column(DateTime(timezone=True))
    # số lượng sản phẩm
    quantity = Column(INTEGER)
    # trạng thái đơn hàng
    status = Column(INTEGER)
