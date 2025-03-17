from sqlalchemy import Boolean, Column, ForeignKey, Integer, String 
from database import Base

# Definir el modelo de usuario
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)

# Definir el modelo de post
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    content = Column(String(100))
    # published = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))