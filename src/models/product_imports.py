from sqlalchemy import Column, String, ForeignKey, DateTime, DECIMAL, Text
from sqlalchemy.orm import relationship
from .base import Base, BaseMixin
from sqlalchemy.dialects.mysql import INTEGER


# Bảng chi tiết của 2 bảng supplier và import
class ProductImport(Base, BaseMixin):
    __tablename__ = 'product_imports'
    product_id = Column(INTEGER(unsigned=True), ForeignKey('products.id', ondelete='CASCADE'))
    import_id = Column(INTEGER(unsigned=True), ForeignKey('imports.id', ondelete='CASCADE'))

