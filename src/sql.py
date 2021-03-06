#!/usr/bin/python
# coding= utf-8

import MySQLdb


class DataBase(object):
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='root',db='xiaomigang', charset='utf8')

    def close(self):
        self.conn.close()

    def save_stories(self, datas):
        self.connect()
        cur = self.conn.cursor()
        sql = """CREATE TABLE IF NOT EXISTS 
        story(id INT PRIMARY KEY AUTO_INCREMENT, user_icon VARCHAR(200), user_name VARCHAR(100), type INT(5), content_des TEXT, 
        image_url VARCHAR(200),time VARCHAR(50), content_from VARCHAR(50))"""
        cur.execute(sql)
        save_sql = "insert into story(user_icon, user_name, type, content_des, image_url, time, content_from) " \
                   "values(%s, %s, %s, %s, %s, %s, %s)"
        cur.executemany(save_sql, datas)
        cur.close()
        self.conn.commit()
        self.close()


