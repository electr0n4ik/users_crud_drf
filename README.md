
<h1 align="center">Users CRUD Application with Django Rest Framework</h1>

## Описание

Это простое серверное приложение для управления пользователями (CRUD) с использованием Django Rest Framework и базой данных PostgreSQL. Приложение поддерживает регистрацию и аутентификацию пользователей с помощью JWT (JSON Web Tokens).

Для деплоя зависимостей и самого сервиса использовал Docker и Docker Compose.

## Установка и запуск

### Шаги установки

1. Клонируйте репозиторий:

```shell
git clone https://github.com/yourusername/users-crud-drf.git
cd users-crud-drf
```

2. Запуск через docker-compose:
   
- открываем новый терминал
- останавливаем postgres, если он запущен
 
```shell
sudo systemctl status postgresql
sudo systemctl stop postgresql
```

- создаем переменные окружения в .env файле, в корне проекта

```shell
SECRET_KEY = 'your_secret_key'
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_HOST = 'db'
DB_PORT = '5432'
```

- запускаем команду для сборки
 
```shell
docker-compose -f docker-compose.yml --env-file .env up --build
```

- видим запущенный сервер по адресу http://0.0.0.0:8888/


## Использование API

Получение списка пользователей, тело ответа

```shell
{
    "username": "newuser",
    "password": "newpassword",
    "email": "newuser@example.com",
    "first_name": "New",
    "last_name": "User"
}
```

Обновление информации о пользователе методом PATCH позволяет частично обновлять информацию о пользователе, а PUT позволяет полностью обновлять информацию о пользователе с указанием всех полей.

```shell
{
    "username": "updateduser",
    "email": "updateduser@example.com",
    "first_name": "Updated",
    "last_name": "User"
}
```

## Безопасность

### Защита от SQL-инъекций

Django ORM (Object-Relational Mapping) обеспечивает автоматическую защиту от SQL-инъекций, поскольку все запросы к базе данных создаются с использованием параметризованных запросов. Это гарантирует, что данные, введенные пользователями, не могут изменить структуру SQL-запросов.

### JWT аутентификация

Использование JWT для аутентификации обеспечивает безопасный и стандартизированный способ аутентификации пользователей. Токены имеют ограниченное время жизни, что уменьшает риск компрометации.

### Дополнительные меры безопасности

- Использование переменных окружения для хранения чувствительных данных, таких как секретный ключ и учетные данные базы данных.

- Ограничение доступа к API только для аутентифицированных пользователей с использованием настроек Django Rest Framework.

- Регулярные обновления зависимостей для обеспечения защиты от известных уязвимостей.

Если у вас есть какие-либо вопросы или предложения, пожалуйста, свяжитесь со мной по адресу andreyshka3@gmail.com.

## CURLs

**api/register/**

**POST**

```shell
curl --location 'http://localhost:8000/api/register/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "username",
    "password": "password",
    "email": "newuser@example.com",
    "first_name": "New",
    "last_name": "User"
}'
```

**api/token/**

**GET**

```shell
curl --location 'http://localhost:8000/api/token/' \
--header 'Content-Type: application/json' \
--data '{
    "username": "username",
    "password": "password"
}'
```

**api/users/**

**GET**

```shell
curl --location 'http://localhost:8000/api/users/' \
--header 'Authorization: Bearer <token>'
```

**api/users/<int:id>/**

**GET**

```shell
curl --location 'http://localhost:8888/api/users/1/' \
--header 'Authorization: Bearer <token>'
```

**PATCH**

```shell
curl --location --request PATCH 'http://localhost:8888/api/users/1/' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "patch_username"
}'
```

**PUT**

```shell
curl --location --request PUT 'http://localhost:8888/api/users/1/' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "put_username",
    "password": "put_password",
    "email": "put@example.com",
    "first_name": "New_put",
    "last_name": "User_put"
}'
```

**DELETE**

```shell
curl --location --request DELETE 'http://localhost:8888/api/users/1/' \
--header 'Authorization: Bearer <token>'
```
