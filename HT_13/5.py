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


class BookNotExist(Exception):
    pass


class Book(object):

    def __init__(self, *args):
        self.book_name = args[0]
        self.author = args[1]
        self.pages = args[2]
        self.janra = args[3]
        self.edition = args[4]

    def __str__(self):
        return f'{[self.book_name, self.author, self.pages, self.janra, self.edition]}'


def copies_detect(name):
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    copy = cur.execute('select copies FROM books WHERE book_name=?', (name,)).fetchone()
    con.close()
    if copy:
        return int(copy[0])
    else:
        return copy

class Library(object):
    if os.path.isfile('main.db'):
        os.remove('main.db')
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    cur.execute(
        'CREATE TABLE books(id integer primary key autoincrement, book_name text, author text, pages integer, janra text, edition text, copies integer)')
    con.commit()
    con.close()

    def add_book(self, book):
        app_items = [book.book_name, book.author, book.pages, book.janra, book.edition]
        con = sqlite3.connect('main.db')
        cur = con.cursor()
        book_copy = copies_detect(book.book_name)
        if book_copy:
            cur.execute('UPDATE books SET copies=? WHERE book_name=?', (book_copy + 1, book.book_name))
        else:
            app_items.append(1)
            cur.execute('INSERT INTO books(book_name, author, pages, janra, edition, copies) VALUES(?,?,?,?,?,?)', tuple(app_items))
        con.commit()
        con.close()

    def pop_book(self, name):
        try:
            con = sqlite3.connect('main.db')
            cur = con.cursor()
            find_book = cur.execute('SELECT book_name FROM books WHERE book_name=?', (name,)).fetchone()
            copies = copies_detect(name)
            if not find_book:
                raise ValueError()
            elif not copies or copies == 1:
                cur.execute('DELETE FROM books WHERE book_name=?', (name,))
            else:
                cur.execute('UPDATE books SET copies=? WHERE book_name=?', (copies - 1, name))
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
                result = cur.execute('SELECT book_name, author, pages, janra, edition, copies FROM books WHERE author=?',
                                     (author,)).fetchone()
            else:
                result = cur.execute('SELECT book_name, author, pages, janra, edition, copies FROM books WHERE book_name=?',
                                     (name,)).fetchone()
            if not result:
                raise BookNotExist()
            else:
                return result
        except ValueError:
            return ('Please enter book name or book author!')
        except BookNotExist:
            return ('There are no such books in the library!')


book_1 = Book('Eye of ctulhu', 'Hovard Lovecraft', 314, 'Horror', 'asdasd')

lib = Library()

lib.add_book(book_1)
print(lib.find_book(name='Eye of ctulhu'))
lib.add_book(book_1)
print(lib.find_book(name='Eye of ctulhu'))
lib.add_book(book_1)
print(lib.find_book(name='Eye of ctulhu'))
lib.pop_book('Eye of ctulhu')
print(lib.find_book(name='Eye of ctulhu'))
lib.pop_book('Eye of ctulhu')
print(lib.find_book(name='Eye of ctulhu'))
lib.pop_book('Eye of ctulhu')
print(lib.find_book(name='Eye of ctulhu'))
lib.pop_book('Eye of ctulhu')
print(lib.find_book(name='Eye of ctulhu'))
