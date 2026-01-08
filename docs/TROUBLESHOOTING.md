# Решение проблем

## Проблемы с установкой зависимостей

### Ошибка SSL: CERTIFICATE_VERIFY_FAILED

**Симптомы:**
```
httpx.ConnectError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: 
self-signed certificate in certificate chain
```

**Причина:**
Эта ошибка возникает в корпоративных сетях, где используются прокси-серверы с самоподписанными SSL сертификатами.

**Решения:**

#### 1. Использовать специальный скрипт (самый простой способ)

**Windows (PowerShell или Command Prompt):**
```powershell
cd backend
.\install_ssl_fix.bat
```

Или просто дважды кликните на файл `install_ssl_fix.bat` в проводнике Windows.

> ⚠️ **Важно:** В Windows не используйте команду `chmod` - это команда Linux/Mac. В Windows `.bat` файлы уже исполняемые.

**Linux/Mac:**
```bash
cd backend
chmod +x install_ssl_fix.sh
./install_ssl_fix.sh
```

#### 2. Ручная установка с параметрами

```bash
# Активируйте виртуальное окружение
venv\Scripts\activate  # Windows
# или
source venv/bin/activate  # Linux/Mac

# Установите зависимости
pip install --upgrade pip --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir
pip install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir
```

#### 3. Настройка pip.conf (постоянное решение)

Создайте файл конфигурации pip:

**Windows:**
- Путь: `%APPDATA%\pip\pip.ini`
- Создайте папку `pip` в `%APPDATA%`, если её нет
- Создайте файл `pip.ini` со следующим содержимым:

```ini
[global]
trusted-host = pypi.org
               pypi.python.org
               files.pythonhosted.org
```

**Linux/Mac:**
- Путь: `~/.pip/pip.conf`
- Создайте файл со следующим содержимым:

```ini
[global]
trusted-host = pypi.org
               pypi.python.org
               files.pythonhosted.org
```

После настройки pip.conf обычная команда `pip install -r requirements.txt` будет работать без ошибок SSL.

**⚠️ Важно:** Отключение проверки SSL снижает безопасность. Используйте только в доверенных корпоративных сетях.

### Ошибка компиляции pydantic-core (требуется Rust)

**Симптомы:**
```
error: metadata-generation-failed
pydantic-core requires Rust and Cargo to compile extensions
```

**Причина:**
Некоторые версии `pydantic-core` требуют компиляции из исходников, для чего нужен Rust.

**Решения:**

#### 1. Использовать предкомпилированные пакеты (рекомендуется)

```bash
# Активируйте виртуальное окружение
venv\Scripts\activate  # Windows
# или
source venv/bin/activate  # Linux/Mac

# Установите с флагом --only-binary
pip install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir --only-binary :all:
```

#### 2. Использовать упрощенные требования

```bash
pip install -r requirements_simple.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir
```

Это установит последние совместимые версии пакетов с предкомпилированными wheels.

#### 3. Установить Rust (если нужна компиляция)

1. Установите Rust с [rustup.rs](https://rustup.rs/)
2. Добавьте Rust в PATH
3. Перезапустите терминал
4. Попробуйте установить зависимости снова

### Python не найден

**Симптомы:**
```
'python' is not recognized as an internal or external command
```

**Решения:**

1. Убедитесь, что Python установлен:
   - Проверьте через Microsoft Store (Windows)
   - Или скачайте с [python.org](https://www.python.org/downloads/)

2. Добавьте Python в PATH:
   - Windows: При установке отметьте "Add Python to PATH"
   - Или добавьте вручную в переменные окружения

3. Используйте полный путь к Python:
   ```bash
   C:\Python39\python.exe -m venv venv
   ```

4. Попробуйте `python3` вместо `python` (Linux/Mac)

### Конфликт версий TypeScript при установке frontend

**Симптомы:**
```
npm error ERESOLVE could not resolve
npm error Conflicting peer dependency: typescript@4.9.5
```

**Причина:**
`react-scripts@5.0.1` поддерживает только TypeScript версий 3.2.1 или 4.x, но в `package.json` указана версия 5.x.

**Решения:**

#### 1. Использовать TypeScript 4.9.5 (рекомендуется)

Версия TypeScript в `package.json` уже обновлена. Просто выполните:

```powershell
npm install
```

#### 2. Использовать --legacy-peer-deps

Если нужно использовать TypeScript 5:

```powershell
npm install --legacy-peer-deps
```

⚠️ **Внимание:** Это может привести к несовместимостям.

**Подробнее:** см. [frontend/INSTALL_TYPESCRIPT_FIX.md](../frontend/INSTALL_TYPESCRIPT_FIX.md)

### Node.js не найден

**Симптомы:**
```
'node' is not recognized as an internal or external command
```

**Решения:**

1. Установите Node.js с [nodejs.org](https://nodejs.org/)
2. Добавьте Node.js в PATH
3. Перезапустите терминал
4. Проверьте установку: `node --version`

### Ошибки при создании виртуального окружения

**Симптомы:**
```
Error: [Errno 2] No such file or directory
```

**Решения:**

1. Убедитесь, что вы находитесь в правильной директории
2. Проверьте права доступа к папке
3. Попробуйте создать виртуальное окружение с полным путем:
   ```bash
   python -m venv C:\Users\YourName\GIT\analyst-assistant-2\backend\venv
   ```

### Проблемы с портами

**Симптомы:**
```
Error: listen EADDRINUSE: address already in use :::8000
```

**Решения:**

1. Найдите процесс, использующий порт:
   ```bash
   # Windows
   netstat -ano | findstr :8000
   
   # Linux/Mac
   lsof -i :8000
   ```

2. Остановите процесс или измените порт в настройках

3. Для backend измените порт в `backend/run.py`:
   ```python
   uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
   ```

### Проблемы с базой данных

**Симптомы:**
```
sqlalchemy.exc.OperationalError: unable to open database file
```

**Решения:**

1. Проверьте права доступа к папке backend
2. Убедитесь, что путь к базе данных корректен
3. Для SQLite проверьте, что файл `requirements.db` может быть создан

### Проблемы с CORS

**Симптомы:**
```
Access to XMLHttpRequest has been blocked by CORS policy
```

**Решения:**

1. Убедитесь, что backend запущен на порту 8000
2. Проверьте настройки CORS в `backend/main.py`
3. Если frontend на другом порту, добавьте его в `allow_origins`

### Предупреждения npm при установке frontend

**Симптомы:**
```
npm warn deprecated ...
9 vulnerabilities (3 moderate, 6 high)
```

**Причина:**
`react-scripts@5.0.1` использует некоторые устаревшие зависимости. Это нормально для разработки.

**Решения:**

1. **Для разработки:** Можно игнорировать эти предупреждения. Приложение будет работать нормально.

2. **Если хотите исправить:**
   ```powershell
   npm audit fix
   ```
   ⚠️ Не используйте `npm audit fix --force` без необходимости - это может сломать совместимость.

**Подробнее:** см. [frontend/NPM_WARNINGS.md](../frontend/NPM_WARNINGS.md)

## Получение помощи

Если проблема не решена:

1. Проверьте логи ошибок
2. Убедитесь, что все зависимости установлены
3. Попробуйте переустановить зависимости
4. Проверьте версии Python и Node.js (должны быть совместимы)
