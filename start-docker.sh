#!/bin/bash
# Скрипт для запуска Analyst Assistant в Docker

set -e

echo "========================================"
echo "Запуск Analyst Assistant в Docker"
echo "========================================"
echo ""

# Проверка наличия Docker
if ! command -v docker &> /dev/null; then
    echo "ОШИБКА: Docker не найден!"
    echo "Пожалуйста, установите Docker с https://www.docker.com/"
    exit 1
fi

# Проверка наличия Docker Compose
if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "ОШИБКА: Docker Compose не найден!"
    echo "Пожалуйста, установите Docker Compose"
    exit 1
fi

# Проверка наличия .env файла
if [ ! -f .env ]; then
    echo "Создание файла .env из примера..."
    cp env.docker.example .env
    echo "Файл .env создан. При необходимости отредактируйте его."
    echo ""
fi

echo "Запуск всех сервисов..."
echo ""

# Используем docker compose или docker-compose в зависимости от версии
if docker compose version &> /dev/null; then
    docker compose up -d
else
    docker-compose up -d
fi

if [ $? -ne 0 ]; then
    echo ""
    echo "ОШИБКА: Не удалось запустить сервисы"
    echo "Проверьте логи: docker-compose logs"
    exit 1
fi

echo ""
echo "========================================"
echo "Сервисы запущены!"
echo "========================================"
echo ""
echo "Доступные сервисы:"
echo "  Frontend:  http://localhost:3000"
echo "  Backend:   http://localhost:8000"
echo "  API Docs:  http://localhost:8000/docs"
echo ""
echo "Полезные команды:"
echo "  docker-compose ps          - статус сервисов"
echo "  docker-compose logs -f     - просмотр логов"
echo "  docker-compose down        - остановка сервисов"
echo ""
