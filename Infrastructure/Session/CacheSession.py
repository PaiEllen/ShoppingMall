#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
from .BaseSession import BaseSession


class CacheSession(BaseSession):

    session_container = {}

    def __init__(self):
        self.handler = None
        self.random_str = None

    def initialize(self, handler, expires):
        self.handler = handler
        client_random_str = handler.get_cookie(CacheSession.session_id, None)
        if client_random_str and client_random_str in CacheSession.session_container:
            self.random_str = client_random_str
        else:
            self.random_str = CacheSession.create_session_id()
            CacheSession.session_container[self.random_str] = {}

        expires_time = time.time() + expires
        handler.set_cookie(CacheSession.session_id, self.random_str, expires=expires_time)

    def __getitem__(self, key):
        ret = CacheSession.session_container[self.random_str].get(key, None)
        return ret

    def __setitem__(self, key, value):
        CacheSession.session_container[self.random_str][key] = value

    def __delitem__(self, key):
        if key in CacheSession.session_container[self.random_str]:
            del CacheSession.session_container[self.random_str][key]