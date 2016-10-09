#!/usr/bin/env python
# -*- coding:utf-8 -*-
from .CacheSession import CacheSession
from .MemcacheSession import MemcacheSession
from .RedisSession import RedisSession


class SessionFactory:

    __session = CacheSession()

    @staticmethod
    def get_session():
        return SessionFactory.__session


    @staticmethod
    def set_session(session):
        SessionFactory.__session = session
