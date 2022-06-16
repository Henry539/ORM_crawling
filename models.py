
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class Shops(Base):
    __tablename__ = "SHOPS"

    ID = Column(Integer, primary_key=True, index=True)
    SHOP_ID = Column(Integer, index=True)
    SHOP_NAME = Column(String, index=True)
    STATUS = Column(Boolean, default=True)

    ITEMS = relationship("Items", back_populates="SHOP")


class Items(Base):
    __tablename__ = "ITEMS"

    ID_ = Column(Integer, primary_key=True, index=True)
    ITEM_ID = Column(Integer, index=True)
    SHOP_ID = Column(Integer, ForeignKey("SHOPS.SHOP_ID"))

    SHOP = relationship("Shops", back_populates="ITEMS")
    DATA = relationship("Data_Items", back_populates="ITEM")

class Data_Items(Base):
    __tablename__ = "DATA_ITEMS"

    ID__ = Column(Integer, primary_key=True, index=True)
    TIME = Column(String, index=True)
    ITEM_ID = Column(Integer, ForeignKey("ITEMS.ITEM_ID"))
    HISTORICAL_SOLD = Column(Integer, index=True)

    ITEM = relationship("Items", back_populates="DATA")