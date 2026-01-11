#!/usr/bin/env python3
"""
Скрипт для ожидания готовности базы данных PostgreSQL
"""
import psycopg2
import sys
import time
import os

# Получаем параметры подключения из переменных окружения
dbname = os.getenv('POSTGRES_DB', 'requirements_db')
user = os.getenv('POSTGRES_USER', 'postgres')
password = os.getenv('POSTGRES_PASSWORD', 'postgres')
host = os.getenv('POSTGRES_HOST', 'db')
port = os.getenv('POSTGRES_PORT', '5432')

max_attempts = 30
wait_interval = 2

print('Waiting for database to be ready...')

for i in range(max_attempts):
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        conn.close()
        print('Database is ready!')
        sys.exit(0)
    except Exception as e:
        print(f'Waiting for database... ({i+1}/{max_attempts}): {e}')
        time.sleep(wait_interval)

print('Database connection failed after 30 attempts')
sys.exit(1)
