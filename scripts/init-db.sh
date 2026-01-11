#!/bin/bash
# Скрипт для инициализации базы данных в Docker контейнере

set -e

echo "Waiting for PostgreSQL to be ready..."

# Ждем пока PostgreSQL будет готов
until docker-compose exec -T db pg_isready -U postgres > /dev/null 2>&1; do
  echo "PostgreSQL is unavailable - sleeping"
  sleep 2
done

echo "PostgreSQL is ready!"

# Проверяем, существует ли база данных
DB_EXISTS=$(docker-compose exec -T db psql -U postgres -tAc "SELECT 1 FROM pg_database WHERE datname='requirements_db'" || echo "")

if [ "$DB_EXISTS" != "1" ]; then
    echo "Creating database..."
    docker-compose exec -T db psql -U postgres -c "CREATE DATABASE requirements_db;"
fi

# Применяем скрипт инициализации
echo "Applying initialization script..."
docker-compose exec -T db psql -U postgres -d requirements_db -f /docker-entrypoint-initdb.d/init_database.sql

echo "Database initialized successfully!"
