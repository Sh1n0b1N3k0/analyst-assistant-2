# Инструкция по инициализации базы данных

## Требования

- PostgreSQL 12 или выше
- Права на создание базы данных и расширений

## Шаг 1: Создание базы данных

```bash
# Подключитесь к PostgreSQL
psql -U postgres

# Создайте базу данных
CREATE DATABASE requirements_db;

# Создайте пользователя (опционально)
CREATE USER requirements_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE requirements_db TO requirements_user;

# Выйдите из psql
\q
```

## Шаг 2: Применение скрипта инициализации

### Вариант 1: Через командную строку

```bash
psql -U postgres -d requirements_db -f database/init_database.sql
```

Или с указанием пользователя:

```bash
psql -U requirements_user -d requirements_db -f database/init_database.sql
```

### Вариант 2: Через psql интерактивно

```bash
psql -U postgres -d requirements_db
```

Затем в psql:

```sql
\i database/init_database.sql
```

### Вариант 3: Через pgAdmin

1. Откройте pgAdmin
2. Подключитесь к серверу PostgreSQL
3. Выберите базу данных `requirements_db`
4. Правый клик → Query Tool
5. Откройте файл `database/init_database.sql`
6. Выполните скрипт (F5)

## Шаг 3: Проверка

После выполнения скрипта вы должны увидеть:

```
NOTICE: База данных инициализирована успешно!
NOTICE: Создано таблиц: 26
NOTICE: Версия схемы: 1.4.1
```

Проверьте созданные таблицы:

```sql
\dt
```

Должны быть созданы все таблицы из скрипта.

## Шаг 4: Настройка переменных окружения

Создайте файл `.env` в корне проекта:

```env
DATABASE_URL=postgresql://requirements_user:your_password@localhost/requirements_db
```

Или для локального пользователя:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost/requirements_db
```

## Шаг 5: Проверка подключения

Запустите backend и проверьте подключение:

```bash
cd backend
venv\Scripts\activate
python run.py
```

Если все настроено правильно, приложение подключится к базе данных.

## Пересоздание базы данных

Если нужно пересоздать базу данных с нуля:

1. Раскомментируйте строки DROP TABLE в начале скрипта `init_database.sql`
2. Выполните скрипт заново

⚠️ **Внимание:** Это удалит все данные!

## Решение проблем

### Ошибка: extension "uuid-ossp" does not exist

Установите расширение:

```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
```

### Ошибка: permission denied

Убедитесь, что пользователь имеет права на создание расширений:

```sql
GRANT ALL PRIVILEGES ON DATABASE requirements_db TO requirements_user;
```

### Ошибка подключения из приложения

Проверьте:
1. Правильность DATABASE_URL в `.env`
2. Что PostgreSQL запущен
3. Что база данных создана
4. Что пользователь имеет права доступа
