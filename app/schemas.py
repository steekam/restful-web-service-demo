from pydantic.networks import EmailStr
from app.models import Course
from pydantic import BaseModel

class CourseBase(BaseModel):
    name: str

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True



class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    course_id: int


class StudentResponse(StudentBase):
    id: int
    course_id: int

    class Config:
        orm_mode = True
