# Установка на Windows

## Быстрая установка

### Вариант 1: Двойной клик (самый простой)

1. Откройте папку `backend` в проводнике Windows
2. Дважды кликните на файл `install_ssl_fix.bat`
3. Дождитесь завершения установки

### Вариант 2: Через PowerShell

```powershell
cd backend
.\install_ssl_fix.bat
```

> ⚠️ **Важно в PowerShell:** Всегда используйте `.\` перед именем `.bat` файла. Это требование безопасности PowerShell.

### Вариант 3: Через Command Prompt (cmd)

```cmd
cd backend
install_ssl_fix.bat
```

> ℹ️ **В Command Prompt** можно использовать имя файла без `.\`

## Важные замечания для Windows

- ✅ **Используйте `.bat` файлы** - они уже исполняемые
- ❌ **НЕ используйте `chmod`** - это команда Linux/Mac, в Windows она не работает
- ✅ **Используйте `.\` перед именем файла** в PowerShell (опционально, но рекомендуется)
- ✅ **Или просто имя файла** в Command Prompt: `install_ssl_fix.bat`

## Если возникают проблемы

1. Убедитесь, что Python установлен:
   ```powershell
   python --version
   ```

2. Если Python не найден, установите его с [python.org](https://www.python.org/downloads/)
   - ⚠️ **Важно:** При установке отметьте "Add Python to PATH"

3. Попробуйте запустить скрипт от имени администратора (правый клик → "Запуск от имени администратора")

## После установки

Запустите сервер:

```powershell
cd backend
venv\Scripts\activate
python run.py
```

API будет доступен на http://localhost:8000
