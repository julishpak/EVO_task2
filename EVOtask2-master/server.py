# -*- coding: utf-8 -*-
import os
import json

import tornado.ioloop
import tornado.web
from mongoengine import connect

from utils import form_greeting, db_fill_epithets
from models import Epithet

db = connect('mongoGreet')
PORT = 4444


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', messages=None)


class GreetHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps({'name': u'Боб', 'width': 1020}))

    def post(self):
        jsonobj = json.loads(self.request.body)

        greeting = form_greeting(jsonobj['name'])
        self.write(json.dumps({'newkey': greeting}))


class Application(tornado.web.Application):
    def __init__(self):

        base_dir = os.path.dirname(__file__)
        settings = {
            'template_path': os.path.join(base_dir, "templates"),
            'static_path': os.path.join(base_dir, "static"),
            'debug': True,
            "xsrf_cookies": False,
        }
        handlers = [
            (r"/?", MainHandler),
            (r"/greet/", GreetHandler)
        ]
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    if len(Epithet.objects().all()) == 0:
        db_fill_epithets()
    application = Application()
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()