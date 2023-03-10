# coursework_6

## Данная курсовая работа представляет собой backend-часть для сайта объявлений.

Проект использует следующие технологии:

- [Django](https://www.djangoproject.com/) - Django makes it easier to build better web apps more quickly and with less code.
- [Django-rest-framework](https://www.django-rest-framework.org/) - Django REST framework is a powerful and flexible toolkit for building Web APIs.
- [Django-filter](https://django-filter.readthedocs.io/en/stable/#) - Django-filter is a generic, reusable application to alleviate writing some of the more mundane bits of view code. Specifically, it allows users to filter down a queryset based on a model’s fields, displaying the form to let them do this.
- [Postgresql](https://www.postgresql.org/) - The World's Most Advanced Open Source Relational Database.
- [Djoser](https://djoser.readthedocs.io/en/latest/getting_started.html) - REST implementation of Django authentication system. djoser library provides a set of Django Rest Framework views to handle basic actions such as registration, login, logout, password reset and account activation. It works with custom user model.
- [Drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/) - Sane and flexible OpenAPI 3.0 schema generation for Django REST framework.


## Installation

Создать виртуальное окружение.

```sh
# для первичной установки
poetry install
# для обновления
poetry update
```

Запустить образ Docker из директории market_postgres
```sh
docker-compose up --build -d 
```

Выполнить миграции.
```sh
./manage.py migrate 
```

Загрузить тестовые данные в базу из csv
```sh
 ./manage.py loadall
```

Запустить сервер
```sh
./manage.py runserver 0.0.0.0:8000  
```

Бэкенд-часть проекта предполагает реализацию следующего функционала:

- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- Восстановление пароля через электронную почту (не обязательно).
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
- Под каждым объявлением пользователи могут оставлять отзывы.
- В заголовке сайта можно осуществлять поиск объявлений по названию.

**Краткое техническое задание и рекомендации по порядку выполнения:**

- **Этап I.** Настройка Django-проекта.
    
    На данном этапе нам предстоит подготовить наш Django-проект к работе.
    Данный этап состоит из трех подзадач:
    
    1. Подключение базы данных Postgres.
    2. Подключение CORS headers.
    3. Подключение Swagger.
- **Этап II.** Создание модели юзера. Настройка авторизации и аутентификации.
    - Создание модели пользователя.
        - Необходимые поля:
        - first_name — имя пользователя (строка).
        - last_name — фамилия пользователя (строка).
        - phone — телефон для связи (строка).
        - email — электронная почта пользователя (email) **(используется в качестве логина).**
        - role — роль пользователя, доступные значения: user, admin.
        - image - аватарка пользователя
    - Настройка авторизации и аутентификации.
        
        На данном этапе мы будем настраивать авторизацию пользователя с помощью библиотеки simple_jwt. Подробнее об этом можно узнать в рекомендациях
        
    - Сброс и восстановление пароля через почту* (необязательно).
        
        Основная сложность при настройке сброса и восстановления пароля через почту — подключение самого почтового ящика, через который будет происходить отправка таких сообщений. Как правило, при такой настройке требуется разрешить доступ неавторизованным приложениям к используемому почтовому ящику — эти настройки обычно находятся в разделе «Безопасность» на сайтах почтовых сервисов.
        В целом логика сброса пароля с использованием Djoser достаточно проста.
        
        1. Юзер отправляет POST-запрос на адрес 
        
        `/users/reset_password/` с содержанием: 
            
            ```json
            {
                "email": "example@mail.com"
            } 
            ```
            
        2. Сервер высылает на почту ссылку вида:
            
            ```html
            "/<url>/{uid}/{token}" # предварительно это настраивается в settings
            ```
            
        3. Далее идет работа фронта — из данной ссылки парсится uid и токен, который впоследствии передается в JSON вместе с новым паролем на адрес `users/reset_password_confirm` — по умолчанию он выглядит именно так.
        А содержание POST-запроса, отправляемого на бэкэнд, выглядит следующим образом:
            
            ```json
            {
                "uid": "uid",
                "token": "token",
                "new_password": "P4$$W0RD"
            }
            ```
            
- **Этап III.** Описание моделей объявлений и отзывов.
    
    Модель **объявления** должна содержать следующие поля:
    
    - title — название товара.
    - price — цена товара (целое число).
    - description — описание товара.
    - author — пользователь, который создал объявление.
    - created_at — время и дата создания объявления.
    
    *Все записи при выдаче должны быть отсортированы по дате создания 
    (чем новее, тем выше).*
    
    Модель **отзыва** должна содержать следующие поля:
    
    - text — текст отзыва.
    - author — пользователь, который оставил отзыв.
    - ad — объявление, под которым оставлен отзыв.
    - created_at - время и дата создания отзыва
- **Этап IV.** Создание views и эндпоинтов.
    
    Для получения документации по требуемым эндпоинтам выполните команду `python3 manage.py runserver` в склонированном репозитории,
    откройте браузер и перейдите по адресу:
    `[http://localhost:8000/api/redoc-tasks/](http://127.0.0.1:8000/api/redoc-tasks/)`
    
    Задание со звездочкой* (не обязательно)
    
    Также наша работа предусматривает реализацию поиска товаров на главной странице по названию. Для выполнения данного задания рекомендуем использовать библиотеку `django-filter`. С документацией можно ознакомиться здесь: [https://django-filter.readthedocs.io/en/stable/guide/install.html](https://django-filter.readthedocs.io/en/stable/guide/install.html). В рекомендациях есть краткая инструкция по использованию фильтров.
    
    Также обратите внимание на эндпоинты, которые требуют реализации пагинации. Эндпоинт /ads/ требует не более 4 объектов на странице (ограничение фронта)
    
- **Этап V**. Определение permissions к views.
    
    **Анонимный пользователь может**:
    
    получать список объявлений.
    
    **Пользователь может:**
    
    - получать список объявлений,
    - получать одно объявление,
    - создавать объявление
    - редактировать и удалять свое объявление,
    - получать список комментариев,
    - создавать комментарии,
    - редактировать/удалять свои комментарии.
    
    **Администратор может:**
    
    дополнительно к правам пользователя редактировать или удалять
    объявления и комментарии любых других пользователей.