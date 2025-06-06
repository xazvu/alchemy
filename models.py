from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    city: Mapped[str] = mapped_column(String(20))
    age: Mapped[int] = mapped_column(Integer)

    passport: Mapped["Passport"] = relationship(back_populates='user', uselist=False, cascade="all, delete-orphan")


class Passport(Base):
    __tablename__ = 'passports'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), unique=True)

    number: Mapped[int] = mapped_column(Integer, unique=True)
    user: Mapped['User'] = relationship(back_populates='passport')


