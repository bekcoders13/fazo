from db_connect import Base
from sqlalchemy import String, Column, Integer, Float, Date


class Laptops(Base):
    __tablename__ = "laptops"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    category_id = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)
    brand = Column(String(255), nullable=False)
    screen_type = Column(String(255), nullable=False)
    color = Column(String(255), nullable=False)
    country = Column(String(255), nullable=False)
    ram_size = Column(Integer, nullable=False)
    rom_size = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    display = Column(Float, nullable=False)
    videocard = Column(String(255), nullable=False)
    rom_type = Column(String(255), nullable=False)
    processor = Column(String(255), nullable=False)
    discount = Column(Integer, nullable=False)
    discount_price = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False)
    discount_time = Column(Date)