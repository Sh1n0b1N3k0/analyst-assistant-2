# Настройка локального Supabase

## Обзор

Проект использует локальный Supabase в Docker контейнере. Supabase - это open-source альтернатива Firebase, которая предоставляет PostgreSQL базу данных с расширениями и дополнительными возможностями.

## Локальный Supabase в Docker

Локальный Supabase запускается автоматически при запуске `docker-compose up -d`. Используется официальный образ `supabase/postgres` с предустановленными расширениями PostgreSQL.

### Что включено:

- ✅ PostgreSQL 15 с расширениями (uuid-ossp, pg_trgm и др.)
- ✅ Автоматическая инициализация схемы базы данных
- ✅ Персистентное хранилище данных (volumes)
- ✅ Health checks для надежного запуска

## Настройка переменных окружения

1. Скопируйте файл `env.docker.example` в `.env`:
   ```bash
   copy env.docker.example .env
   ```

2. Файл `.env` уже содержит настройки по умолчанию:
   ```env
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_DB=postgres
   POSTGRES_PORT=5432
   ```

3. При необходимости измените пароль и другие настройки в `.env`

## Инициализация базы данных

Схема базы данных применяется автоматически при первом запуске контейнера через файл `database/init_database.sql`.

### Ручная инициализация (если нужно)

Если нужно применить схему вручную:

```bash
# Подключиться к контейнеру
docker-compose exec supabase-db psql -U postgres -d postgres

# Или применить SQL файл
docker-compose exec -T supabase-db psql -U postgres -d postgres < database/init_database.sql
```

## Запуск системы

```bash
docker-compose up -d
```

Эта команда:
- ✅ Запустит локальный Supabase PostgreSQL
- ✅ Применит схему базы данных
- ✅ Запустит backend API
- ✅ Запустит frontend

## Проверка подключения

1. Проверьте логи backend:
   ```bash
   docker-compose logs backend
   ```

2. Должно появиться: `Supabase database is ready!`

3. Проверьте health endpoint:
   ```bash
   curl http://localhost:8000/api/health
   ```

## Работа с базой данных

### Подключение к локальному Supabase

```bash
# Через docker-compose
docker-compose exec supabase-db psql -U postgres -d postgres

# Или напрямую (если psql установлен локально)
psql -h localhost -p 5432 -U postgres -d postgres
```

Пароль по умолчанию: `postgres` (или тот, что указан в `.env`)

### Выполнение SQL запросов

```bash
# Через docker-compose
docker-compose exec supabase-db psql -U postgres -d postgres -c "SELECT COUNT(*) FROM requirements;"
```

### Резервное копирование

```bash
# Создать backup
docker-compose exec supabase-db pg_dump -U postgres postgres > backup_$(date +%Y%m%d_%H%M%S).sql

# Восстановить из backup
docker-compose exec -T supabase-db psql -U postgres -d postgres < backup.sql
```

## Структура данных

Данные хранятся в Docker volume `supabase_db_data` и сохраняются между перезапусками контейнеров.

### Удаление всех данных

```bash
docker-compose down -v
```

⚠️ **Внимание:** Это удалит все данные из базы данных!

## Расширения PostgreSQL

Локальный Supabase включает следующие расширения:

- `uuid-ossp` - для генерации UUID
- `pg_trgm` - для полнотекстового поиска

Расширения автоматически создаются при инициализации базы данных.

## Troubleshooting

### Ошибка подключения

Если backend не может подключиться к базе данных:

1. Проверьте, что контейнер `supabase-db` запущен:
   ```bash
   docker-compose ps
   ```

2. Проверьте логи базы данных:
   ```bash
   docker-compose logs supabase-db
   ```

3. Проверьте переменные окружения в `.env`

### База данных не инициализируется

Если схема не применяется автоматически:

1. Проверьте, что файл `database/init_database.sql` существует
2. Проверьте логи контейнера:
   ```bash
   docker-compose logs supabase-db
   ```

3. Примените схему вручную (см. раздел "Ручная инициализация")

### Проблемы с портами

Если порт 5432 уже занят:

1. Измените `POSTGRES_PORT` в `.env`:
   ```env
   POSTGRES_PORT=5433
   ```

2. Обновите `DATABASE_URL` в docker-compose.yml или используйте переменную окружения

## Дополнительные возможности

Локальный Supabase предоставляет стандартный PostgreSQL с расширениями. Для полного функционала Supabase (REST API, Realtime, Auth) можно использовать:

1. **Supabase CLI** для локальной разработки:
   ```bash
   npm install -g supabase
   supabase init
   supabase start
   ```

2. Или использовать облачный Supabase для продакшн окружения

## Миграция данных

### Из локального PostgreSQL

Если у вас есть данные в локальном PostgreSQL:

```bash
# Экспорт
pg_dump -U postgres requirements_db > backup.sql

# Импорт в локальный Supabase
docker-compose exec -T supabase-db psql -U postgres -d postgres < backup.sql
```

### В облачный Supabase

Для миграции в облачный Supabase:

1. Экспортируйте данные из локального Supabase
2. Импортируйте через Supabase Dashboard или CLI
