# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import csv
import pathlib
import os
from scrapy.exporters import CsvItemExporter
from itemadapter import ItemAdapter


class VikkaPipeline(object):

    def open_spider(self, spider):
        self.custom_file = open(f'temp.csv', 'wb')


    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.custom_file.close()


    def process_item(self, item, spider):
        rename_file = item.pop('year')
        if os.path.exists(os.path.join(os.getcwd(), 'temp.csv')):
            if os.path.exists(os.path.join(os.getcwd(), f'{rename_file}.csv')):
                os.remove(os.path.join(os.getcwd(), f'{rename_file}.csv'))
            self.custom_file.close()
            os.rename(os.path.join(os.getcwd(), 'temp.csv'), os.path.join(os.getcwd(), f'{rename_file}.csv'))
            self.custom_file = open(f'{rename_file}.csv', 'wb')
            self.exporter = CsvItemExporter(self.custom_file, 'UTF-8')
        self.exporter.fields_to_export = [i for i in item.keys() if i != 'year']
        self.exporter.export_item(item)
        return item

    def file_path(self, item, response=None, info=None):
        return