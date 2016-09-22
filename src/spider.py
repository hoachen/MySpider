# -*- coding:utf-8 -*-
import urllib2
import re
import models
from models import User
from models import TextModel
from models import ImageModel

BDJ = "budejie"
QIUSHI = "qiushibaike"

CONTENT_WEBSITE = {
    BDJ: "http://www.budejie.com",
}


class Spider(object):
    def __init__(self, headers):
        self.headers = headers

    def request_content(self, url):
        try:
            print 'url:', url
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            return content
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接错误",e.reason
                return None    	

    def parse_texts(self):
        pass

    def parse_images(self):
        pass
    

class BuDeJie(Spider):
    def __init__(self, headers):
        Spider.__init__(self, headers)
        self.name = BDJ
        self.base_url = CONTENT_WEBSITE[self.name]
    
    def parse_texts(self):
        url = "%s/text/" % self.base_url
        content = self.request_content(url)
        # print content
        if content:
            pattern = re.compile('<img.*?u-logo lazy".*?data-original="(.*?)".*?></a>.*?'+ # user icon url
                '<a.*?u-user-name.*?target="_blank">(.*?)</a>.*?'+   # user name 
                '<span.*?f-ib f-fr">(.*?)</span>.*?'+  # release time
                '<div.*?j-r-list-c-desc">(.*?)</div>',re.S) # text
            items = re.findall(pattern, content)
            models = []
            for item in items:
                # name, icon
                user = User(item[0], item[1])
                # user, time, text, content_from
                model = TextModel(user, item[2], item[3], self.name)
                models.append(model)
            return models
        else:
            print 'request content error'
            return None    

    def parse_images(self):
        url = '%s/pic/' % self.base_url
        content = self.request_content(url)
        # print content
        if content:
            pattern = re.compile('<img.*?u-logo lazy".*?data-original="(.*?)".*?></a>.*?'+ # user icon url
                '<a.*?u-user-name.*?target="_blank">(.*?)</a>.*?'+   # user name 
                '<span.*?f-ib f-fr">(.*?)</span>.*?'+  # release time
                '<div.*?j-r-list-c-desc">(.*?)</div>.*?'+ # text
                '<img.*?class="lazy".*?data-original="(.*?)".*?>', re.S) #image url
            items = re.findall(pattern, content)
            models = []
            for item in items:
                user = User(item[0], item[1])
                # (self, user, time, image_url, text, content_from):
                model = ImageModel(user, item[2], item[3], item[4], self.name)
                models.append(model)
            return models    