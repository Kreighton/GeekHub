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
        insert_into_table = """INSERT INTO {table}(
        article_title, 
        article_body, 
        tags, 
        url) VALUES(?,?,?,?)"""

        create_customname_table = """CREATE TABLE IF NOT EXISTS {table}(
        id integer primary key autoincrement,
        article_title text, 
        article_body text, 
        tags text, 
        url text)"""

        self.cur.execute(create_customname_table.format(table=table_name))
        self.cur.execute(insert_into_table.format(table=table_name), tuple(inserted_data))

        return item

    def open_spider(self, spider):
        self.con = sqlite3.connect('main.db')
        self.cur = self.con.cursor()

    def close_spider(self, spider):
        self.con.commit()
        self.con.close()
