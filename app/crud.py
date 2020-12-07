

from sqlalchemy.orm import Session
from app.database import Base


class Crud():

    @classmethod
    def create(cls, db: Session, detailsDict: dict):
        modelInstance: Base = cls(**detailsDict)
        db.add(modelInstance)
        db.commit()
        db.refresh(modelInstance)
        return modelInstance

    @classmethod
    def get_by_id(cls, db: Session, id: int):
        return db.query(cls).filter(cls.id == id).first()
    
    @classmethod
    def get_first_where(cls, db: Session, *argv):
        return db.query(cls).filter(*argv).first()

    @classmethod
    def get_all_where(cls, db: Session, *argv):
        return db.query(cls).filter(*argv).all()

    @classmethod
    def get_all(cls, db: Session):
        return db.query(cls).all()

    def update(self, db: Session):
        pass

    def delete(self, db: Session):
        pass
