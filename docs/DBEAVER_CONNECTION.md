# Подключение DBeaver к локальной базе данных

## Параметры подключения

Для подключения DBeaver к локальной базе данных Supabase (PostgreSQL) используйте следующие параметры:

### Основные параметры:

- **Тип БД**: PostgreSQL
- **Хост**: `localhost`
- **Порт**: `5432`
- **База данных**: `requirements_db` (основная база с таблицами) или `postgres` (системная база)
- **Пользователь**: `postgres`
- **Пароль**: `postgres` (или значение из вашего `.env` файла)

## Пошаговая инструкция

### Шаг 1: Убедитесь, что база данных запущена

```bash
docker-compose ps supabase-db
```

Контейнер должен быть в статусе `Up` и `healthy`.

### Шаг 2: Откройте DBeaver

1. Запустите DBeaver
2. В меню выберите **Database** > **New Database Connection** (или нажмите `Ctrl+Shift+N`)

### Шаг 3: Выберите тип базы данных

1. В списке выберите **PostgreSQL**
2. Нажмите **Next**

### Шаг 4: Заполните параметры подключения

На вкладке **Main**:

- **Host**: `localhost`
- **Port**: `5432`
- **Database**: `requirements_db` (основная база с таблицами проекта)
- **Username**: `postgres`
- **Password**: `postgres`

> ⚠️ **Важно:** Если вы изменили пароль в файле `.env`, используйте тот пароль, который указан там.

### Шаг 5: Настройте дополнительные параметры (опционально)

На вкладке **Driver properties** можно оставить значения по умолчанию.

### Шаг 6: Тест подключения

1. Нажмите кнопку **Test Connection**
2. Если драйвер PostgreSQL не установлен, DBeaver предложит его скачать - нажмите **Download**
3. После успешного теста должно появиться сообщение: **Connected**

### Шаг 7: Сохраните подключение

1. Нажмите **Finish**
2. Подключение появится в дереве баз данных слева

## Проверка подключения

После подключения вы должны увидеть:

- Базу данных `requirements_db` с таблицами проекта
- Схему `public` с таблицами:
  - `users`
  - `roles`
  - `permissions`
  - `projects`
  - `requirements`
  - `system_components`
  - `ui_elements`
  - И другие таблицы (всего 28 таблиц)

## Выполнение SQL запросов

1. Правой кнопкой мыши на базе данных `requirements_db` > **SQL Editor** > **New SQL Script**
2. Или используйте горячую клавишу `Ctrl+]`

Пример запроса:

```sql
-- Проверка количества таблиц
SELECT COUNT(*) FROM information_schema.tables 
WHERE table_schema = 'public';

-- Просмотр всех требований
SELECT * FROM requirements LIMIT 10;
```

## Troubleshooting

### Ошибка: "password authentication failed for user postgres"

**Причина:** Пароль в DBeaver не совпадает с паролем в базе данных.

**Решение:**

1. **Проверьте пароль в файле `.env`:**
   ```bash
   # В Windows PowerShell
   Get-Content .env | Select-String "POSTGRES_PASSWORD"
   ```

2. **Используйте пароль из `.env` файла в DBeaver**

3. **Если пароль не работает, установите его заново:**
   ```bash
   docker-compose exec supabase-db psql -U postgres -d postgres -c "ALTER USER postgres WITH PASSWORD 'postgres';"
   ```

4. **Проверьте подключение:**
   ```bash
   docker-compose exec supabase-db psql -U postgres -d requirements_db -c "SELECT 1;"
   ```

Подробнее: [DBEAVER_PASSWORD_FIX.md](DBEAVER_PASSWORD_FIX.md)

### Ошибка: "Connection refused"

**Причина:** База данных не запущена или порт занят.

**Решение:**
```bash
# Проверьте статус контейнера
docker-compose ps supabase-db

# Если контейнер не запущен, запустите его
docker-compose up -d supabase-db
```

### Ошибка: "password authentication failed"

**Причина:** Неправильный пароль.

**Решение:**
1. Проверьте файл `.env` в корне проекта
2. Убедитесь, что используете правильный пароль из `POSTGRES_PASSWORD`
3. Если файла `.env` нет, используйте пароль по умолчанию: `postgres`

### Ошибка: "database does not exist"

**Причина:** База данных не инициализирована.

**Решение:**
```bash
# Пересоздайте базу данных
docker-compose down -v
docker-compose up -d supabase-db

# Дождитесь инициализации (проверьте логи)
docker-compose logs supabase-db
```

### DBeaver не может скачать драйвер

**Решение:**
1. Проверьте подключение к интернету
2. Или скачайте драйвер вручную:
   - Перейдите в **Window** > **Preferences** > **DBeaver** > **Drivers**
   - Найдите PostgreSQL
   - Нажмите **Edit** > **Download/Update**

## Альтернативные способы подключения

### Через psql (командная строка)

```bash
# Подключение через docker-compose
docker-compose exec supabase-db psql -U postgres -d postgres

# Или напрямую (если psql установлен локально)
psql -h localhost -p 5432 -U postgres -d postgres
```

Пароль: `postgres`

### Через pgAdmin

Используйте те же параметры подключения, что и для DBeaver.

## Полезные SQL запросы

```sql
-- Список всех таблиц
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public'
ORDER BY table_name;

-- Информация о схеме базы данных
SELECT 
    schemaname,
    tablename,
    tableowner
FROM pg_tables
WHERE schemaname = 'public'
ORDER BY tablename;

-- Размер базы данных
SELECT pg_size_pretty(pg_database_size('requirements_db'));

-- Количество записей в основных таблицах
SELECT 
    'users' as table_name, COUNT(*) as count FROM users
UNION ALL
SELECT 'requirements', COUNT(*) FROM requirements
UNION ALL
SELECT 'projects', COUNT(*) FROM projects
UNION ALL
SELECT 'system_components', COUNT(*) FROM system_components;
```
