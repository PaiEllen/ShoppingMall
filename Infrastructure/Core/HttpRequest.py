#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import tornado.ioloop
import tornado.web
from ..Session.SessionFacotry import SessionFactory


class BaseRequestHandler(tornado.web.RequestHandler):

    def initialize(self):
        self.session = SessionFactory.get_session()
        self.session.initialize(self,120)