# Быстрое решение проблем с Docker

## Проблема: Frontend не собирается (react-scripts: not found)

### Решение 1: Использовать альтернативный Dockerfile

Измените `docker-compose.yml`, секция frontend:

```yaml
frontend:
  build:
    context: ./frontend
    dockerfile: Dockerfile.alternative
```

Затем:

```bash
docker-compose build frontend --no-cache
docker-compose up -d
```

### Решение 2: Использовать упрощенный docker-compose

```bash
docker-compose -f docker-compose.simple.yml up -d --build
```

### Решение 3: Собрать frontend локально, затем использовать готовую сборку

**Шаг 1:** Соберите frontend локально (если Node.js установлен):

```bash
cd frontend
npm install --legacy-peer-deps
npm run build
```

**Шаг 2:** Измените `frontend/Dockerfile`:

```dockerfile
FROM nginx:alpine

# Копируем уже собранное приложение
COPY build /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

**Шаг 3:** Запустите:

```bash
docker-compose build frontend
docker-compose up -d
```

### Решение 4: Запустить только backend и БД

Если frontend не критичен для начала:

```bash
# Запустить только backend и БД
docker-compose up -d db backend

# Frontend можно запустить локально:
cd frontend
npm install --legacy-peer-deps
npm start
```

## Проверка после исправления

После применения любого решения проверьте:

```bash
# Статус контейнеров
docker-compose ps

# Логи frontend
docker-compose logs frontend

# Проверка доступности
curl http://localhost:3000
```

## Если ничего не помогает

Используйте локальную разработку без Docker для frontend:

1. Запустите только backend и БД в Docker:
   ```bash
   docker-compose up -d db backend
   ```

2. Запустите frontend локально:
   ```bash
   cd frontend
   npm install --legacy-peer-deps
   npm start
   ```

3. Frontend будет доступен на http://localhost:3000
4. Backend будет доступен на http://localhost:8000
