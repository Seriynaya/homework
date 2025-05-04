# Домашняя работа Django REST framework

## Описание:

Этот проект представляет собой работу с DRF

## Использование:

1. Клонируйте репозиторий:
```
https://github.com/Seriynaya/homework.git
```


2. Установление зависимостей:
```
pip install django
```


3. Создайте файл .env в корне проекта и добавьте туда переменные окружения, указанные в файле .env.sample.


4. Подключение к базе данных:
```
[postgres]
host = localhost
port = 5432
user = postgres
password = 5432
```


4. Запуск проекта:
```
Через Docker:
docker compose up -d
Через Python:
python main.py
```

5. Проверка работоспособности:
```
Просмотр запущенных контейнеров:
docker-compose ps
Просмотр логов контейнеров:
docker-compose logs
Остановка сервиса и удаление контейнера:
docker-compose down
Сбор образов для сервисов:
docker-compose build
Выполнение команды внутри работающего контейнера:
docker-compose exec
```


## Структура проекта:

1. users/ - приложение для работы с пользователями.
2. materials/ - приложение для работы с курсами и уроками.
