# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import sqlite3
from scrapy.exporters import CsvItemExporter
from itemadapter import ItemAdapter


class VikkaPipeline(object):

    def open_spider(self, spider):
        self.con = sqlite3.connect('main.db')
        self.cur = self.con.cursor()
        self.cur.execute("""DROP TABLE IF EXISTS temp""")
        self.cur.execute("""CREATE TABLE temp(
        id integer primary key autoincrement,
        article_title text, 
        article_body text, 
        tags text, 
        url text)""")

    def close_spider(self, spider):
        self.con.commit()
        self.con.close()

    def process_item(self, item, spider):
        table_name = f'news_{item.pop("year")}'
        inserted_data = [item[k] for k in item]
        drop_table_if_exists = """DROP TABLE IF EXISTS {table}"""
        rename_table = """ALTER TABLE temp RENAME {table}"""
        insert_into_table = """INSERT INTO {table}(
        article_title, 
        article_body, 
        tags, 
        url) VALUES(?,?,?,?)"""

        if self.cur.execute('SELECT id FROM temp').fetchone():
            self.cur.execute(drop_table_if_exists.format(table=table_name))
            self.cur.execute(rename_table.format(table=table_name))
        self.cur.execute(insert_into_table.format(table=table_name), tuple(inserted_data))
        return item

