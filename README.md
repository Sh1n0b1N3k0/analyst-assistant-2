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

> ⚠️ **Перед началом:** Убедитесь, что у вас установлены [Python 3.8+](https://www.python.org/downloads/) и [Node.js 16+](https://nodejs.org/).  
> Подробнее см. [REQUIREMENTS.md](REQUIREMENTS.md)  
> **Быстрая инструкция:** [QUICK_START.md](QUICK_START.md)

### Установка зависимостей

**Windows:**

**PowerShell:**
```powershell
# Backend
cd backend
.\install.bat

# Frontend
cd frontend
.\install.bat
```

**Command Prompt (cmd):**
```cmd
# Backend
cd backend
install.bat

# Frontend
cd frontend
install.bat
```

Или просто дважды кликните на файлы `.bat` в проводнике Windows.

**Linux/Mac:**
```bash
# Backend
cd backend
chmod +x install.sh && ./install.sh

# Frontend
cd frontend
chmod +x install.sh && ./install.sh
```

Подробные инструкции см. в [INSTALL.md](INSTALL.md) и [docs/SETUP.md](docs/SETUP.md)

> ⚠️ **Проблемы с SSL?** Если у вас ошибка `CERTIFICATE_VERIFY_FAILED`:
> - **Windows PowerShell:** `.\install_ssl_fix.bat`
> - **Windows Command Prompt:** `install_ssl_fix.bat`
> - **Или просто дважды кликните** на файл в проводнике
> - **Linux/Mac:** `chmod +x install_ssl_fix.sh && ./install_ssl_fix.sh`  
> Подробнее: [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)

### Запуск

**Backend:**
```bash
cd backend
venv\Scripts\activate  # Windows
# или source venv/bin/activate  # Linux/Mac
python run.py
```

API будет доступен на http://localhost:8000  
Документация API: http://localhost:8000/docs

**Frontend:**
```bash
cd frontend
npm start
```

Приложение будет доступно на http://localhost:3000

## Технологии

- **Backend**: Python, FastAPI, SQLAlchemy
- **Frontend**: React, TypeScript
- **Database**: SQLite (разработка) / PostgreSQL (продакшн)
