from db_connect import Base
from sqlalchemy import String, Column, Integer, Numeric, Date


class Tablets(Base):
    __tablename__ = "tablets"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25), nullable=False)
    description = Column(String(255), nullable=False)
    category_id = Column(Integer, nullable=False)
    price = Column(Numeric, nullable=False)
    brand = Column(String(25), nullable=False)
    screen_type = Column(String(25), nullable=False)
    camera = Column(Integer, nullable=False)
    self_camera = Column(Integer, nullable=False)
    color = Column(String(25), nullable=False)
    country = Column(String(25), nullable=False)
    ram_size = Column(Integer, nullable=False)
    rom_size = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    display = Column(Numeric, nullable=False)
    weight = Column(Numeric, nullable=False)
    discount = Column(Numeric, nullable=False)
    discount_price = Column(Numeric, nullable=False)
    count = Column(Integer, nullable=False)
    discount_time = Column(Date)
    see_num = Column(Integer, nullable=True)
    favorite = Column(Integer, nullable=True)
