import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey

class Base(DeclarativeBase):
    pass


import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey


class Base(DeclarativeBase):
    pass


class Reys(Base):
    __tablename__ = 'reys'  # Исправлено название таблицы
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

    pilots: Mapped[list['Pilot']] = relationship('Pilot', back_populates='reys')


class Pilot(Base):
    __tablename__ = 'pilots'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20))

    reys_id: Mapped[int] = mapped_column(ForeignKey("reys.id"))
    reys: Mapped["Reys"] = relationship("Reys", back_populates="pilots")


