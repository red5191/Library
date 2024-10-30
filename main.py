library = {
    'Dune' : {'author' : 'Franklin Patrick Herbert', 'year' : 1965, 'availability' : True},
    'Kolobok' : {'author' : 'Tolstoy Alexey Nikolaevich', 'year' : 1941, 'availability' : False},
    'Wiedzmin' : {'author' : 'Andrzej Sapkowski', 'year' : 1986, 'availability' : None}
}

def book_list_view(library):
    if not library:
        book_list = 'Библиотека пуста'
    else:
        book_list = list(library.keys())
    return book_list


# dz2
print(book_list_view(library))


#dz3
correct = ['да', 'нет']
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


add_book()

# dz4
def remove_book():
    title = input('Укажите название удаляемой книги ')
    if title in library:
        library.pop(title)
        print(f'Книга {title} успешно удалена')
    else:
        print('Такой книги в библиотеке не числится')

remove_book()

# dz5
def issue_book():
    title = input('Какую книгу выдать? ')
    if title in library:
        book = library[title]
        book['availability'] = False
        print(f'Книга {title} выдана')
    else:
        print('Такой книги в библиотеке не числится')

def return_book():
    title = input('Какую книгу возвращают? ')
    if title in library:
        book = library[title]
        book['availability'] = True
        print(f'Книга {title} возвращена')
    else:
        print('Такой книги в библиотеке не числится')


issue_book()
return_book()

# dz6+7
def find_book():
    title = input('Какую книгу ищем? ')
    if title in library:
        book = library[title]
        print(f'Книга {title}, автор {book['author']}, год издания {book['year']} числится в библиотеке.')
        if book['availability']:
            print('Книга доступна')
        if not book['availability']:
            print('Книга выдана')
        if book['availability'] is None:
            print('Книга в библиотеке, но ее статус не определен')
    else:
        print('Такой книги в библиотеке не числится')

find_book()