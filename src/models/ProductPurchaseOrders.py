from sqlalchemy import Column, String, ForeignKey, DateTime, DECIMAL, Text
from sqlalchemy.orm import relationship
from .base import Base, BaseMixin
from sqlalchemy.dialects.mysql import INTEGER


# Bảng chi tiết của 2 bảng supplier và import
class ProductPurchaseOrders(Base, BaseMixin):
    __tablename__ = 'ProductPurchaseOrders'
    product_id = Column(INTEGER(unsigned=True), ForeignKey('Products.id', ondelete='CASCADE'))
    import_id = Column(INTEGER(unsigned=True), ForeignKey('PurchaseOrders.id', ondelete='CASCADE'))

