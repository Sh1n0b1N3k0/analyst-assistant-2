# Решение конфликта версий TypeScript

## Проблема

При установке зависимостей возникает ошибка:
```
ERESOLVE could not resolve
Conflicting peer dependency: typescript@4.9.5
```

Это происходит потому, что `react-scripts@5.0.1` поддерживает только TypeScript версий 3.2.1 или 4.x, но в `package.json` была указана версия 5.x.

## Решение 1: Использовать TypeScript 4.9.5 (рекомендуется)

Версия TypeScript в `package.json` уже обновлена до `^4.9.5`. Просто выполните:

```powershell
npm install
```

## Решение 2: Использовать TypeScript 5 с --legacy-peer-deps

Если вам нужен TypeScript 5, измените `package.json`:

```json
"typescript": "^5.2.2"
```

И установите с флагом:

```powershell
npm install --legacy-peer-deps
```

⚠️ **Внимание:** Это может привести к несовместимостям, так как react-scripts официально не поддерживает TypeScript 5.

## Решение 3: Обновить react-scripts

Можно обновить react-scripts до более новой версии (если доступна), которая поддерживает TypeScript 5:

```powershell
npm install react-scripts@latest --legacy-peer-deps
```

## После установки

После успешной установки запустите приложение:

```powershell
npm start
```
