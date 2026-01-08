# Analyst Assistant - Система управления требованиями SRS

Система для управления требованиями к программному обеспечению в стандарте SRS (Software Requirements Specification).

## Структура проекта

```
analyst-assistant-2/
├── backend/          # Backend API (FastAPI)
├── frontend/         # Frontend приложение (React)
├── database/         # Схемы и миграции базы данных
└── docs/             # Документация
```

## Компоненты

### База данных
Хранит требования и их атрибуты в стандарте SRS.

### Backend
- **Импорт требований**: Компонент для импорта новых требований и их атрибутов
- **Экспорт требований**: Компонент для экспорта хранимых требований и их атрибутов

### Frontend
- **Форма импорта требований**: Пользовательский интерфейс для импорта
- **Форма настройки экспорта**: Пользовательский интерфейс для настройки и выполнения экспорта

## Быстрый старт

Подробные инструкции по установке см. в [docs/SETUP.md](docs/SETUP.md)

### Backend
```bash
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
python run.py
```

API будет доступен на http://localhost:8000
Документация API: http://localhost:8000/docs

### Frontend
```bash
cd frontend
npm install
npm start
```

Приложение будет доступно на http://localhost:3000

## Технологии

- **Backend**: Python, FastAPI, SQLAlchemy
- **Frontend**: React, TypeScript
- **Database**: SQLite (разработка) / PostgreSQL (продакшн)
