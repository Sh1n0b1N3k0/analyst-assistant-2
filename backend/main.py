"""
Главный файл FastAPI приложения
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import import_requirements, export_requirements

# Создание таблиц базы данных
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Analyst Assistant API",
    description="API для управления требованиями SRS",
    version="1.0.0"
)

# Настройка CORS для работы с фронтендом
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
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
