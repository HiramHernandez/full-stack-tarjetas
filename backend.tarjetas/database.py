from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
config = {
  'user': 'root',
  'password': 'lmZ1415&',
  'host': 'localhost',
  'database': 'tarjetas_credito'
}
SQLALCHEMY_DATABASE_URL: str = f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}/{config['database']}"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()