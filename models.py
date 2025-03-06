from database import Base
from typing import Optional
from sqlalchemy import String, Integer, Float, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, date

class Car(Base):
    __tablename__ = 'cars'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category: Mapped[str] = mapped_column(String(16))
    marka: Mapped[str] = mapped_column(String(16))
    model: Mapped[str] = mapped_column(String(16))
    price: Mapped[int] = mapped_column(Integer, default=0)
    year: Mapped[date]
    mileage: Mapped[int] = mapped_column(Integer, default=0)
    city: Mapped[str] = mapped_column(String(16))
    country: Mapped[str] = mapped_column(String(16))
    with_photo: Mapped[bool] = mapped_column(Boolean, default=False)
    color: Mapped[str] = mapped_column(String(16))
    volume:  Mapped[float] = mapped_column(Float, default=0.8)
    description: Mapped[Optional[str]]


class Bet(Base):
    __tablename__ = 'bets'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    number: Mapped[int] = mapped_column(Integer, default=0)
    total_number:  Mapped[int] = mapped_column(Integer, default=0)
    buy_number: Mapped[int] = mapped_column(Integer, default=0)
    start_date: Mapped[datetime]
    end_date: Mapped[datetime]
