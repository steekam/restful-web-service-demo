from fastapi import FastAPI
from app.routers import courses, students
import uvicorn

from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(courses.router)
app.include_router(students.router)

if __name__ == "__main__":
    uvicorn.run(app, port=8080)
