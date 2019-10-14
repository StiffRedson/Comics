# Публикуем коммиксы во Вконтакте
___

Скрипт публикует случайный комикс с сайта [xkcd.com](https://xkcd.com) в группу во Вконтакте

## Как установить?
---
* Установите Python3
* Сделайте клон проекта к себе на компьютер
* Настройте окружение в папке проекта

  ```
  you@name:~/project/path$ pip install -r requirements.txt
  ```
* Создайте группу в вк
* Создайте _standalone_ приложения здесь [vk.com/dev](https://vk.com/dev)
* Получите ключ авторизфции здесь [vk.com/dev/](https://vk.com/dev/implicit_flow_user).
Создайте фаил .env и укажите в нем значение ключа следующим образом.
>VK_ACCESS_TOKEN=*Ваш ключ авторизации*

## Как использовать?
Вызвать консоль и перейти в расположении проекта, вызвать на исполнение _comics.py_ c аргументом _-n_ и указанием номера Вашей группы

```
you@name:~/project/path$ python3 comics.py -n XXXXXXXXX
```

## Цели проекта
---
Код создан в образовательных целях на сайте для веб-разработчиков [dvmn.org](https://dvmn.org/modules/)

## Автор
---
| Contacts | Ivan Fedorov          |
|----------|-----------------------|
| Email    | StiffRedson@gmail.com |
| Telegram | @StivaRedson          |