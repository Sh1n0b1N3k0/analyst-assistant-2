# База данных

База данных для хранения требований в стандарте SRS.

## Структура

База данных использует PostgreSQL и инициализируется через SQL скрипт.

### Инициализация базы данных

Для инициализации базы данных используйте скрипт `init_database.sql`:

```bash
psql -U postgres -d requirements_db -f init_database.sql
```

Или через psql интерактивно:

```bash
psql -U postgres -d requirements_db
\i init_database.sql
```

### Версия схемы

Текущая версия схемы: **1.4.1**

## Основные таблицы

### RBAC (Пользователи и права доступа)
- `users` - Пользователи системы
- `roles` - Роли пользователей
- `permissions` - Права доступа
- `user_roles` - Связь пользователей с ролями
- `role_permissions` - Связь ролей с правами

### Проекты
- `projects` - Проекты (контекст для всех артефактов)

### Требования
- `requirements` - Требования по ISO/IEC/IEEE 29148
- `requirement_relationships` - Связи между требованиями

### Системные компоненты
- `system_capabilities` - Функции системы
- `system_components` - Системные компоненты
- `component_dependencies` - Зависимости компонентов
- `component_requirement_links` - Трассировка компонент ↔ требования
- `component_ui_links` - Трассировка компонент ↔ UI

### UI элементы
- `ui_elements` - Элементы интерфейса

### Дополнительные таблицы
- `change_history` - История изменений и аудит
- `comments` - Комментарии и обсуждения
- `test_cases` - Тест-кейсы и верификация
- `documents` - Документация и артефакты
- `risks` - Риски и проблемы
- `metrics` - Метрики и KPI
- `external_systems` - Внешние системы и интеграции
- `deployments` - Развертывание и окружения
- `entities` - Сущности системы
- `entity_relationships` - Связи между сущностями
- `requirement_entities` - Связь требований с сущностями
- `component_entities` - Связь компонентов с сущностями
- `ui_entity_links` - Связь UI элементов с сущностями
- `message_broker_details` - Детали брокера сообщений

## Настройка

### PostgreSQL

Для продакшн окружения используется PostgreSQL.

1. Установите PostgreSQL
2. Создайте базу данных:
   ```sql
   CREATE DATABASE requirements_db;
   ```
3. Примените скрипт инициализации:
   ```bash
   psql -U postgres -d requirements_db -f database/init_database.sql
   ```

### Переменные окружения

Установите переменную окружения в `.env`:

```env
DATABASE_URL=postgresql://user:password@localhost/requirements_db
```

### SQLite (для разработки)

Для разработки можно использовать SQLite, но рекомендуется использовать PostgreSQL для полной функциональности.

```env
DATABASE_URL=sqlite:///./requirements.db
```

⚠️ **Внимание:** SQLite не поддерживает все функции PostgreSQL (UUID, JSONB, массивы, полнотекстовый поиск и т.д.), поэтому некоторые функции могут не работать.

## Представления (Views)

Скрипт создает следующие представления для удобных запросов:

- `requirements_view` - Требования с информацией о создателе и исполнителе
- `components_health_view` - Компоненты с информацией о здоровье
- `requirement_traceability_view` - Трассировка требований

## Расширения PostgreSQL

Скрипт использует следующие расширения:
- `uuid-ossp` - Генерация UUID
- `pg_trgm` - Полнотекстовый поиск

## Роли по умолчанию

После инициализации создаются следующие роли:
- `admin` - Администратор с полным доступом
- `analyst` - Бизнес-аналитик
- `reviewer` - Ревьюер
- `developer` - Разработчик
- `viewer` - Просмотр (только чтение)
