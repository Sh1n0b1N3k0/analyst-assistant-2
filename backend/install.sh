#!/bin/bash

echo "Установка зависимостей Backend..."
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

echo "Установка зависимостей..."
echo "Обновление pip..."
pip install --upgrade pip --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org || \
pip install --upgrade pip --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir

echo "Установка зависимостей проекта..."
pip install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org || \
pip install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir

if [ $? -ne 0 ]; then
    echo "ОШИБКА: Не удалось установить зависимости"
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
