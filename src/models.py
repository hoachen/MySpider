# -*- coding:utf-8 -*-

TEXT, IMAGE = 1,2

class User(object):
    def __init__(self, icon, name):
        self.icon = icon
        self.name = name

    def __repr__(self):
        return "%s,%s" % (self.name, self.icon)    

class Model(object):
    def __init__(self, user, content_type, time, content_from):
        self.content_type = content_type
        self.user = user
        self.time = time
        self.content_from = content_from 


class TextModel(Model):
    def __init__(self, user, time, text, content_from):
        Model.__init__(self, user, TEXT, time, content_from)
        self.text = text

    def __repr__(self):
        return "%s, %s, %s" % (self.user.name, self.text, self.content_from)    


class ImageModel(Model):
    def __init__(self, user, time, text, image_url, content_from):
        Model.__init__(self, user, IMAGE, time, content_from)
        self.image_url = image_url;
        self.text = text

    def __repr__(self):
        return "%s, %s, %s, %s, %s" % (self.user.name, self.image_url, self.text, self.content_from)   
