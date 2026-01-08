# API Документация

## Базовый URL
```
http://localhost:8000
```

## Endpoints

### Импорт требований

#### POST /api/import/json
Импорт требований из JSON файла.

**Request:**
- Content-Type: `multipart/form-data`
- Body: файл JSON

**Пример JSON:**
```json
[
  {
    "requirement_id": "REQ-001",
    "title": "Название требования",
    "description": "Описание требования",
    "priority": "High",
    "status": "Draft",
    "category": "Функциональные",
    "source": "Заказчик",
    "stakeholder": "Иван Иванов",
    "attributes": [
      {
        "attribute_name": "Версия",
        "attribute_value": "1.0"
      }
    ]
  }
]
```

#### POST /api/import/csv
Импорт требований из CSV файла.

**Request:**
- Content-Type: `multipart/form-data`
- Body: файл CSV

**Пример CSV заголовков:**
```
requirement_id,title,description,priority,status,category,source,stakeholder
```

#### POST /api/import/manual
Ручной импорт одного требования.

**Request Body:**
```json
{
  "requirement_id": "REQ-001",
  "title": "Название требования",
  "description": "Описание требования",
  "priority": "High",
  "status": "Draft",
  "category": "Функциональные",
  "source": "Заказчик",
  "stakeholder": "Иван Иванов",
  "attributes": []
}
```

### Экспорт требований

#### GET /api/export/json
Получить требования в JSON формате.

**Query Parameters:**
- `category` (optional): фильтр по категории
- `status` (optional): фильтр по статусу
- `priority` (optional): фильтр по приоритету

#### GET /api/export/json/file
Скачать требования в JSON файле.

**Query Parameters:** (те же, что и выше)

#### GET /api/export/csv/file
Скачать требования в CSV файле.

**Query Parameters:** (те же, что и выше)

#### GET /api/export/filters
Получить доступные значения для фильтров.

**Response:**
```json
{
  "categories": ["Функциональные", "Нефункциональные"],
  "statuses": ["Draft", "Approved", "Rejected"],
  "priorities": ["High", "Medium", "Low"]
}
```

### Служебные endpoints

#### GET /
Информация об API.

#### GET /api/health
Проверка здоровья API.
