from sqlalchemy import Column, String, DECIMAL, ForeignKey
from .base import Base, BaseMixin
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import INTEGER

class Customer(Base, BaseMixin):
    __tablename__ = 'customers'
    name = Column(String(255), unique=True)
    account = Column(String(255))
    total_spending = Column(DECIMAL(30, 0), default=0)
    rank_id = Column(INTEGER(unsigned=True), ForeignKey('member_ranks.id'))
    rank = relationship('MemberRank', back_populates='customers')
    orders = relationship('Order', back_populates='customer', cascade="all, delete-orphan")

