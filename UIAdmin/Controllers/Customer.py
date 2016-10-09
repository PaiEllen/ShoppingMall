#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from Infrastructure.Core.HttpRequest import BaseRequestHandler
from Model.User import CustomerService
from Repository.Admin.UserRepository import UserRepository


class CustomerManagerHandler(BaseRequestHandler):

    def get(self, *args, **kwargs):
        self.render("Admin/UserManager/CustomerManager.html")


class CustomerHandler(BaseRequestHandler):
    def get(self, *args, **kwargs):
        """
        获取
        :param args:
        :param kwargs:
        :return:
        """
        if self.get_argument('type', None) == 'all':
            ret = {'status': True, 'rows': "", 'summary': ''}
            try:
                customer_service = CustomerService(UserRepository())
                all_customer_list = customer_service.all_customer_info()
                ret['rows'] = all_customer_list
            except Exception as e:
                ret['status'] = False
                ret['summary'] = str(e)
            self.write(json.dumps(ret))
        else:
            ret = {'status': True, 'total': 0, 'rows': [], 'summary': ''}
            try:
                rows = int(self.get_argument('rows', 10))
                page = int(self.get_argument('page', 1))
                start = (page - 1) * rows
                customer_service = CustomerService()
                row_list = customer_service.get_customer_by_page(start, rows)
                row_count = customer_service.get_customer_count()
                ret['total'] = row_count
                ret['rows'] = row_list
            except Exception as e:
                ret['status'] = False
                ret['summary'] = str(e)
            self.write(json.dumps(ret))

    def post(self, *args, **kwargs):
        """
        添加用户
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status': False, 'summary': ''}
        username = self.get_argument('username', None)
        email = self.get_argument('email', None)
        password = self.get_argument('password', None)
        user_type = self.get_argument('user_type', None)
        vip = self.get_argument('vip', None)
        if not username:
            ret['summary'] = '用户名不能为空'
        else:
            try:
                customer_service = CustomerService(UserRepository())
                result = customer_service.create_customer(username=username,email=email,password=password,user_type=user_type,vip=vip)
                if not result:
                    ret['summary'] = '用户已经存在'
                else:
                    ret['status'] = True
            except Exception as e:
                ret['summary'] = str(e)

        self.write(json.dumps(ret))

    def put(self, *args, **kwargs):
        """
        更新普通用户信息
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status': False, 'summary': ''}
        nid = self.get_argument('nid', None)
        username = self.get_argument('username', None)
        email = self.get_argument('email', None)
        password = self.get_argument('password', None)
        user_type = self.get_argument('user_type', None)
        vip = self.get_argument('vip', None)
        if not username or not nid:
            ret['summary'] = '用户名不能为空'
        else:
            try:
                region_service = CustomerService()
                result = region_service.modify_Customer(nid=nid, username=username,email=email,password=password,user_type=user_type,vip=vip)

                if not result:
                    ret['summary'] = '用户已经存在'
                else:
                    ret['status'] = True
            except Exception as e:
                ret['summary'] = str(e)
        self.write(json.dumps(ret))

    def delete(self, *args, **kwargs):
        """
        删除用户
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status': False, 'summary': ''}

        nid = self.get_argument('nid', None)
        if not nid:
            ret['summary'] = '请选择要删除的数据'
        else:
            # 调用service去删除吧...
            # 如果删除失败，则显示错误信息
            try:
                customer_service = CustomerService(UserRepository())
                customer_service.delete_customer(nid)
                ret['status'] = True
            except Exception as e:
                ret['summary'] = str(e)
        self.write(json.dumps(ret))


class BusinessManagerHandler(BaseRequestHandler):

    def get(self, *args, **kwargs):
        self.render("Admin/UserManager/BusinessManager.html")
