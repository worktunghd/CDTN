from sqlalchemy import Column, String, ForeignKey, DateTime, DECIMAL, Text
from sqlalchemy.orm import relationship
from .base import Base, BaseMixin
from sqlalchemy.dialects.mysql import INTEGER


# Bảng nhà cung cấp
class Supplier(Base, BaseMixin):
    __tablename__ = 'suppliers'
    # mã
    code = Column(String(255), unique=True)
    # tên nhà cung cấp
    name = Column(String(255))
    # số điện thoại
    phone = Column(String(255), nullable=True)
    # địa chỉ
    address = Column(String(255), nullable=True)
    products = relationship('Product', back_populates='supplier', cascade="all, delete-orphan")
    imports = relationship('Import', secondary='supplier_imports', back_populates='suppliers')
