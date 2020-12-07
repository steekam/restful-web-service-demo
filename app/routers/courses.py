from typing import List

from app.schemas import CourseCreate, CourseResponse, StudentResponse
from app.database import get_db
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm.session import Session
from app.models import Course

router = APIRouter(
    prefix='/courses',
    tags=["courses"],
)

@router.get("/")
def get_all_courses(db: Session = Depends(get_db)):
    return Course.get_all(db)

@router.get("/{course_id}", response_model=CourseResponse)
def get_course_by_id(course_id: int, db: Session = Depends(get_db)):
    return Course.get_by_id(db, course_id)

@router.post("/create", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
def create(course: CourseCreate, db: Session = Depends(get_db)):
    return Course.create(db, course.dict())

@router.get("/{course_id}/students", response_model=List[StudentResponse])
def get_students_in_course(course_id: int, db: Session = Depends(get_db)):
    course = Course.get_by_id(db, course_id)

    if not course:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Course not found")

    return course.students
