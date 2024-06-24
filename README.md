graduate_work DRF

Бэкенд-часть веб-приложения "Самообучения".

Технологии:
- python 3.12
- PostgreSQL

Используемые библиотеки:
- Django;
- djangorestframework;
- djangorestframework-simplejwt;
- django-filter;
- setuptools;
- drf-yasg;
- pillow;
- psycopg2-binary;
- python-dotenv;
- django-cors-headers;
- coverage.


Инструкция для развертывания проекта:
1. Клонировать проект

https://github.com/AlinaMordovina/self_study.git

2. Создать виртуальное окружения

Находясь в директории проекта запустить в терминале команды:

python -m venv venv

source venv/bin/activate

3. Установить зависимости

Все зависимости указаны в файле requirements.txt

Для установки всех зависимостей из файла необходимо запустить в терминале команду:

pip install -r requirements.txt

4. Cоздать базу данных

Для создания базы данных необходимо запустить в терминале команду:

CREATE DATABASE DATABASE_NAME

5. Применить миграции 

Для создания и применения миграций необходимо запустить в терминале команды:

python3 manage.py makemigrations
python3 manage.py migrate

6. Заполнить файл .env по образцу .env.sample
7. Для создания суперпользователя необходимо применить команду "python manage.py csu"
8. Для запуска проекта использовать команду "python manage.py runserver", либо через конфигурационные настройки PyCharm.
9. Посмотреть документацию API:
- Swagger http://127.0.0.1:8000/swagger/
- Redoc http://127.0.0.1:8000/redoc/
10. Управление всеми сущностями реализовано через стандартный Django admin.







Автор проекта: Мордовина Алина