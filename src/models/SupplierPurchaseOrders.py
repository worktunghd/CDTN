from sqlalchemy import Column, String, ForeignKey, DateTime, DECIMAL, Text
from sqlalchemy.orm import relationship
from .base import Base, BaseMixin
from sqlalchemy.dialects.mysql import INTEGER


# Bảng chi tiết của 2 bảng Supplier và PurchaseOrders
class SupplierPurchaseOrders(Base, BaseMixin):
    __tablename__ = 'SupplierPurchaseOrders'
    supplier_id = Column(INTEGER(unsigned=True), ForeignKey('Suppliers.id', ondelete='CASCADE'))
    import_id = Column(INTEGER(unsigned=True), ForeignKey('PurchaseOrders.id', ondelete='CASCADE'))

