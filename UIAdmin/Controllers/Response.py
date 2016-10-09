#!/usr/bin/env python
# -*- coding:utf-8 -*-


class UserResponse:

    def __init__(self, status=True, message='', model_view=None):
        self.status = status
        self.message = message
        self.modelView = model_view