### Тестовое задание "API заказы на автомобили"
___

#### Назначение

Выполнение тестового задания создания API 
для оплаты товаров сервиса Stripe
___

#### Запуск
Перед запуском в докере создать файл `.env` в директории 'config' и указать следующие параметры:
SECRET_KEY={секретный ключ проекта Django}
NAME_DB={имя Postgre базы}
USER_DB={имя пользователя для подключения к базе}
PASS_DB={пароль пользователя}
HOST_DB={Ip или контейнер}
PORT_DB=5432
(также это возможно было описать внутри docker-compose)
`docker-compose.yml` внтури директории `car`
