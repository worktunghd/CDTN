from sqlalchemy import Column, String, DECIMAL
from .base import Base, BaseMixin
from sqlalchemy.orm import relationship


class MemberRank(Base, BaseMixin):
    __tablename__ = 'member_ranks'
    name = Column(String(255))
    code = Column(String(255), unique=True)
    spending = Column(DECIMAL(18, 0), default=0)
    discount = Column(String(255))
    customers = relationship('Customer', back_populates='rank')
