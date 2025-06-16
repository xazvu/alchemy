from sqlalchemy.orm import selectinload, session
from sqlalchemy.orm import Session
from sqlalchemy.util import await_only

import models
from models import Base, Pilot
from engine import engine, session


# Создание таблиц (если не существует)
Base.metadata.create_all(engine)





