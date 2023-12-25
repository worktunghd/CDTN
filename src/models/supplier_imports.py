from sqlalchemy import Column, String, ForeignKey, DateTime, DECIMAL, Text
from sqlalchemy.orm import relationship
from .base import Base, BaseMixin
from sqlalchemy.dialects.mysql import INTEGER


# Bảng chi tiết của 2 bảng supplier và import
class SupplierImport(Base, BaseMixin):
    __tablename__ = 'supplier_imports'
    supplier_id = Column(INTEGER(unsigned=True), ForeignKey('suppliers.id', ondelete='CASCADE'))
    import_id = Column(INTEGER(unsigned=True), ForeignKey('imports.id', ondelete='CASCADE'))

