# Онлайн-магазин телефонов — gadget.kg

Django-проект с корзиной, заказами, регистрацией по Gmail, активацией по email, оплатой, Celery, JWT и Docker.

##  Возможности

- Регистрация/вход по Gmail + подтверждение email (Celery + Redis)
- JWT-аутентификация
- Категории, подкатегории и товары
- Добавление товаров в корзину
- Оформление заказов
- Отзывы и рейтинги
- Фильтрация, поиск и сортировка товаров
- Платежи и фильтрация по пользователю
- Панель администратора
- Разграничение прав доступа
- Docker-окружение + PostgreSQL

##  Установка и запуск (в Docker)

```bash
# 1. Клонируем репозиторий
git clone https://github.com/ИМЯ_ПОЛЬЗОВАТЕЛЯ/gadget.kg.git
cd gadget.kg

# 2. Собираем контейнеры
docker-compose build

# 3. Запускаем проект
docker-compose up


Миграции и суперпользователь
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser


Регистрация и активация пользователя
Отправить POST на /api/user/register/ с email и password

На консоль придёт код активации

Отправить POST на /api/user/activate/ с email и code