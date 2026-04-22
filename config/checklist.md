# Чек-лист по замечаниям куратора

Привет! Ниже — структурированный список всех пунктов, которые нужно исправить.  
Отмечай галочкой ✅, когда выполнишь каждый пункт.

---

## 📌 Задача 1: Настройка подключения к PostgreSQL

### Что не сделано:
- [x] Добавить `psycopg2-binary` в `requirements.txt` или `pyproject.toml`  
  > Нужно: `pip install psycopg2-binary` и зафиксировать зависимость
- [x] Вынести параметры подключения к БД в файл `.env`  
  Пример содержимого `.env`:
  ```env
  DB_NAME=your_db_name
  DB_USER=your_db_user
  DB_PASSWORD=your_password
  DB_HOST=localhost
  DB_PORT=5432  
```

![Скриншот приложения](howmework_screenshots\resultsSMD.png)