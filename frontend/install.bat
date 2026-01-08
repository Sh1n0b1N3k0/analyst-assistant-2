@echo off
echo Установка зависимостей Frontend...
echo.

REM Проверка наличия Node.js
node --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ========================================
    echo ОШИБКА: Node.js не найден!
    echo ========================================
    echo.
    echo Пожалуйста, установите Node.js 16+ с https://nodejs.org/
    echo.
    echo Инструкции по установке см. в файле INSTALL_NODEJS.md
    echo.
    echo После установки Node.js:
    echo 1. Закройте и снова откройте PowerShell
    echo 2. Выполните: npm install
    echo.
    pause
    exit /b 1
)

REM Проверка наличия npm
npm --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ========================================
    echo ОШИБКА: npm не найден!
    echo ========================================
    echo.
    echo npm обычно устанавливается вместе с Node.js
    echo Если npm не найден, переустановите Node.js
    echo и убедитесь, что опция "Add to PATH" отмечена
    echo.
    echo Инструкции по установке см. в файле INSTALL_NODEJS.md
    echo.
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
