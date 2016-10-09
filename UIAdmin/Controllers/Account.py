#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
from Infrastructure.Core.HttpRequest import BaseRequestHandler
from Infrastructure.utils import check_code
from Model.User import UserService


class LoginHandler(BaseRequestHandler):
    def get(self, *args, **kwargs):
        self.render("Admin/Account/login.html")

    def post(self, *args, **kwargs):
        username = self.get_argument("username",None)
        email = self.get_argument("email",None)
        pwd = self.get_argument("pwd",None)
        code = self.get_argument("checkcode",None)
        service = UserService()
        result = service.check_login(user=username,email=email,pwd=pwd)
        #obj封装了所有的用户信息，UserModel对象
        if result and code.upper() == self.session["CheckCode"].upper():
            self.session['username'] = result.username
            self.redirect("/ProvinceManager.html")
        else:
            self.write("alert('error')")


class CheckCodeHandler(BaseRequestHandler):
    def get(self, *args, **kwargs):
        stream = io.BytesIO()
        img, code = check_code.create_validate_code()
        img.save(stream, "png")
        self.session["CheckCode"] = code
        self.write(stream.getvalue())