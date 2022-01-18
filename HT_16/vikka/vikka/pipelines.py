# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import sqlite3
from scrapy.exporters import CsvItemExporter
from itemadapter import ItemAdapter


class VikkaPipeline(object):

    def process_item(self, item, spider):
        table_name = f'news_{item.pop("table_date")}'
        inserted_data = [item[k] for k in item]
        drop_table_if_exists = """DROP TABLE IF EXISTS {table}"""
        rename_table = """ALTER TABLE temp RENAME TO {table}"""
        insert_into_table = """INSERT INTO {table}(
        article_title, 
        article_body, 
        tags, 
        url) VALUES(?,?,?,?)"""

        if self.cur.execute('SELECT table_name FROM tables WHERE table_name="temp"').fetchone():
            self.cur.execute(drop_table_if_exists.format(table=table_name))
            self.cur.execute(rename_table.format(table=table_name))
            self.cur.execute('DELETE FROM tables WHERE table_name="temp"')
            if not self.cur.execute('SELECT table_name FROM tables WHERE table_name=?', (table_name,)).fetchone():
                self.cur.execute('INSERT INTO tables(table_name) VALUES(?)', (table_name,))
        self.cur.execute(insert_into_table.format(table=table_name), tuple(inserted_data))

        return item

    """
    1. открываем бд
    2. создаём таблицу с именами существующих таблиц(если не существует)
    3. если таблица была, удаляем оттуда все упоминания таблицы temp
    4. создаём таблицу temp со всеми полями
    5. в таблицу с таблицами вставляем упоминание таблицы temp, тк она была создана
    В process_item:
    1. Если в таблице с таблицами есть упоминание таблицы temp, то:
        1.1. удаляем таблицу с юзер инпут датой, если таковая была.
        1.2. ренеймим таблицу temp в таблицу с юзер инпут датой
        1.3. если упоминания таблицы с юзер инпут датой нету в таблице с таблицами:
            1.3.1. вставляем название таблицы с юзер инпут датой в таблицу с таблицами.
            1.3.2. удаляем упоминание temp из таблицы с таблицами
    2. закидываем данные в таблицу с юзер инпут датой
    """
    def open_spider(self, spider):
        self.con = sqlite3.connect('main.db')
        self.cur = self.con.cursor()
        self.cur.execute("""DROP TABLE IF EXISTS temp""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS tables(table_name text)""")
        self.cur.execute('DELETE FROM tables WHERE table_name="temp"')
        self.cur.execute("""CREATE TABLE temp(
        id integer primary key autoincrement,
        article_title text, 
        article_body text, 
        tags text, 
        url text)""")
        self.cur.execute('INSERT INTO tables(table_name) VALUES("temp")')

    def close_spider(self, spider):
        self.con.commit()
        self.con.close()