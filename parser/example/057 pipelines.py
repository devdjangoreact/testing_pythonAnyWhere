# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import logging
import pymongo
import sqlite3

class MongodbPipeline:
    collection_name = 'transcripts'

    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb+srv://frank:frank@cluster0.m0o4d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.client['My_Database']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item

class SQLitePipeline:

    def open_spider(self, spider):
        # create database file
        self.connection = sqlite3.connect('transcripts.db')
        # we need a cursor object to execute SQL queries
        self.c = self.connection.cursor()
        #  try/except will help when running this for the +2nd time (we can't create the same table twice)
        try:
            # query: create table with columns
            self.c.execute('''
                CREATE TABLE transcripts(
                    title TEXT,
                    plot TEXT,
                    transcript TEXT,
                    url TEXT
                )
            ''')
            # save changes
            self.connection.commit()
        except sqlite3.OperationalError:
            pass


    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        # query: insert data into table
        self.c.execute('''
            INSERT INTO transcripts (title,plot,transcript,url) VALUES(?,?,?,?)
        ''', (
            item.get('title'),
            item.get('plot'),
            item.get('transcript'),
            item.get('url'),
        ))
        # save changes
        self.connection.commit()
        return item