from sqlalchemy.orm import selectinload
from sqlalchemy.orm import Session

from models import Base, User, Passport
from engine import engine


# Создание таблиц (если не существует)
Base.metadata.create_all(engine)

# Добавление пользователя с паспортом
def get_user():
    with Session(engine) as session:
        user = User(name='', city='', age=)
        user.passport = Passport(number=1555555)
        session.add(user)
        session.commit()

# Получение паспорта по пользователю
def get_passport_with_user():
    with Session(engine) as session:
        user = session.get(User, 4)
        if user:
            print(user.passport.number)
        return None


# Получение пользователя по паспорту
def get_user_with_passport():
    with Session(engine) as session:
        passport = session.get(Passport, 2)
        if passport and passport.user:
            print(passport.user.name, passport.number)
            return passport.user
        return None



# get_user_with_passport()
# get_passport_with_user()
# get_user()

