# Локальное развертывание в Docker

## Быстрый старт (3 команды)

### 1. Настройка переменных окружения

**Windows (Command Prompt):**
```cmd
copy env.docker.example .env
```

**Windows (PowerShell):**
```powershell
Copy-Item env.docker.example .env
```

**Linux/Mac:**
```bash
cp env.docker.example .env
```

Файл `.env` уже содержит все необходимые настройки для локального развертывания.

### 2. Запуск всех компонентов

```bash
docker-compose up -d
```

Эта команда автоматически:
- ✅ Соберет образы backend и frontend
- ✅ Запустит PostgreSQL базу данных
- ✅ Инициализирует базу данных (выполнит `database/init_database.sql`)
- ✅ Запустит backend API на порту 8000
- ✅ Запустит frontend на порту 3000

### 3. Проверка работы

Откройте в браузере:
- **Frontend приложение**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Документация (Swagger)**: http://localhost:8000/docs
- **API Документация (ReDoc)**: http://localhost:8000/redoc

## Проверка статуса

### Просмотр статуса всех контейнеров

```bash
docker-compose ps
```

Должны быть запущены 3 контейнера:
- `analyst-assistant-db` (PostgreSQL)
- `analyst-assistant-backend` (FastAPI)
- `analyst-assistant-frontend` (Nginx + React)

### Просмотр логов

```bash
# Все сервисы
docker-compose logs -f

# Только backend
docker-compose logs -f backend

# Только frontend
docker-compose logs -f frontend

# Только база данных
docker-compose logs -f db
```

## Управление

### Остановка всех сервисов

```bash
docker-compose down
```

### Остановка с удалением данных БД

```bash
docker-compose down -v
```

⚠️ **Внимание:** Это удалит все данные из базы данных!

### Перезапуск

```bash
docker-compose restart
```

### Пересборка после изменений кода

```bash
docker-compose up -d --build
```

## Работа с базой данных

### Подключение к PostgreSQL

```bash
docker-compose exec db psql -U postgres -d requirements_db
```

### Выполнение SQL запросов

```bash
docker-compose exec db psql -U postgres -d requirements_db -c "SELECT COUNT(*) FROM requirements;"
```

### Резервное копирование

```bash
docker-compose exec db pg_dump -U postgres requirements_db > backup_$(date +%Y%m%d_%H%M%S).sql
```

### Восстановление из backup

```bash
docker-compose exec -T db psql -U postgres -d requirements_db < backup.sql
```

## Структура развертывания

```
┌─────────────────────────────────────────┐
│         Docker Network                   │
│  analyst-assistant-network               │
│                                          │
│  ┌──────────┐  ┌──────────┐  ┌────────┐│
│  │ Frontend │──│ Backend  │──│   DB   ││
│  │ :80      │  │ :8000    │  │ :5432  ││
│  └──────────┘  └──────────┘  └────────┘│
│       │             │              │     │
└───────┼─────────────┼──────────────┼─────┘
        │             │              │
    :3000          :8000          :5432
  (localhost)   (localhost)   (localhost)
```

## Порты

- **3000** - Frontend (React приложение через Nginx)
- **8000** - Backend API (FastAPI)
- **5432** - PostgreSQL база данных

## Volumes (хранилище данных)

- `postgres_data` - данные PostgreSQL (сохраняются между перезапусками)
- `backend_uploads` - загруженные файлы backend

## Переменные окружения

Все настройки находятся в файле `.env`:

```env
# PostgreSQL
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=requirements_db
POSTGRES_PORT=5432

# Backend
BACKEND_PORT=8000

# Frontend
FRONTEND_PORT=3000

# CORS
CORS_ORIGINS=http://localhost:3000,http://localhost:80
```

## Решение проблем

### Проблема: Контейнеры не запускаются

1. Проверьте логи:
   ```bash
   docker-compose logs
   ```

2. Проверьте, что порты свободны:
   ```bash
   # Windows
   netstat -an | findstr "3000 8000 5432"
   
   # Linux/Mac
   lsof -i :3000 -i :8000 -i :5432
   ```

3. Пересоберите образы:
   ```bash
   docker-compose build --no-cache
   docker-compose up -d
   ```

### Проблема: База данных не инициализируется

1. Проверьте логи базы данных:
   ```bash
   docker-compose logs db
   ```

2. Пересоздайте базу данных:
   ```bash
   docker-compose down -v
   docker-compose up -d db
   # Подождите 10-15 секунд для инициализации
   docker-compose up -d
   ```

### Проблема: Backend не может подключиться к БД

1. Убедитесь, что база данных запущена:
   ```bash
   docker-compose ps db
   ```

2. Проверьте подключение:
   ```bash
   docker-compose exec backend python -c "from database import engine; engine.connect()"
   ```

### Проблема: Frontend не видит backend

1. Проверьте, что backend запущен:
   ```bash
   curl http://localhost:8000/api/health
   ```

2. Проверьте настройки nginx:
   ```bash
   docker-compose exec frontend cat /etc/nginx/conf.d/default.conf
   ```

## Разработка в Docker

Для разработки с hot reload код монтируется как volume. Изменения в коде применяются автоматически:

- **Backend**: изменения применяются через `--reload` флаг uvicorn
- **Frontend**: требует пересборки образа (или используйте dev режим)

### Dev режим для frontend

Создайте `docker-compose.override.yml`:

```yaml
version: '3.8'

services:
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile.dev  # Создайте отдельный Dockerfile для dev
    volumes:
      - ./frontend:/app
      - /app/node_modules
    command: npm start
    ports:
      - "3000:3000"
```

## Очистка

### Удаление всех контейнеров и volumes

```bash
docker-compose down -v
```

### Удаление образов

```bash
docker-compose down --rmi all
```

### Полная очистка (контейнеры, volumes, образы, сети)

```bash
docker-compose down -v --rmi all
docker system prune -a
```

⚠️ **Внимание:** Это удалит все данные и образы!

## Следующие шаги

После успешного запуска:

1. Откройте http://localhost:3000
2. Используйте форму импорта для добавления требований
3. Используйте форму экспорта для выгрузки требований
4. Изучите API документацию на http://localhost:8000/docs

## Дополнительная документация

- [DOCKER_QUICKSTART.md](DOCKER_QUICKSTART.md) - Краткая инструкция
- [docs/DOCKER.md](docs/DOCKER.md) - Подробная документация
- [README.md](README.md) - Общая информация о проекте
