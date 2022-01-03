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
import os

class Book(object):

    def __init__(self, *args):
        self.book_name = args[0]
        self.author = args[1]
        self.pages = args[2]
        self.janra = args[3]
        self.edition = args[4]
        
    def __str__(self):
        return f'{[self.book_name, self.author, self.pages, self.janra, self.edition]}'

class Library(object):
    if os.path.isfile('main.db'):
        os.remove('main.db')
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE books(id integer primary key autoincrement, book_name text, author text, pages integer, janra text, edition text, copies integer)')
    con.commit()
    con.close()

    def copies_detect(self, name):
        con = sqlite3.connect('main.db')
        cur = con.cursor()
        copy = cur.execute('select copies FROM books WHERE book_name=?', name)
        con.close()
        return copy
    #тут ошибка, не находит copies_detect
    def add_book(self, book):
        app_items = (book.book_name, book.author, book.pages, book.janra, book.edition)
        con = sqlite3.connect('main.db')
        cur = con.cursor()
        book_copy = copies_detect(book.book_name)
        cur.execute('INSERT INTO books(book_name, author, pages, janra, edition) VALUES(?,?,?,?,?)', app_items)
        con.commit()
        con.close()
         
    

    def pop_book(self, name):
        try:
            con = sqlite3.connect('main.db')
            cur = con.cursor()
            find_book = cur.execute('SELECT book_name FROM books WHERE book_name=?', name)
            if not find_book:
                raise ValueError()
            cur.execute('DELETE FROM books WHERE book_name=?', name)
            con.commit()
            con.close()
        except ValueError:
            print('Wrong book name!')
            return


    def find_book(self, name='', author=''):
        try:
            con = sqlite3.connect('main.db')
            cur = con.cursor()
            if not name and not author:
                raise ValueError()
            elif not name:
                result = cur.execute('SELECT book_name, author, pages, janra, edition FROM books WHERE author=?', (author,)).fetchone()
            else:
                result = cur.execute('SELECT book_name, author, pages, janra, edition FROM books WHERE book_name=?', (name,)).fetchone()
            return result
        except ValueError:
            return ('Please enter book name or book author!')
            


book_1 = Book('Eye of ctulhu', 'Hovard Lovecraft', 314, 'Horror', 'asdasd')
print(book_1)

lib = Library()

lib.add_book(book_1)
lib.add_book(book_1)
print(lib.find_book(name='Eye of ctulhu'))
