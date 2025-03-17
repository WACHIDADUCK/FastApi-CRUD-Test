from sqlalchemy import create_engine  # Corrección: sqlalchemy en lugar de sqalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL de la base de datos: mysql+mysqlconnector://usuario:contraseña@localhost:puerto/nombre_base_datos
URL_DATABASE = 'mysql+mysqlconnector://root:01450145@localhost:3306/pythonblog'

# Crear el motor de la base de datos
engine = create_engine(URL_DATABASE)

# Crear una fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear una clase base para los modelos
Base = declarative_base()