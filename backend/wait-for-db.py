#!/usr/bin/env python3
"""
Скрипт для ожидания готовности локальной базы данных Supabase
"""
import psycopg2
import sys
import time
import os

# Получаем параметры подключения из переменных окружения
dbname = os.getenv('POSTGRES_DB', 'postgres')
user = os.getenv('POSTGRES_USER', 'postgres')
password = os.getenv('POSTGRES_PASSWORD', 'postgres')
host = os.getenv('POSTGRES_HOST', 'supabase-db')
port = os.getenv('POSTGRES_PORT', '5432')

max_attempts = 30
wait_interval = 2

print('Waiting for Supabase database to be ready...')

for i in range(max_attempts):
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port,
            connect_timeout=5
        )
        conn.close()
        print('Supabase database is ready!')
        sys.exit(0)
    except psycopg2.OperationalError as e:
        print(f'Waiting for database... ({i+1}/{max_attempts}): {e}')
        time.sleep(wait_interval)
    except Exception as e:
        print(f'Unexpected error: {e}')
        time.sleep(wait_interval)

print('Database connection failed after 30 attempts')
sys.exit(1)
