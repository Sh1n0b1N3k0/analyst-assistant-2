@echo off
echo Установка зависимостей Backend с обходом проблем SSL...
echo.
echo ВНИМАНИЕ: Этот скрипт отключает проверку SSL сертификатов.
echo Используйте только если у вас проблемы с корпоративным прокси.
echo.

REM Проверка наличия Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ОШИБКА: Python не найден!
    echo Пожалуйста, установите Python 3.8+ с https://www.python.org/
    pause
    exit /b 1
)

echo Создание виртуального окружения...
python -m venv venv
if errorlevel 1 (
    echo ОШИБКА: Не удалось создать виртуальное окружение
    pause
    exit /b 1
)

echo Активация виртуального окружения...
call venv\Scripts\activate.bat

echo Настройка переменных окружения для обхода SSL...
set PIP_TRUSTED_HOST=pypi.org pypi.python.org files.pythonhosted.org
set PYTHONDONTWRITEBYTECODE=1

echo Установка зависимостей...
echo Обновление pip...
pip install --upgrade pip --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir

if errorlevel 1 (
    echo ОШИБКА: Не удалось обновить pip
    pause
    exit /b 1
)

echo Установка зависимостей проекта...
echo Попытка установки с предкомпилированными пакетами...
pip install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir --only-binary :all:
if errorlevel 1 (
    echo Попытка установки без ограничений на бинарные пакеты...
    pip install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir
)
if errorlevel 1 (
    echo Попытка установки с упрощенными требованиями...
    pip install -r requirements_simple.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir
)

if errorlevel 1 (
    echo ОШИБКА: Не удалось установить зависимости
    echo.
    echo Попробуйте установить зависимости вручную:
    echo   venv\Scripts\activate
    echo   pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir -r requirements.txt
    pause
    exit /b 1
)

echo.
echo ========================================
echo Установка завершена успешно!
echo ========================================
echo.
echo Для запуска сервера выполните:
echo   venv\Scripts\activate
echo   python run.py
echo.
pause
