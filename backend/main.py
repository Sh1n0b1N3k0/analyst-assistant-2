"""
Главный файл FastAPI приложения
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base, DATABASE_URL
from routers import import_requirements, export_requirements

# Создание таблиц базы данных
# ВНИМАНИЕ: Для PostgreSQL используйте скрипт database/init_database.sql
# Автоматическое создание через SQLAlchemy работает только для простых моделей
# Для полной схемы с RBAC, компонентами и т.д. используйте SQL скрипт
if "sqlite" in DATABASE_URL:
    Base.metadata.create_all(bind=engine)
else:
    # Для PostgreSQL таблицы создаются через init_database.sql
    # Здесь можно добавить проверку существования таблиц
    pass

app = FastAPI(
    title="Analyst Assistant API",
    description="API для управления требованиями SRS",
    version="1.0.0"
)

# Настройка CORS для работы с фронтендом
# Разрешаем запросы с фронтенда (локально и из Docker)
import os
cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:80,http://frontend:80").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутеров
app.include_router(import_requirements.router, prefix="/api/import", tags=["import"])
app.include_router(export_requirements.router, prefix="/api/export", tags=["export"])


@app.get("/")
async def root():
    """Корневой endpoint"""
    return {"message": "Analyst Assistant API", "version": "1.0.0"}


@app.get("/api/health")
async def health_check():
    """Проверка здоровья API"""
    return {"status": "healthy"}
