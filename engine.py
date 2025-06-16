from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#SQlite
DATABASE_URL = "sqlite:///./susano.db"  # или другой URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

