# Миграция с локального PostgreSQL на Supabase

Этот документ описывает процесс миграции с локального PostgreSQL контейнера на Supabase.

## Что изменилось

### Удалено:
- Локальный контейнер PostgreSQL (`db` сервис в docker-compose.yml)
- Зависимость backend от локальной БД
- Локальные volumes для данных БД

### Обновлено:
- `docker-compose.yml` - убран сервис `db`, обновлены переменные окружения
- `backend/wait-for-db.py` - теперь работает с Supabase connection string
- `env.docker.example` - добавлена настройка `SUPABASE_DATABASE_URL`
- Документация обновлена для работы с Supabase

## Шаги миграции

### 1. Создайте проект Supabase

1. Перейдите на [https://supabase.com](https://supabase.com)
2. Создайте новый проект
3. Сохраните пароль базы данных

### 2. Получите Connection String

1. В Supabase Dashboard перейдите в **Settings** > **Database**
2. Скопируйте **Connection string** (рекомендуется Connection pooling)
3. Формат: `postgresql://postgres.[project-ref]:[password]@aws-0-[region].pooler.supabase.com:6543/postgres`

### 3. Настройте переменные окружения

1. Обновите файл `.env`:
   ```env
   SUPABASE_DATABASE_URL=postgresql://postgres.[project-ref]:[password]@aws-0-[region].pooler.supabase.com:6543/postgres
   ```

2. Или создайте новый из примера:
   ```bash
   copy env.docker.example .env
   # Затем отредактируйте .env и укажите SUPABASE_DATABASE_URL
   ```

### 4. Примените схему базы данных

1. Откройте SQL Editor в Supabase Dashboard
2. Откройте файл `database/init_database.sql` из проекта
3. Скопируйте весь SQL скрипт
4. Вставьте в SQL Editor и выполните (Run)

### 5. Миграция данных (если есть)

Если у вас уже есть данные в локальной БД:

1. Экспортируйте данные из локальной БД:
   ```bash
   docker-compose exec db pg_dump -U postgres requirements_db > backup.sql
   ```

2. Импортируйте в Supabase:
   ```bash
   psql "postgresql://postgres:[password]@db.[project-ref].supabase.co:5432/postgres" -f backup.sql
   ```

   Или используйте SQL Editor в Supabase Dashboard.

### 6. Обновите Docker Compose

1. Остановите старые контейнеры:
   ```bash
   docker-compose down -v
   ```

2. Запустите с новой конфигурацией:
   ```bash
   docker-compose up -d
   ```

### 7. Проверка

1. Проверьте логи backend:
   ```bash
   docker-compose logs backend
   ```

2. Должно появиться: `Supabase database is ready!`

3. Проверьте health endpoint:
   ```bash
   curl http://localhost:8000/api/health
   ```

## Откат (если нужно вернуться к локальной БД)

Если нужно вернуться к локальной БД:

1. Восстановите старую версию `docker-compose.yml` из Git
2. Восстановите `backend/wait-for-db.py` из Git
3. Запустите:
   ```bash
   docker-compose up -d
   ```

## Преимущества Supabase

- ✅ Не нужно управлять локальной БД
- ✅ Автоматические резервные копии
- ✅ Масштабируемость
- ✅ Дополнительные возможности (REST API, Realtime, Auth)
- ✅ Веб-интерфейс для управления данными
- ✅ SQL Editor в браузере

## Дополнительная информация

- [Документация Supabase](https://supabase.com/docs)
- [Настройка Supabase для проекта](docs/SUPABASE_SETUP.md)
