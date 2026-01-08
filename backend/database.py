"""
Настройка подключения к базе данных
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from pathlib import Path
from dotenv import load_dotenv

# Загружаем .env из корня проекта
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# URL базы данных (по умолчанию SQLite)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./requirements.db")

# Создание движка базы данных
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

# Создание сессии
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()


def get_db():
    """
    Dependency для получения сессии базы данных
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
