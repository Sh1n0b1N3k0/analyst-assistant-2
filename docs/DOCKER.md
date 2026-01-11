# Развертывание в Docker

## Требования

- Docker 20.10+
- Docker Compose 2.0+

## Быстрый старт

### 1. Подготовка

Скопируйте файл с переменными окружения:

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

Или используйте скрипт `start-docker.bat` / `start-docker.sh` - он создаст файл автоматически.

При необходимости отредактируйте `.env` файл.

### 2. Запуск всех сервисов

```bash
docker-compose up -d
```

Эта команда:
- Соберет образы для backend и frontend
- Запустит PostgreSQL базу данных
- Инициализирует базу данных скриптом `database/init_database.sql`
- Запустит backend API
- Запустит frontend (nginx)

### 3. Проверка

После запуска сервисы будут доступны:

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Документация**: http://localhost:8000/docs
- **PostgreSQL**: localhost:5432

Проверьте статус контейнеров:

```bash
docker-compose ps
```

Просмотрите логи:

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

## Остановка

Остановить все сервисы:

```bash
docker-compose down
```

Остановить и удалить volumes (удалит данные БД):

```bash
docker-compose down -v
```

## Пересборка образов

Если изменили код и нужно пересобрать образы:

```bash
docker-compose build
docker-compose up -d
```

Или одной командой:

```bash
docker-compose up -d --build
```

## Отдельные сервисы

### Запуск только базы данных

```bash
docker-compose up -d db
```

### Запуск только backend

```bash
docker-compose up -d db backend
```

### Запуск только frontend

```bash
docker-compose up -d frontend
```

## Работа с базой данных

### Подключение к PostgreSQL

```bash
docker-compose exec db psql -U postgres -d requirements_db
```

### Выполнение SQL скрипта

```bash
docker-compose exec -T db psql -U postgres -d requirements_db < database/init_database.sql
```

### Резервное копирование

```bash
docker-compose exec db pg_dump -U postgres requirements_db > backup.sql
```

### Восстановление из backup

```bash
docker-compose exec -T db psql -U postgres -d requirements_db < backup.sql
```

## Разработка

### Режим разработки с hot reload

Для разработки можно использовать volumes для монтирования кода:

```yaml
# docker-compose.override.yml
version: '3.8'

services:
  backend:
    volumes:
      - ./backend:/app
    command: uvicorn main:app --host 0.0.0.0 --port 8000 --reload

  frontend:
    volumes:
      - ./frontend:/app
      - /app/node_modules
```

Создайте `docker-compose.override.yml` на основе `docker-compose.override.yml.example`.

### Выполнение команд в контейнерах

**Backend:**
```bash
docker-compose exec backend python manage.py <command>
docker-compose exec backend pip install <package>
```

**Frontend:**
```bash
docker-compose exec frontend npm install <package>
```

## Переменные окружения

Основные переменные (в файле `.env`):

- `POSTGRES_USER` - пользователь PostgreSQL (по умолчанию: postgres)
- `POSTGRES_PASSWORD` - пароль PostgreSQL (по умолчанию: postgres)
- `POSTGRES_DB` - имя базы данных (по умолчанию: requirements_db)
- `POSTGRES_PORT` - порт PostgreSQL (по умолчанию: 5432)
- `BACKEND_PORT` - порт backend API (по умолчанию: 8000)
- `FRONTEND_PORT` - порт frontend (по умолчанию: 3000)
- `CORS_ORIGINS` - разрешенные источники для CORS

## Troubleshooting

### Проблема: Контейнеры не запускаются

1. Проверьте логи:
   ```bash
   docker-compose logs
   ```

2. Проверьте, что порты не заняты:
   ```bash
   netstat -an | findstr "3000 8000 5432"
   ```

3. Пересоберите образы:
   ```bash
   docker-compose build --no-cache
   ```

### Проблема: База данных не инициализируется

1. Проверьте логи базы данных:
   ```bash
   docker-compose logs db
   ```

2. Проверьте, что скрипт инициализации доступен:
   ```bash
   docker-compose exec db ls -la /docker-entrypoint-initdb.d/
   ```

3. Пересоздайте базу данных:
   ```bash
   docker-compose down -v
   docker-compose up -d db
   ```

### Проблема: Backend не может подключиться к БД

1. Убедитесь, что база данных запущена:
   ```bash
   docker-compose ps db
   ```

2. Проверьте переменную DATABASE_URL в backend:
   ```bash
   docker-compose exec backend env | grep DATABASE_URL
   ```

3. Проверьте подключение вручную:
   ```bash
   docker-compose exec backend python -c "from database import engine; engine.connect()"
   ```

### Проблема: Frontend не видит backend

1. Проверьте настройки nginx:
   ```bash
   docker-compose exec frontend cat /etc/nginx/conf.d/default.conf
   ```

2. Проверьте, что backend доступен:
   ```bash
   docker-compose exec frontend curl http://backend:8000/api/health
   ```

## Production развертывание

Для production рекомендуется:

1. Использовать секреты вместо `.env` файла
2. Настроить SSL/TLS
3. Использовать внешнюю базу данных
4. Настроить мониторинг и логирование
5. Использовать reverse proxy (nginx/traefik)
6. Настроить резервное копирование БД

Пример production конфигурации:

```yaml
# docker-compose.prod.yml
version: '3.8'

services:
  backend:
    restart: always
    environment:
      DATABASE_URL: ${DATABASE_URL}
    # Добавьте healthcheck и другие настройки

  frontend:
    restart: always
    # Настройки для production

  db:
    restart: always
    # Настройки для production
```

Запуск:

```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```
