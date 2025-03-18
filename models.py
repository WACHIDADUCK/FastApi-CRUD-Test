from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from database import Base
from sqlalchemy.orm import relationship


class UserType(Base):
    __tablename__ = "user_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

# Definir el modelo de Users
class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(50))
    profile_pic = Column(String(50))
    user_type_id = Column(Integer, ForeignKey("user_types.id"))
    user_type = relationship("UserType")


# class Subject(Base):
#     __tablename__ = "subjects"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(50), index=True)


# class SubjectTeacher(Base):
#     __tablename__ = "SubjectTeachers"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(50), index=True)

# Classrooms


class Lessons(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    start_time = Column(String(100))
    end_time = Column(String(100))
    subject = Column(String(100))

    content = Column(String(100))
    user_id = Column(Integer, ForeignKey("users.id"))


