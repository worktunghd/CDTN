from sqlalchemy import Column, String, ForeignKey, DateTime, DECIMAL, Text
from sqlalchemy.orm import relationship
from .base import Base, BaseMixin
from sqlalchemy.dialects.mysql import INTEGER


# Bảng sản phẩm
class Products(Base, BaseMixin):
    __tablename__ = 'Products'
    product_name = Column(String(255))
    # mã sản phẩm
    product_code = Column(String(255), unique=True)
    # ảnh sản phẩm
    product_image = relationship('Images', back_populates='product', cascade="all, delete-orphan")
    # khuyến mãi
    promotion_price = Column(DECIMAL(18, 0), default=0)
    # loại sản phẩm
    category_id = Column(INTEGER(unsigned=True), ForeignKey('Categories.id', ondelete='CASCADE'))
    category = relationship('Categories', back_populates='products', single_parent=True)
    supplier_id = Column(INTEGER(unsigned=True), ForeignKey('Suppliers.id'))
    supplier = relationship('Suppliers', back_populates='products')
    imports = relationship('PurchaseOrders', secondary='ProductPurchaseOrders', back_populates='products')
    # mã phân loại sản phẩm
    item_classification = relationship('ItemClassification', back_populates='product')
    # ngày sản xuất
    manufacture_date = Column(DateTime(timezone=True))
    # giá
    price = Column(String(255))
    # số lượng
    stock_quantity = Column(INTEGER)
    # mô tả
    description = Column(Text)
