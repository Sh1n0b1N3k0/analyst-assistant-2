#!/bin/bash
# Скрипт для остановки Analyst Assistant в Docker

echo "Остановка Analyst Assistant..."

if docker compose version &> /dev/null; then
    docker compose down
else
    docker-compose down
fi

echo ""
echo "Сервисы остановлены."
