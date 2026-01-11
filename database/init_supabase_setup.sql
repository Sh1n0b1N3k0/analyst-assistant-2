-- Скрипт инициализации для Supabase PostgreSQL
-- Создает необходимые роли перед применением основной схемы

-- Создание роли supabase_admin (если не существует)
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'supabase_admin') THEN
        CREATE ROLE supabase_admin WITH SUPERUSER CREATEDB CREATEROLE LOGIN;
    END IF;
END
$$;

-- Создание базы данных requirements_db (если не существует)
SELECT 'CREATE DATABASE requirements_db'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'requirements_db')\gexec
