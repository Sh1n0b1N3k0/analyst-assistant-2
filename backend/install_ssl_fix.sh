#!/bin/bash

echo "Установка зависимостей Backend с обходом проблем SSL..."
echo ""
echo "ВНИМАНИЕ: Этот скрипт отключает проверку SSL сертификатов."
echo "Используйте только если у вас проблемы с корпоративным прокси."
echo ""

# Проверка наличия Python
if ! command -v python3 &> /dev/null; then
    echo "ОШИБКА: Python3 не найден!"
    echo "Пожалуйста, установите Python 3.8+"
    exit 1
fi

echo "Создание виртуального окружения..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "ОШИБКА: Не удалось создать виртуальное окружение"
    exit 1
fi

echo "Активация виртуального окружения..."
source venv/bin/activate

echo "Настройка переменных окружения для обхода SSL..."
export PIP_TRUSTED_HOST="pypi.org pypi.python.org files.pythonhosted.org"
export PYTHONDONTWRITEBYTECODE=1

echo "Установка зависимостей..."
echo "Обновление pip..."
pip install --upgrade pip --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir

if [ $? -ne 0 ]; then
    echo "ОШИБКА: Не удалось обновить pip"
    exit 1
fi

echo "Установка зависимостей проекта..."
echo "Попытка установки с предкомпилированными пакетами..."
pip install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir --only-binary :all: || \
pip install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir || \
pip install -r requirements_simple.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir

if [ $? -ne 0 ]; then
    echo "ОШИБКА: Не удалось установить зависимости"
    echo ""
    echo "Попробуйте установить зависимости вручную:"
    echo "  source venv/bin/activate"
    echo "  pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir -r requirements.txt"
    exit 1
fi

echo ""
echo "========================================"
echo "Установка завершена успешно!"
echo "========================================"
echo ""
echo "Для запуска сервера выполните:"
echo "  source venv/bin/activate"
echo "  python run.py"
echo ""
