# Скрипт для инициализации базы данных в Docker контейнере (PowerShell)

Write-Host "Waiting for PostgreSQL to be ready..." -ForegroundColor Yellow

# Ждем пока PostgreSQL будет готов
$maxAttempts = 30
$attempt = 0

do {
    $attempt++
    try {
        docker-compose exec -T db pg_isready -U postgres 2>&1 | Out-Null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "PostgreSQL is ready!" -ForegroundColor Green
            break
        }
    } catch {
        # Ignore errors
    }
    
    if ($attempt -lt $maxAttempts) {
        Write-Host "PostgreSQL is unavailable - sleeping ($attempt/$maxAttempts)" -ForegroundColor Yellow
        Start-Sleep -Seconds 2
    } else {
        Write-Host "PostgreSQL failed to start after $maxAttempts attempts" -ForegroundColor Red
        exit 1
    }
} while ($attempt -lt $maxAttempts)

# Проверяем, существует ли база данных
Write-Host "Checking if database exists..." -ForegroundColor Yellow
$dbExists = docker-compose exec -T db psql -U postgres -tAc "SELECT 1 FROM pg_database WHERE datname='requirements_db'" 2>&1

if ($dbExists -notmatch "1") {
    Write-Host "Creating database..." -ForegroundColor Yellow
    docker-compose exec -T db psql -U postgres -c "CREATE DATABASE requirements_db;"
}

# Применяем скрипт инициализации
Write-Host "Applying initialization script..." -ForegroundColor Yellow
docker-compose exec -T db psql -U postgres -d requirements_db -f /docker-entrypoint-initdb.d/init_database.sql

if ($LASTEXITCODE -eq 0) {
    Write-Host "Database initialized successfully!" -ForegroundColor Green
} else {
    Write-Host "Failed to initialize database" -ForegroundColor Red
    exit 1
}
