from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# 1. Connect to MySQL Server first (without a specific database) to create it if it doesn't exist
SERVER_URL = "mysql+pymysql://root:gowthu22%40gali@localhost/cafe_db"
temp_engine = create_engine(SERVER_URL)
with temp_engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS cafe_db"))

# 2. Now connect to the actual database
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:gowthu22%40gali@localhost/cafe_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
