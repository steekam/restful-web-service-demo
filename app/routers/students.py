from typing import List

from pydantic.networks import EmailStr
from app.schemas import StudentBase, StudentResponse
from app.database import get_db
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from app.models import Course, Student
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/students",
    tags=["students"]
)

@router.get("/", response_model=List[StudentResponse])
def get_all_students(db: Session = Depends(get_db)):
    return Student.get_all(db)

@router.get("/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    return Student.get_by_id(db, student_id);

@router.get("/by_email/{student_email}")
def get_student_by_email(student_email: EmailStr, db: Session = Depends(get_db)):
    return Student.get_first_where(db, Student.email == student_email);

@router.post("/create", response_model=StudentResponse)
def create_student_record(student: StudentBase, db: Session = Depends(get_db)):
    if Student.get_first_where(db, Student.email == student.email):
        raise HTTPException(422, detail="Email address already exists")
    
    if not Course.get_by_id(db, student.course_id):
        raise HTTPException(422, detail="Course does not exist")

    return Student.create(db, student.dict())

