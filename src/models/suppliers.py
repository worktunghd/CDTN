from sqlalchemy import Column, String, ForeignKey, DateTime, DECIMAL, Text
from sqlalchemy.orm import relationship
from .base import Base, BaseMixin
from sqlalchemy.dialects.mysql import INTEGER


# Bảng nhà cung cấp
class Suppliers(Base, BaseMixin):
    __tablename__ = 'Suppliers'
    # mã
    code = Column(String(255), unique=True)
    # tên nhà cung cấp
    supplier_name = Column(String(255))
    # số điện thoại
    phone_number = Column(String(255), nullable=True)
    # địa chỉ
    address = Column(String(255), nullable=True)
    products = relationship('Products', back_populates='supplier', cascade="all, delete-orphan")
    imports = relationship('PurchaseOrders', secondary='SupplierPurchaseOrders', back_populates='suppliers')
