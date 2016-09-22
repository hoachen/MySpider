# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import thread
import time

from spider import BuDeJie

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        #初始化headers
headers = { 'User-Agent' : user_agent }

if __name__ == '__main__':
    b = BuDeJie(headers)        
    models = b.parse_images()
    for m in models:
        print m.text
        print m.image_url
        print m.user.icon
        print m.user.name
        print m.time


