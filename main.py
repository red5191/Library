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
    return book_list


def add_book():
    print('Добавляем книгу')
    title = input('Укажите название ')
    author = input('Укажите автора ')
    year = input('Укажите год ')
    if title in library:
        refresh = input('Обновить информацию? ').lower()
        while refresh not in correct:
            print('Пожалуйста используйте для ответа \"да\" или \"нет\"')
            refresh = input('Обновить информацию? ').lower()
        if refresh == 'да':
            library[title] = {'author' : author, 'year' : year, 'availability' : None}
            print(f'Данные по книге {title} успешно обновлены')
    else:
        library[title] = {'author' : author, 'year' : year, 'availability' : None}
        print(f'Данные по книге {title} успешно добавлены')


print(f'В библиотеке числятся следующие наименования: {book_list_view(library)}')

add_book()