# Многоэтапная сборка для оптимизации размера образа

# Этап 1: Сборка приложения
FROM node:18-slim AS builder

WORKDIR /app

# Создаем .npmrc файл для обхода проблем с SSL сертификатами
RUN echo "strict-ssl=false" > /root/.npmrc && \
    echo "registry=https://registry.npmjs.org/" >> /root/.npmrc && \
    cat /root/.npmrc

# Копируем package.json и package-lock.json
COPY package.json package-lock.json* ./

# Устанавливаем все зависимости
RUN npm install --legacy-peer-deps

# Копируем исходный код
COPY . .

# Собираем приложение
ENV NODE_ENV=production
ENV GENERATE_SOURCEMAP=false
ENV CI=false

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
