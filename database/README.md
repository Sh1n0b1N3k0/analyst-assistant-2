# База данных

База данных для хранения требований в стандарте SRS.

## Структура

База данных использует SQLAlchemy ORM и автоматически создается при первом запуске приложения.

### Таблицы

#### requirements
Основная таблица для хранения требований:
- `id` - первичный ключ
- `requirement_id` - уникальный идентификатор требования
- `title` - название требования
- `description` - описание требования
- `priority` - приоритет (High, Medium, Low)
- `status` - статус (Draft, Approved, Rejected, etc.)
- `category` - категория требования
- `source` - источник требования
- `stakeholder` - заинтересованное лицо
- `created_at` - дата создания
- `updated_at` - дата обновления

#### requirement_attributes
Таблица для хранения дополнительных атрибутов требований:
- `id` - первичный ключ
- `requirement_id` - внешний ключ к requirements
- `attribute_name` - название атрибута
- `attribute_value` - значение атрибута
- `created_at` - дата создания

## Настройка

По умолчанию используется SQLite (`requirements.db`). Для продакшн окружения рекомендуется использовать PostgreSQL.

Для изменения базы данных установите переменную окружения:
```
DATABASE_URL=postgresql://user:password@localhost/requirements_db
```
