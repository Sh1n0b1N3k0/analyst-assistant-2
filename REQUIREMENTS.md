# Требования к системе

## Обязательные требования

### 1. Python 3.8 или выше

**Проверка установки:**
```bash
python --version
# или
python3 --version
```

**Установка:**
- Windows: [Скачать Python](https://www.python.org/downloads/)
  - ⚠️ **Важно:** При установке отметьте опцию "Add Python to PATH"
- Linux: `sudo apt-get install python3 python3-pip python3-venv` (Ubuntu/Debian)
- Mac: `brew install python3` или скачать с [python.org](https://www.python.org/downloads/)

### 2. Node.js 16 или выше и npm

**Проверка установки:**
```bash
node --version
npm --version
```

**Установка:**
- Windows/Linux/Mac: [Скачать Node.js](https://nodejs.org/)
  - ⚠️ **Важно для Windows:** При установке отметьте опцию **"Add to PATH"** (добавить в PATH)
  - npm устанавливается автоматически вместе с Node.js
  - После установки **закройте и снова откройте PowerShell/терминал**
  
**Подробная инструкция для Windows:** см. [frontend/INSTALL_NODEJS.md](frontend/INSTALL_NODEJS.md)

## Рекомендуемые инструменты

### Git
Для работы с репозиторием (если еще не установлен):
- Windows/Linux/Mac: [Скачать Git](https://git-scm.com/downloads)

### Редактор кода
- Visual Studio Code: [Скачать VS Code](https://code.visualstudio.com/)
- PyCharm (для Python разработки)
- WebStorm (для React разработки)

## Проверка готовности системы

Выполните следующие команды для проверки:

```bash
# Python
python --version
pip --version

# Node.js
node --version
npm --version

# Git (опционально)
git --version
```

Если все команды выполняются успешно, система готова к установке зависимостей проекта.

## Следующие шаги

После установки всех требований:

1. **Установите зависимости Backend:**
   ```bash
   cd backend
   install.bat  # Windows
   # или
   ./install.sh  # Linux/Mac
   ```

2. **Установите зависимости Frontend:**
   ```bash
   cd frontend
   install.bat  # Windows
   # или
   ./install.sh  # Linux/Mac
   ```

Подробные инструкции см. в [INSTALL.md](INSTALL.md)
