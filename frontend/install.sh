#!/bin/bash

echo "Установка зависимостей Frontend..."
echo ""

# Проверка наличия Node.js
if ! command -v node &> /dev/null; then
    echo "ОШИБКА: Node.js не найден!"
    echo "Пожалуйста, установите Node.js 16+ с https://nodejs.org/"
    exit 1
fi

# Проверка наличия npm
if ! command -v npm &> /dev/null; then
    echo "ОШИБКА: npm не найден!"
    echo "npm обычно устанавливается вместе с Node.js"
    exit 1
fi

echo "Версия Node.js:"
node --version
echo "Версия npm:"
npm --version
echo ""

echo "Установка зависимостей..."
npm install

if [ $? -ne 0 ]; then
    echo "ОШИБКА: Не удалось установить зависимости"
    exit 1
fi

echo ""
echo "========================================"
echo "Установка завершена успешно!"
echo "========================================"
echo ""
echo "Для запуска приложения выполните:"
echo "  npm start"
echo ""
