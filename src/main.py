# -*- coding:utf-8 -*-

from spider import BuDeJie
from spider import NeiHan
from sql import DataBase

def crawl_texts(s):
    text_stories = s.parse_texts()  
    db = DataBase()
    datas = []
    for m in text_stories:
        data = (m.user.icon, m.user.name, 
                m.content_type, m.text, None, m.time, m.content_from)        
        datas.append(data)
    db.save_stories(tuple(datas))    
          
def crawl_images(s):
    text_stories = s.parse_images()  
    db = DataBase()
    datas = []
    for m in text_stories:
        data = (m.user.icon, m.user.name, 
                m.content_type, m.text, m.image_url, m.time, m.content_from)        
        datas.append(data)
    db.save_stories(tuple(datas))    


if __name__ == '__main__':
    spiders = [BuDeJie(), NeiHan()]
    for s in spiders:
        crawl_texts(s)
        crawl_images(s)

    