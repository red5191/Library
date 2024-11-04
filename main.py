library = {
    'Dune': {
        'author': 'Franklin Patrick Herbert', 
        'year': 1965, 
        'availability': True},
    'Kolobok': {
        'author': 'Tolstoy Alexey Nikolaevich', 
        'year': 1941, 
        'availability': False},
    'Wiedzmin': {
        'author': 'Andrzej Sapkowski', 
        'year': 1986, 
        'availability': None}
}

correct = ['да', 'нет']


def book_list_view(library):
    if not library:
        book_list = 'Библиотека пуста'
    else:
        book_list = list(library.keys())
    print(f'В библиотеке числятся следующие наименования: {(', '.join(book_list))}')
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


def remove_book(title):
    if title in library:
        library.pop(title)
        print(f'Книга {title} успешно удалена')
    else:
        print('Такой книги в библиотеке не числится')


def issue_book(title):
    if title in library:
        if library[title]['availability'] is False:
            print(f'Книга {title} уже выдана!')
        else:
            library[title]['availability'] = False
            print(f'Книга {title} выдана')
    else:
        print('Такой книги в библиотеке не числится')


def return_book(title):
    if title in library:
        if library[title]['availability'] is True:
            print(f'Книга {title} уже возвращена!')
        else:
            library[title]['availability'] = True
            print(f'Книга {title} возвращена')
    else:
        print('Такой книги в библиотеке не числится')


def find_book(title):
    if title in library:
        book = library[title]
        print(f'Книга {title} за авторством {book['author']}, {book['year']}-го года выпуска числится в библиотеке')
        if book['availability'] is True:
            print('Книга доступна')
        if book['availability'] is False:
            print('Книга выдана')
        if book['availability'] is None:
            print('Книга в библиотеке, но ее статус не определен')
    else:
        print('Такой книги в библиотеке не числится')


book_list_view(library)
add_book('Dune', 'utvjhvb', 2023)
remove_book('Kolobok')

issue_book('Wiedzmin')
return_book('Wiedzmin')

find_book('Wiedźmin')
