# Быстрый старт с Docker

## Предварительные требования

- Docker 20.10+
- Docker Compose 2.0+

## Запуск за 3 шага

### Шаг 1: Настройка переменных окружения

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

Или просто запустите `start-docker.bat` (Windows) / `start-docker.sh` (Linux/Mac) - скрипт создаст файл автоматически.

При необходимости отредактируйте `.env` файл (по умолчанию настройки подходят для разработки).

### Шаг 2: Запуск системы

```bash
docker-compose up -d
```

Эта команда:
- ✅ Соберет образы для backend и frontend
- ✅ Запустит PostgreSQL базу данных
- ✅ Автоматически инициализирует базу данных
- ✅ Запустит backend API
- ✅ Запустит frontend

### Шаг 3: Проверка

Откройте в браузере:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Документация**: http://localhost:8000/docs

## Полезные команды

### Просмотр статуса

```bash
docker-compose ps
```

### Просмотр логов

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

### Остановка

```bash
docker-compose down
```

### Пересборка после изменений

```bash
docker-compose up -d --build
```

### Очистка (удаление всех данных)

```bash
docker-compose down -v
```

## Что дальше?

- Подробная документация: [docs/DOCKER.md](docs/DOCKER.md)
- Разработка в Docker: см. раздел "Разработка" в [docs/DOCKER.md](docs/DOCKER.md)
- Production развертывание: см. раздел "Production развертывание" в [docs/DOCKER.md](docs/DOCKER.md)
