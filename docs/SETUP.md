# Инструкция по установке и запуску

## Требования

- Python 3.8+
- Node.js 16+
- npm или yarn

## Установка Backend

1. Перейдите в папку backend:
```bash
cd backend
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
```

3. Активируйте виртуальное окружение:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Установите зависимости:
```bash
pip install -r requirements.txt
```

5. Создайте файл `.env` в корне проекта (или скопируйте `.env.example`):
```bash
DATABASE_URL=sqlite:///./requirements.db
```

6. Запустите сервер:
```bash
python run.py
```

Или:
```bash
uvicorn main:app --reload
```

API будет доступен по адресу: http://localhost:8000

Документация API (Swagger): http://localhost:8000/docs

## Установка Frontend

1. Перейдите в папку frontend:
```bash
cd frontend
```

2. Установите зависимости:
```bash
npm install
```

3. Запустите dev сервер:
```bash
npm start
```

Приложение будет доступно по адресу: http://localhost:3000

## Структура проекта

```
analyst-assistant-2/
├── backend/              # Backend приложение
│   ├── main.py          # Главный файл приложения
│   ├── database.py      # Настройка БД
│   ├── models/          # Модели данных
│   ├── schemas/         # Pydantic схемы
│   ├── routers/         # API роутеры
│   └── requirements.txt # Зависимости Python
├── frontend/            # Frontend приложение
│   ├── src/
│   │   ├── App.tsx     # Главный компонент
│   │   └── components/ # React компоненты
│   └── package.json    # Зависимости Node.js
├── database/            # Документация БД
└── docs/                # Документация проекта
```

## Использование

1. Запустите backend сервер
2. Запустите frontend приложение
3. Откройте браузер и перейдите на http://localhost:3000
4. Используйте форму импорта для добавления требований
5. Используйте форму экспорта для выгрузки требований

## База данных

По умолчанию используется SQLite. База данных создается автоматически при первом запуске приложения.

Для использования PostgreSQL измените `DATABASE_URL` в файле `.env`:
```
DATABASE_URL=postgresql://user:password@localhost/requirements_db
```
