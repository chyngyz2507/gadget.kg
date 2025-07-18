#!/bin/bash

# Ожидание PostgreSQL
echo "⏳ Waiting for PostgreSQL..."
while ! pg_isready -h db -p 5432 -U ${DB_USER:-postgres} -d ${DB_NAME:-megaautokg} >/dev/null 2>&1; do
  sleep 2
done

echo "✅ PostgreSQL is ready!"

# Применение миграций
python manage.py migrate

# Сбор статики (только если DEBUG=False)
if [ "${DEBUG:-False}" = "False" ]; then
  python manage.py collectstatic --noinput
fi

# Запуск сервера
exec python manage.py runserver 0.0.0.0:8000