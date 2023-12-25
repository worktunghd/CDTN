from sqlalchemy import Column, String, ForeignKey, DateTime, DECIMAL, Text
from sqlalchemy.orm import relationship
from .base import Base, BaseMixin
from sqlalchemy.dialects.mysql import INTEGER


# Bảng nhập hàng
class Import(Base, BaseMixin):
    __tablename__ = 'imports'
    # mã
    code = Column(String(255), unique=True)
    suppliers = relationship('Supplier', secondary='supplier_imports', back_populates='imports')
    products = relationship('Product', secondary='product_imports', back_populates='imports')
    # ngày nhập
    import_date = Column(DateTime(timezone=True))
    # ngày giao
    delivery_date = Column(DateTime(timezone=True))
    # số lượng
    quantity = Column(INTEGER)
    # thành tiền
    price = Column(String(255))
    # chiết khấu
    discount = Column(INTEGER, default=0)
    # thuế vat
    vat = Column(INTEGER, default=0)
    # tiền trước thuế
    original_price = Column(String(255))
    # tổng tiền
    final_price = Column(String(255))
    # trạng thái
    status = Column(INTEGER, default=0)
    description = Column(String(255), nullable=True)