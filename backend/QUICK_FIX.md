# Быстрое решение проблем с установкой

## Проблема: SSL Certificate Verify Failed

Если вы получили ошибку `CERTIFICATE_VERIFY_FAILED`:

### Windows:

**PowerShell (обязательно используйте `.\`):**
```powershell
cd backend
.\install_ssl_fix.bat
```

**Command Prompt (cmd):**
```cmd
cd backend
install_ssl_fix.bat
```

**Или просто дважды кликните** на `install_ssl_fix.bat` в проводнике Windows.

> ⚠️ **Важно:** В PowerShell всегда используйте `.\` перед именем `.bat` файла!

### Linux/Mac:
```bash
cd backend
chmod +x install_ssl_fix.sh
./install_ssl_fix.sh
```

## Проблема: Ошибка компиляции pydantic-core

Если установка падает с ошибкой компиляции Rust, используйте упрощенный файл требований:

```bash
cd backend
venv\Scripts\activate
pip install -r requirements_simple.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --no-cache-dir
```

## Проверка установки

После установки проверьте:

**Windows:**
```powershell
venv\Scripts\activate
pip list
```

**Linux/Mac:**
```bash
source venv/bin/activate
pip list
```

Должны быть установлены:
- fastapi
- uvicorn
- sqlalchemy
- pydantic
- pydantic-core (предкомпилированный)

## Запуск

**Windows:**
```powershell
venv\Scripts\activate
python run.py
```

**Linux/Mac:**
```bash
source venv/bin/activate
python run.py
```

API будет доступен на http://localhost:8000
