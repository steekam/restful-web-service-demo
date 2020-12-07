from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pathlib import Path

from sqlalchemy.orm.session import Session

ROOT_DIR = Path(__file__).parent.parent.resolve()
SQLALCHEMY_DATABASE_URL = f"sqlite:///{ROOT_DIR}/database.sqlite"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



# Dependency for routes
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
