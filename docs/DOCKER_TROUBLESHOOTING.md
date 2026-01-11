# Решение проблем с Docker

## Проблема: Frontend не собирается

### Ошибка: `react-scripts: not found`

**Причина:** Зависимости не установились правильно.

**Решение 1:** Пересоберите образ без кэша:

```bash
docker-compose build frontend --no-cache
```

**Решение 2:** Используйте альтернативный Dockerfile:

Измените `docker-compose.yml`:

```yaml
frontend:
  build:
    context: ./frontend
    dockerfile: Dockerfile.alternative
```

**Решение 3:** Проверьте package-lock.json

Убедитесь, что `package-lock.json` синхронизирован с `package.json`:

```bash
cd frontend
npm install --legacy-peer-deps
```

Затем пересоберите:

```bash
docker-compose build frontend --no-cache
```

### Ошибка: `npm error Exit handler never called!`

**Причина:** Проблема с npm в Alpine Linux.

**Решение:** Используйте полный образ Node.js вместо Alpine:

Измените первую строку в `frontend/Dockerfile`:

```dockerfile
FROM node:18 AS builder
```

Вместо:

```dockerfile
FROM node:18-alpine AS builder
```

### Ошибка: Порт уже занят

**Решение:** Измените порты в `.env`:

```env
BACKEND_PORT=8001
FRONTEND_PORT=3001
POSTGRES_PORT=5433
```

## Проблема: Backend не может подключиться к БД

### Ошибка: `could not connect to server`

**Решение 1:** Убедитесь, что база данных запущена:

```bash
docker-compose ps db
```

**Решение 2:** Проверьте переменную DATABASE_URL:

```bash
docker-compose exec backend env | grep DATABASE_URL
```

Должна быть: `postgresql://postgres:postgres@db:5432/requirements_db`

**Решение 3:** Перезапустите сервисы:

```bash
docker-compose restart
```

## Проблема: База данных не инициализируется

### Скрипт init_database.sql не выполняется

**Решение 1:** Проверьте, что файл монтирован:

```bash
docker-compose exec db ls -la /docker-entrypoint-initdb.d/
```

Должен быть файл `init_database.sql`.

**Решение 2:** Пересоздайте базу данных:

```bash
docker-compose down -v
docker-compose up -d db
# Подождите 10-15 секунд
docker-compose logs db
# Проверьте, что скрипт выполнился
docker-compose up -d
```

**Решение 3:** Примените скрипт вручную:

```bash
docker-compose exec -T db psql -U postgres -d requirements_db < database/init_database.sql
```

## Проблема: Frontend не видит backend

### Ошибка: CORS или 404 при запросах к API

**Решение 1:** Проверьте настройки nginx:

```bash
docker-compose exec frontend cat /etc/nginx/conf.d/default.conf
```

Убедитесь, что есть секция:

```nginx
location /api {
    proxy_pass http://backend:8000;
    ...
}
```

**Решение 2:** Проверьте, что backend доступен:

```bash
docker-compose exec frontend wget -O- http://backend:8000/api/health
```

**Решение 3:** Проверьте CORS настройки в backend:

В файле `.env` убедитесь, что есть:

```env
CORS_ORIGINS=http://localhost:3000,http://localhost:80,http://frontend:80
```

## Проблема: Медленная сборка

### Ускорение сборки

**Решение 1:** Используйте BuildKit:

```bash
DOCKER_BUILDKIT=1 docker-compose build
```

**Решение 2:** Используйте кэш слоев:

Не удаляйте `package-lock.json` и используйте правильный порядок копирования в Dockerfile.

## Проблема: Контейнеры падают

### Проверка логов

```bash
# Все сервисы
docker-compose logs

# Конкретный сервис
docker-compose logs backend
docker-compose logs frontend
docker-compose logs db
```

### Перезапуск с пересборкой

```bash
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

## Проблема: Данные не сохраняются

### Проверка volumes

```bash
docker volume ls
docker volume inspect analyst-assistant-2_postgres_data
```

### Резервное копирование

```bash
docker-compose exec db pg_dump -U postgres requirements_db > backup.sql
```

## Полная переустановка

Если ничего не помогает:

```bash
# Остановить и удалить все
docker-compose down -v

# Удалить образы
docker-compose down --rmi all

# Очистить систему Docker (осторожно!)
docker system prune -a

# Пересобрать и запустить
docker-compose up -d --build
```
