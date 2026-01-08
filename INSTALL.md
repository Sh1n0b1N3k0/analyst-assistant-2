# Инструкция по установке зависимостей

## Требования

Перед установкой убедитесь, что у вас установлены:

- **Python 3.8+** - [Скачать Python](https://www.python.org/downloads/)
- **Node.js 16+** и **npm** - [Скачать Node.js](https://nodejs.org/)

## Автоматическая установка

### Windows (PowerShell или Command Prompt)

**Backend:**
```powershell
cd backend
.\install.bat
```

Или просто дважды кликните на файл `install.bat` в проводнике Windows.

> ⚠️ **Важно в PowerShell:** Всегда используйте `.\` перед именем `.bat` файла (например, `.\install.bat`). Это требование безопасности PowerShell. В Command Prompt (cmd) можно использовать просто `install.bat`.

**Frontend:**
```powershell
cd frontend
.\install.bat
```

**Если проблемы с SSL:**
```powershell
cd backend
.\install_ssl_fix.bat
```

> ⚠️ **Важно для Windows:**
> - В **PowerShell** всегда используйте `.\` перед именем `.bat` файла (например, `.\install_ssl_fix.bat`)
> - В **Command Prompt (cmd)** можно использовать просто `install_ssl_fix.bat`
> - Не используйте команду `chmod` - это команда Linux/Mac. В Windows `.bat` файлы уже исполняемые

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

**Если проблемы с SSL:**
```bash
cd backend
chmod +x install_ssl_fix.sh
./install_ssl_fix.sh
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

**Симптомы:**
```
'npm' is not recognized as an internal or external command
```

**Решения:**

1. **Установите Node.js:**
   - Скачайте с [nodejs.org](https://nodejs.org/) (рекомендуется LTS версия)
   - ⚠️ **Важно для Windows:** При установке отметьте опцию **"Add to PATH"**
   - Завершите установку

2. **После установки:**
   - **Закройте и снова откройте PowerShell/терминал** (это необходимо для обновления PATH)
   - Проверьте установку:
     ```powershell
     node --version
     npm --version
     ```

3. **Если Node.js установлен, но не найден:**
   - Добавьте Node.js в PATH вручную
   - Или переустановите Node.js с опцией "Add to PATH"

**Подробная инструкция:** см. [frontend/INSTALL_NODEJS.md](frontend/INSTALL_NODEJS.md)

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

### Ошибка SSL: CERTIFICATE_VERIFY_FAILED

Если вы получаете ошибку `[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed`, это обычно происходит в корпоративных сетях с прокси-серверами.

**Решение 1: Использовать специальный скрипт (рекомендуется)**

**Windows:**
```bash
cd backend
install_ssl_fix.bat
```

**Linux/Mac:**
```bash
cd backend
chmod +x install_ssl_fix.sh
./install_ssl_fix.sh
```

**Решение 2: Ручная установка с обходом SSL**

1. Активируйте виртуальное окружение:
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

2. Установите зависимости с опциями обхода SSL:
   ```bash
   pip install --upgrade pip --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir
   ```
   
3. Если возникают проблемы с компиляцией pydantic-core, используйте упрощенный файл требований:
   ```bash
   pip install -r requirements_simple.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir
   ```
   
   Или попробуйте с предкомпилированными пакетами:
   ```bash
   pip install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir --only-binary :all:
   ```

**Решение 3: Настройка pip.conf (постоянное решение)**

Создайте файл `pip.conf`:

**Windows:** `%APPDATA%\pip\pip.ini`
**Linux/Mac:** `~/.pip/pip.conf`

Добавьте в файл:
```ini
[global]
trusted-host = pypi.org
               pypi.python.org
               files.pythonhosted.org
```

После этого обычная установка `pip install -r requirements.txt` будет работать без ошибок SSL.

**⚠️ Внимание:** Отключение проверки SSL снижает безопасность. Используйте только в доверенных корпоративных сетях.

