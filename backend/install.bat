@echo off
echo Установка зависимостей Backend...
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

echo Установка зависимостей...
echo Обновление pip...
pip install --upgrade pip --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org
if errorlevel 1 (
    echo Попытка установки без проверки SSL сертификатов...
    pip install --upgrade pip --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir
)

echo Установка зависимостей проекта...
pip install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org
if errorlevel 1 (
    echo Попытка установки без проверки SSL сертификатов и кэша...
    pip install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir
)

if errorlevel 1 (
    echo ОШИБКА: Не удалось установить зависимости
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
