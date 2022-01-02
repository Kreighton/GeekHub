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

con = sqlite3.connect('db.sql')
cur = con.cursor()
cur.execute('create table books(id integer primary key autoincrement, book_name text, author text, pages integer, janra text, edition text')
con.commit()
con.close()


class SchoolLibrary(object):

    def __init__(self, *args):
        self.book_name = args[0]
        self.author = args[1]
        self.pages = args[2]
        self.janra = args[3]
        self.edition = args[4]

    def add_book(self):
        con = sqlite3.connect('db.sql')
        cur = con.cursor()
        cur.execute('INSERT INTO books (book_name, author, pages, janra, edition) VALUES (?,?,?,?,?)',
                    (self.book_name, self.author, self.pages, self.janra, self.edition))
        con.commit()
        con.close()
        print(f'Added book {self.book_name}')
        return
    
book_1 = SchoolLibrary('Eye of ctulhu', 'Hovard Lovecraft', 314, 'Horror', 'asdasd')
book_1.add_book()
