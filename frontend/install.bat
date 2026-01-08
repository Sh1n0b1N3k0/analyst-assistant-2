@echo off
echo Установка зависимостей Frontend...
echo.

REM Проверка наличия Node.js
node --version >nul 2>&1
if errorlevel 1 (
    echo ОШИБКА: Node.js не найден!
    echo Пожалуйста, установите Node.js 16+ с https://nodejs.org/
    pause
    exit /b 1
)

REM Проверка наличия npm
npm --version >nul 2>&1
if errorlevel 1 (
    echo ОШИБКА: npm не найден!
    echo npm обычно устанавливается вместе с Node.js
    pause
    exit /b 1
)

echo Версия Node.js:
node --version
echo Версия npm:
npm --version
echo.

echo Установка зависимостей...
npm install

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
echo Для запуска приложения выполните:
echo   npm start
echo.
pause
