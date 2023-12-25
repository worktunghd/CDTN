from sqlalchemy import Column, String, ForeignKey, DateTime, DECIMAL, Text
from sqlalchemy.orm import relationship
from .base import Base, BaseMixin
from sqlalchemy.dialects.mysql import INTEGER


# Bảng con phân loại hàng
class SubItemClassification(Base, BaseMixin):
    __tablename__ = 'sub_item_classifications'
    # tên phân loại
    sub_item_classification_name = Column(String(255))
    # số lượng
    quantity = Column(INTEGER)
    # giá
    price = Column(DECIMAL(18, 0))
    # ảnh
    image_url = Column(String(255))
    # id mã phân loại
    item_classification_id = Column(INTEGER(unsigned=True), ForeignKey('item_classifications.id'))
    item_classification = relationship('ItemClassification', back_populates='sub_item_classifications')

