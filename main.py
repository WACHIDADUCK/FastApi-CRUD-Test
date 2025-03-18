from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Crear todas las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

# # Definir el esquema de datos para un post
# class PostBase(BaseModel):
#     title: str
#     content: str
#     user_id: int

class UserTypeBase(BaseModel):
    name: str
class UserTypeUpdate(BaseModel):
    name: str

# Definir el esquema de datos para un usuario

class UserBase(BaseModel):
    name: str
    email: str
    profile_pic: str
    user_type_id: int

class LessonBase(BaseModel):
    
    title: str
    start_time: str
    end_time: str
    subject: str
    content: str
    user_id: int



# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Anotación para la dependencia de la base de datos
db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
def read_root():
    return {"Hello": "World"}



# USER TYPES
@app.post("/users_types/", status_code=status.HTTP_201_CREATED)
async def create_user_type(user_type: UserTypeBase, db: db_dependency):
    db_user_type = models.UserType(**user_type.dict())
    db.add(db_user_type)
    db.commit()
    return db_user_type

@app.get("/users_types/{type_id}", status_code=status.HTTP_200_OK)
async def read_user_type(type_id: int, db: db_dependency):
    user_type = db.query(models.UserType).filter(models.UserType.id == type_id).first()
    if user_type is None:
        raise HTTPException(status_code=404, detail="User type not found")
    return user_type

@app.delete("/users_types/{type_id}", status_code=status.HTTP_200_OK)
async def delete_post(type_id: int, db: db_dependency):
    user_type = db.query(models.UserType).filter(models.UserType.id == type_id).first()
    if user_type is None:
        raise HTTPException(status_code=404, detail="User type not found")
    db.delete(user_type)
    db.commit()

@app.put("/users_types/{type_id}", status_code=status.HTTP_200_OK)
async def update_user_type(type_id: int, user_type: UserTypeUpdate, db: db_dependency):
    db_user_type = db.query(models.UserType).filter(models.UserType.id == type_id).first()
    if db_user_type is None:
        raise HTTPException(status_code=404, detail="User type not found")
    
    db_user_type.name = user_type.name
    db.commit()
    db.refresh(db_user_type)
    return db_user_type



# USERS
# Ruta para crear un nuevo usuario
@app.post("/user/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.Users(**user.dict())
    db.add(db_user)
    db.commit()
    return db_user

@app.get("/user/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/user/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db: db_dependency):
    db_user = db.query(models.Users).filter(models.Users.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()

@app.put("/user/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user: UserBase, db: db_dependency):
    db_user = db.query(models.Users).filter(models.Users.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_user.name = user.name
    db_user.email = user.email
    db_user.profile_pic = user.profile_pic
    db_user.user_type_id = user.user_type_id
    db.commit()
    db.refresh(db_user)
    return db_user


# # LESSONS
@app.post("/lesson/", status_code=status.HTTP_201_CREATED)
async def create_user(lesson: LessonBase, db: db_dependency):
    db_lesson = models.Lessons(**lesson.dict())
    db.add(db_lesson)
    db.commit()
    return db_lesson

@app.get("/lesson/{lesson_id}", status_code=status.HTTP_200_OK)
async def read_user(lesson_id: int, db: db_dependency):
    lesson = db.query(models.Lessons).filter(models.Lessons.id == lesson_id).first()
    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson

@app.delete("/lesson/{lesson_id}", status_code=status.HTTP_200_OK)
async def delete_user(lesson_id: int, db: db_dependency):
    db_lesson = db.query(models.Lessons).filter(models.Lessons.id == lesson_id).first()
    if db_lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    db.delete(db_lesson)
    db.commit()

@app.put("/lesson/{lesson_id}", status_code=status.HTTP_200_OK)
async def update_user(lesson_id: int, lesson: LessonBase, db: db_dependency):
    db_lesson = db.query(models.Lessons).filter(models.Lessons.id == lesson_id).first()
    if db_lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    
    db_lesson.title = lesson.title
    db_lesson.start_time = lesson.start_time
    db_lesson.end_time = lesson.end_time
    db_lesson.subject = lesson.subject
    db_lesson.content = lesson.content
    db_lesson.user_id = lesson.user_id
    
    db.commit()
    db.refresh(db_lesson)
    return db_lesson
