# -*- coding:utf-8 -*-

from spider import BuDeJie
from sql import DataBase

if __name__ == '__main__':
    b = BuDeJie()        
    text_stories = b.parse_texts()
    db = DataBase()
    datas = []
    for m in text_stories:
        datas.append((m.user.icon, m.user.name, 
            m.content_type, m.text, None, m.time, m.content_from))
    db.save_stories(tuple(datas))
    image_stories = b.parse_images()
    datas = []
    for m in image_stories:
        datas.append((m.user.icon, m.user.name, 
            m.content_type, m.text, m.image_url, m.time, m.content_from))
    db.save_stories(tuple(datas))