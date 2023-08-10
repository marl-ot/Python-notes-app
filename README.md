﻿# Приложение заметки (Python)

## Информация о проекте

Проект, содержащий функционал работы с заметками.
Программа умеет создавать заметку, сохранять её, читать список
заметок, редактировать заметку, удалять заметку.

Заметка сохраняется в формате json и при сохранении содержит 
идентификатор, заголовок, тело заметки и дату/время создания или
последнего изменения заметки.

При выводе списка заметок отображает список отфильтрованных по дате заметок.

## Пользовательский интерфейс

1. Реализация через параметры запуска программы (команда, данные);
2. Реализация как запрос команды с консоли и последующим вводом данных.

### Вариант №1

Примеры команд для работы с приложением:

    python main.py add --title "Заголовок" --content "Содержание заметки"
    python main.py list
    python main.py list --date "2023-08-11"
    python main.py read 1
    python main.py edit 1 --content "Новое содержание заметки"
    python main.py delete 1


### Вариант №2

Пример работы с приложением:

    python main.py
    Меню:
        1. Создать заметку
        2. Список заметок
        3. Прочитать заметку
        4. Редактировать заметку
        5. Удалить заметку
        6. Сохранить и выйти
    Введите ваш выбор: 2
    Введите заголовок заметки: новая заметка
    Введите содержание заметки: содержание новой заметки
    Заметка удалена

    Введите команду:
    ...
