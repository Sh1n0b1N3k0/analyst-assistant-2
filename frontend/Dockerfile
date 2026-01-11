# Многоэтапная сборка для оптимизации размера образа

# Этап 1: Сборка приложения
FROM node:18-slim AS builder

WORKDIR /app

# Копируем package.json и .npmrc (если есть)
COPY package.json ./
COPY .npmrc* ./

# Настраиваем npm для обхода проблем с SSL сертификатами (если .npmrc не скопирован)
RUN npm config set strict-ssl false || true
RUN npm config set registry https://registry.npmjs.org/ || true

# Устанавливаем зависимости без package-lock.json для избежания конфликтов
# Сначала устанавливаем react-scripts явно
RUN npm install react-scripts@5.0.1 --legacy-peer-deps --save

# Затем устанавливаем остальные зависимости
RUN npm install --legacy-peer-deps

# Копируем исходный код
COPY . .

# Собираем приложение
ENV NODE_ENV=production
ENV GENERATE_SOURCEMAP=false
ENV CI=false

# Проверяем установку перед сборкой
RUN npm list react-scripts

# Собираем приложение
RUN npm run build

# Этап 2: Production образ
FROM nginx:alpine

# Копируем собранное приложение
COPY --from=builder /app/build /usr/share/nginx/html

# Копируем конфигурацию nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Открываем порт
EXPOSE 80

# Запускаем nginx
CMD ["nginx", "-g", "daemon off;"]
