# Быстрый старт

## Шаг 1: Установите необходимые инструменты

### Python 3.8+
- Скачайте с [python.org](https://www.python.org/downloads/)
- ⚠️ При установке отметьте **"Add Python to PATH"**

### Node.js 16+
- Скачайте LTS версию с [nodejs.org](https://nodejs.org/)
- ⚠️ При установке отметьте **"Add to PATH"**
- После установки **закройте и снова откройте PowerShell**

Проверьте установку:
```powershell
python --version
node --version
npm --version
```

## Шаг 2: Установите зависимости Backend

**PowerShell:**
```powershell
cd backend
.\install_ssl_fix.bat
```

Или просто дважды кликните на `install_ssl_fix.bat` в проводнике.

## Шаг 3: Установите зависимости Frontend

**Сначала установите Node.js** (если еще не установлен):
- См. [frontend/INSTALL_NODEJS.md](frontend/INSTALL_NODEJS.md)

**Затем установите зависимости:**
```powershell
cd frontend
npm install
```

## Шаг 4: Запустите приложение

### Запуск Backend (в первом окне PowerShell):

```powershell
cd backend
venv\Scripts\activate
python run.py
```

Backend будет доступен на http://localhost:8000

### Запуск Frontend (во втором окне PowerShell):

```powershell
cd frontend
npm start
```

Frontend будет доступен на http://localhost:3000

## Готово! 🎉

Откройте браузер и перейдите на http://localhost:3000

## Решение проблем

- **Python не найден:** См. [REQUIREMENTS.md](REQUIREMENTS.md)
- **Node.js не найден:** См. [frontend/INSTALL_NODEJS.md](frontend/INSTALL_NODEJS.md)
- **Ошибки SSL:** Используйте `install_ssl_fix.bat` вместо `install.bat`
- **Другие проблемы:** См. [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)
