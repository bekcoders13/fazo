from sqlalchemy import Column, Integer, Date
from db_connect import Base


class Incomes(Base):
    __tablename__ = "incomes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    date_receipt = Column(Date, nullable=False)