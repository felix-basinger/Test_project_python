menu = ['Главное меню',
        'Открыть файл',
        'Сохранить файл',
        'Показать все заметки',
        'Добавить заметку',
        'Найти заметку',
        'Изменить заметку',
        'Удалить заметку',
        'Выход'
        ]

invalid_selection = f'Ошибка ввода. Введите число от 1 до {len(menu) - 1}: '

select_menu = 'Выберите пункт меню: '

load_successful = 'Loading'
error_load = 'not loading'

save_successful = 'Saving'
error_save = 'not saving'

empty_note = 'Empty Nodes'

search_word = 'Что ищем? '

index_update = 'Введите id: '


def empty_search(word):
    return f' {word} не найдено!'


def remove_contact(word):
    return f' Заметка {word} удалена'


def add_successful(title: str) -> str:
    return f'Заметка {title} успешно добавлена!'


new_note = {
    'title': 'Введите заголовок: ',
    'body': 'Введите тело заметки: '
}

goodbay = 'До встречи!!'