'''5. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної
бібліотеки(включіть фантазію).'''
'''
Название книги
Автор
Количество страниц
Жанр
Издание

create table books(id integer primary key autoincrement, book_name text, author text, pages integer, janra text, edition text
'''
import sqlite3


class Book(object):

    def __init__(self, *args):
        self.book_name = args[0]
        self.author = args[1]
        self.pages = args[2]
        self.janra = args[3]
        self.edition = args[4]
        

    def show_book(self):
        print(self.book_name, self.author, self.pages, self.janra, self.edition)
        
class Dictionary(Book):

    def __init__(self, lang_to, lang_in, *args):
        self.lang_to = lang_to
        self.lang_in = lang_in
        super(Dictionary, self).__init__(*args)

class 
book_1 = Book('Eye of ctulhu', 'Hovard Lovecraft', 314, 'Horror', 'asdasd')

book_1.show_book()

book_2 = Dictionary('English', 'German', 'English-German general dictionary', 'Someone', 890, 'Dictionary', 'asdasd')
book_2.show_book()
