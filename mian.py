from sqlalchemy.orm import Session

from models import Base, User
from engine import engine


# Создание таблиц (если не существует)
Base.metadata.create_all(engine)

# Добавление пользователя
# with Session(engine) as session:
#     session.add(User(name='Isa', city='Paris', age=20))
#     session.commit()