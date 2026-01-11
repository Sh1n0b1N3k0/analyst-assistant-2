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

## Docker развертывание (рекомендуется)

Для быстрого локального развертывания всей системы в Docker:

> ⚠️ **Важно:** Локальный Supabase запускается автоматически в Docker контейнере.  
> Схема базы данных применяется автоматически при первом запуске.

### Windows:
```bash
start-docker.bat
```

### Linux/Mac:
```bash
chmod +x start-docker.sh
./start-docker.sh
```

### Или вручную:

**Windows:**
```cmd
copy env.docker.example .env
docker-compose up -d
docker-compose ps
```

**Linux/Mac:**
```bash
cp env.docker.example .env
docker-compose up -d
docker-compose ps
```

После запуска:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Документация**: http://localhost:8000/docs

**Остановка:**
```cmd
# Windows
stop-docker.bat

# Linux/Mac
./stop-docker.sh

# Или вручную
docker-compose down
```

**Для Windows также см.:** [WINDOWS_DOCKER.md](WINDOWS_DOCKER.md)

Подробные инструкции:
- [LOCAL_DOCKER_SETUP.md](LOCAL_DOCKER_SETUP.md) - Локальное развертывание
- [DOCKER_QUICKSTART.md](DOCKER_QUICKSTART.md) - Быстрый старт
- [docs/DOCKER.md](docs/DOCKER.md) - Полная документация

## Технологии

- **Backend**: Python, FastAPI, SQLAlchemy
- **Frontend**: React, TypeScript
- **Database**: Локальный Supabase PostgreSQL ([supabase/postgres](https://github.com/supabase/postgres))
- **Containerization**: Docker, Docker Compose

## База данных

Проект использует локальный Supabase (PostgreSQL в Docker контейнере) с расширенной схемой базы данных для управления требованиями SRS.

### Основные возможности схемы:

- **RBAC** - Роли и права доступа (администратор, аналитик, ревьюер, разработчик, просмотр)
- **Требования** - По стандарту ISO/IEC/IEEE 29148 с полной трассировкой
- **Системные компоненты** - Микросервисы, библиотеки, БД, API Gateway и т.д.
- **UI элементы** - Экраны, формы, поля с иерархией
- **Трассировка** - Связи между требованиями, компонентами и UI
- **История изменений** - Полный аудит всех изменений
- **Комментарии** - Обсуждения артефактов
- **Тест-кейсы** - Верификация требований
- **Документация** - Спецификации и диаграммы
- **Риски и метрики** - Трекинг рисков и KPI проекта
- **Сущности системы** - Акторы, объекты данных, бизнес-процессы

### Инициализация базы данных:

**Локальный Supabase (автоматически):**
Схема базы данных применяется автоматически при первом запуске Docker Compose через файл `database/init_database.sql`.

**Ручная инициализация (если нужно):**
```bash
docker-compose exec supabase-db psql -U postgres -d postgres -f /docker-entrypoint-initdb.d/init_database.sql
```

Подробнее: [docs/SUPABASE_SETUP.md](docs/SUPABASE_SETUP.md) и [database/README.md](database/README.md)
