library = {
    'Dune': {'author': 'Franklin Patrick Herbert', 'year': 1965, 'availability': True},
    'Kolobok': {'author': 'Tolstoy Alexey Nikolaevich', 'year': 1941, 'availability': False},
    'Wiedzmin': {'author': 'Andrzej Sapkowski', 'year': 1986, 'availability': None}
}

correct = ['да', 'нет']


def book_list_view(library):
    if not library:
        book_list = 'Библиотека пуста'
    else:
        book_list = list(library.keys())
    print(f'В библиотеке числятся следующие наименования: {book_list}')
    return book_list


def add_book(title, author, year):
    print('Добавляем книгу')
    if title in library:
        refresh = input('Обновить информацию? ').lower()
        while refresh not in correct:
            print('Пожалуйста используйте для ответа \"да\" или \"нет\"')
            refresh = input('Обновить информацию? ').lower()
        if refresh == 'да':
            library[title] = {'author': author, 'year': year, 'availability': None}
            print(f'Данные по книге {title} успешно обновлены')
    else:
        library[title] = {'author': author, 'year': year, 'availability': None}
        print(f'Данные по книге {title} успешно добавлены')


add_book('Dune')
