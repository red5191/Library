library = {
    'Dune': {'author': 'Franklin Patrick Herbert', 'year': 1965, 'availability': True},
    'Kolobok': {'author': 'Tolstoy Alexey Nikolaevich', 'year': 1941, 'availability': False},
    'Wiedzmin': {'author': 'Andrzej Sapkowski', 'year': 1986, 'availability': None}
}


def book_list_view(library):
    if not library:
        book_list = 'Библиотека пуста'
    else:
        book_list = list(library.keys())
    return book_list


print(book_list_view(library))
