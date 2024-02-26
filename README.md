# Product market
### Описание
**Product market** — это REST API с базовым функционалом продуктового магазина. Через админку добавляются продукты и их категории, а пользователь добавляет продукты в корзину. В корзине подсчитывается сумма чека, общее количество продуктов и перечисляется весь список, который добавил покупатель.  

### Функционал
`GET` `api/product/` — Получение всех продуктов   
`GET` `api/product/<int:id>/` — Получение продукта по id  

`POST` `DELETE` `api/product/<int:id>/cart/` — Добавление 1 продукта в корзину / Удаление продукта из корзины  
`POST` `PATCH` `api/product/<int:id>/cart/?amount=<int:id>` — Добавление продукта в указанном количестве / Изменение количества продукта в корзине  

`GET` `api/cart/` — Получение содержимого корзины  
`POST` `api/cart/clean/` — Очистка корзины  

`GET` `api/category/` — Получение всех категорий с подкатегориями  
`GET` `api/category/<int:id>/` — Получение категории по id  

`POST` `api/auth/users/` — Создание нового пользователя  
`POST` `api/auth/token/login/` — Получение токена  
```
{
  "username" : "str",
  "email": "str",
  "password": "str"
}
```

### Стек технологий
- Django
- Django Rest Framework
- Djoser

### Автор
**Имя:** Эмилар Локтев  
**Почта:** emilar-l@yandex.ru  
**Telegram** @itsme_emichka  

### Как запустить проект
1. **Клонировать репозиторий**  
`git clone https://github.com/itsme-emichka/product_market.git`

2. **Перейти в директорию проекта**  
`cd product_market`

3. **Создать файл** `.env` **со следующими переменными**
    - SECRET_KEY
    - DEBUG

4. **Создать и активировать виртуальное окружение**  
    - `python -m venv venv`
    - Windows - `source venv/Scripts/activate`  
       Linux/MacOS - `source venv/bin/activate`

5. **Поставить зависимости**  
`pip install -r requirements.txt`

6. **Перейти в директорию с файлом** `manage.py`  
`cd product_market`

7. **Применить миграции**  
`python manage.py migrate`

8. **Запустить сервер**  
`python manage.py runserver`
