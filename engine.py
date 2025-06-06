from sqlalchemy import create_engine

#SQlite
engine = create_engine('sqlite:///singular.db', echo=True, future=True)