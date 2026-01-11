# Запуск в Docker на Windows

## Самый простой способ

Просто запустите скрипт:

```cmd
start-docker.bat
```

Скрипт автоматически:
- ✅ Проверит наличие Docker
- ✅ Создаст файл `.env` если его нет
- ✅ Запустит все сервисы

## Ручной запуск

### Шаг 1: Создание файла .env

**Command Prompt (cmd):**
```cmd
copy env.docker.example .env
```

**PowerShell:**
```powershell
Copy-Item env.docker.example .env
```

### Шаг 2: Запуск сервисов

```cmd
docker-compose up -d
```

### Шаг 3: Проверка

```cmd
docker-compose ps
```

## Остановка

**Используйте скрипт:**
```cmd
stop-docker.bat
```

**Или вручную:**
```cmd
docker-compose down
```

## Просмотр логов

```cmd
docker-compose logs -f
```

## Доступ к сервисам

После запуска откройте в браузере:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Документация**: http://localhost:8000/docs

## Решение проблем

### Docker не найден

Установите Docker Desktop:
https://www.docker.com/products/docker-desktop

### Порт уже занят

Измените порты в файле `.env`:
```env
BACKEND_PORT=8001
FRONTEND_PORT=3001
POSTGRES_PORT=5433
```

### Ошибки при запуске

Проверьте логи:
```cmd
docker-compose logs
```

Пересоберите образы:
```cmd
docker-compose build --no-cache
docker-compose up -d
```
