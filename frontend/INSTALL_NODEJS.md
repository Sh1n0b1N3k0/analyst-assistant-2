# Установка Node.js для Windows

## Проблема: npm не найден

Если вы получили ошибку:
```
'npm' is not recognized as an internal or external command
```

Это означает, что Node.js не установлен или не добавлен в PATH.

## Решение: Установка Node.js

### Шаг 1: Скачайте Node.js

1. Перейдите на https://nodejs.org/
2. Скачайте **LTS версию** (рекомендуется)
3. Выберите установщик для Windows (.msi файл)

### Шаг 2: Установите Node.js

1. Запустите скачанный установщик
2. Следуйте инструкциям установщика
3. ⚠️ **ВАЖНО:** Убедитесь, что отмечена опция **"Add to PATH"** (добавить в PATH)
4. Завершите установку

### Шаг 3: Проверьте установку

Закройте и снова откройте PowerShell, затем выполните:

```powershell
node --version
npm --version
```

Должны отобразиться версии Node.js и npm.

### Шаг 4: Установите зависимости frontend

После установки Node.js:

```powershell
cd C:\Users\sergey.tiunov\GIT\analyst-assistant-2\frontend
npm install
```

### Шаг 5: Запустите frontend

```powershell
npm start
```

## Альтернатива: Использование nvm (Node Version Manager)

Если вы хотите управлять несколькими версиями Node.js:

1. Установите nvm-windows: https://github.com/coreybutler/nvm-windows
2. Установите Node.js через nvm:
   ```powershell
   nvm install lts
   nvm use lts
   ```

## Проверка после установки

После установки Node.js и npm, выполните:

```powershell
# Проверка версий
node --version
npm --version

# Переход в папку frontend
cd C:\Users\sergey.tiunov\GIT\analyst-assistant-2\frontend

# Установка зависимостей
npm install

# Запуск приложения
npm start
```

Приложение будет доступно на http://localhost:3000
