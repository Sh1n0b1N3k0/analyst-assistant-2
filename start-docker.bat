@echo off
echo ========================================
echo Запуск Analyst Assistant в Docker
echo ========================================
echo.

REM Проверка наличия Docker
docker --version >nul 2>&1
if errorlevel 1 (
    echo ОШИБКА: Docker не найден!
    echo Пожалуйста, установите Docker Desktop с https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)

REM Проверка наличия Docker Compose
docker-compose --version >nul 2>&1
if errorlevel 1 (
    echo ОШИБКА: Docker Compose не найден!
    echo Пожалуйста, установите Docker Desktop
    pause
    exit /b 1
)

REM Проверка наличия .env файла
if not exist .env (
    if exist env.docker.example (
        echo Создание файла .env из примера...
        copy env.docker.example .env >nul
        echo Файл .env создан. При необходимости отредактируйте его.
        echo.
    ) else (
        echo ВНИМАНИЕ: Файл env.docker.example не найден!
        echo Создайте файл .env вручную с необходимыми переменными.
        echo.
    )
)

echo Запуск всех сервисов...
echo.
docker-compose up -d

if errorlevel 1 (
    echo.
    echo ОШИБКА: Не удалось запустить сервисы
    echo Проверьте логи: docker-compose logs
    pause
    exit /b 1
)

echo.
echo ========================================
echo Сервисы запущены!
echo ========================================
echo.
echo Доступные сервисы:
echo   Frontend:  http://localhost:3000
echo   Backend:   http://localhost:8000
echo   API Docs:  http://localhost:8000/docs
echo.
echo Полезные команды:
echo   docker-compose ps          - статус сервисов
echo   docker-compose logs -f     - просмотр логов
echo   docker-compose down        - остановка сервисов
echo.
pause
