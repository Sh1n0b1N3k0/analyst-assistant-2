# Инструкция по установке зависимостей

## Требования

Перед установкой убедитесь, что у вас установлены:

- **Python 3.8+** - [Скачать Python](https://www.python.org/downloads/)
- **Node.js 16+** и **npm** - [Скачать Node.js](https://nodejs.org/)

## Автоматическая установка

### Windows

**Backend:**
```bash
cd backend
install.bat
```

**Frontend:**
```bash
cd frontend
install.bat
```

### Linux/Mac

**Backend:**
```bash
cd backend
chmod +x install.sh
./install.sh
```

**Frontend:**
```bash
cd frontend
chmod +x install.sh
./install.sh
```

## Ручная установка

### Backend

1. Перейдите в папку backend:
```bash
cd backend
```

2. Создайте виртуальное окружение:
```bash
# Windows
python -m venv venv

# Linux/Mac
python3 -m venv venv
```

3. Активируйте виртуальное окружение:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Установите зависимости:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Frontend

1. Перейдите в папку frontend:
```bash
cd frontend
```

2. Установите зависимости:
```bash
npm install
```

## Проверка установки

### Backend

Проверьте, что зависимости установлены:
```bash
cd backend
venv\Scripts\activate  # Windows
# или
source venv/bin/activate  # Linux/Mac

pip list
```

Должны быть установлены:
- fastapi
- uvicorn
- sqlalchemy
- pydantic
- и другие зависимости

### Frontend

Проверьте, что зависимости установлены:
```bash
cd frontend
npm list --depth=0
```

Должны быть установлены:
- react
- react-dom
- typescript
- axios
- и другие зависимости

## Запуск после установки

### Backend
```bash
cd backend
venv\Scripts\activate  # Windows
python run.py
```

### Frontend
```bash
cd frontend
npm start
```

## Решение проблем

### Python не найден

1. Убедитесь, что Python установлен
2. Добавьте Python в PATH
3. Перезапустите терминал
4. Попробуйте использовать `python3` вместо `python` (Linux/Mac)

### Node.js не найден

1. Убедитесь, что Node.js установлен
2. Добавьте Node.js в PATH
3. Перезапустите терминал

### Ошибки при установке зависимостей

1. Обновите pip/npm:
   ```bash
   pip install --upgrade pip
   npm install -g npm@latest
   ```

2. Очистите кэш:
   ```bash
   pip cache purge
   npm cache clean --force
   ```

3. Попробуйте установить зависимости заново
