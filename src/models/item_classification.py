from sqlalchemy import Column, String, ForeignKey, DateTime, DECIMAL, Text
from sqlalchemy.orm import relationship
from .base import Base, BaseMixin
from sqlalchemy.dialects.mysql import INTEGER


# Bảng phân loại hàng
class ItemClassification(Base, BaseMixin):
    __tablename__ = 'item_classifications'
    # tên phân loại
    item_classification_name = Column(String(255), unique=True)
    product_id = Column(INTEGER(unsigned=True), ForeignKey('Products.id'))
    product = relationship('Products', back_populates='item_classification')
    sub_item_classifications = relationship('SubItemClassification', back_populates='item_classification')

