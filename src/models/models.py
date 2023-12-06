from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    update_date = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
