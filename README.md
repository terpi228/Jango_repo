# Домашняя работа №23 — Интернет-магазин на Django

## Описание
Реализовано приложение `catalog` с моделями:
- `Category` — категории товаров
- `Product` — продукты
- `Contact` — контактные данные

Добавлены:
- Админка с фильтрами и поиском
- Главная страница с последними 5 товарами
- Страница контактов
- Фикстуры и кастомная команда `fill_db`
- Поля `created_at` и `updated_at`

## Как запустить


`python -m venv venv`<br>
`venv\Scripts\activate`<br>
`pip install -r requirements.txt`<br>
`python manage.py migrate`<br>
`python manage.py createsuperuser`<br>
`python manage.py runserver`<br>

Админка: http://127.0.0.1:8000/admin/

Кастомная команда
``` Bash
python manage.py fill_db
```
Заполняет базу тестовыми данными.


![Скриншот приложения](https://github.com/terpi228/Jango_repo/blob/homework1/howmework_screenshots/resultsSMD.png)
