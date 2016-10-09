#!/usr/bin/env python
# -*- coding: utf-8 -*-
#建模
from Infrastructure.DI.Meta import DIMetaClass

class VipType:

    VIP_TYPE = (
        {'nid': 1, 'caption': '铜牌'},
        {'nid': 2, 'caption': '银牌'},
        {'nid': 3, 'caption': '金牌'},
        {'nid': 4, 'caption': '铂金'},
    )

    def __init__(self, nid):
        self.nid = nid

    def get_caption(self):
        caption = None

        for item in VipType.VIP_TYPE:
            if item['nid'] == self.nid:
                caption = item['caption']
                break
        return caption

    caption = property(get_caption)


class UserType:

    USER_TYPE = (
        {'nid': 1, 'caption': '用户'},
        {'nid': 2, 'caption': '商户'},
        {'nid': 3, 'caption': '管理员'},
    )

    def __init__(self, nid):
        self.nid = nid

    def get_caption(self):
        caption = None

        for item in UserType.USER_TYPE:
            if item['nid'] == self.nid:
                caption = item['caption']
                break
        return caption

    caption = property(get_caption)


class UserModel:
    def __init__(self, nid, username,password, email, last_login, user_type_obj, vip_type_obj):
        self.nid = nid
        self.username = username
        self.email = email
        self.password = password
        self.last_login = last_login
        self.user_type_obj = user_type_obj
        self.vip_type_obj = vip_type_obj

#接口
class IUserRepository:

    def fetch_one_by_user(self,user,pwd):
        """
        根据用户名和密码获取对象
        :param user:
        :param pwd:
        :return:
        """

    def fetch_one_by_email(self, user, pwd):
        """
        根据邮箱和密码获取对象
        :param user:
        :param pwd:
        :return:
        """

    def fetch_all_by_user_type(self):
        """
        获取普通用户数据
        :return:
        """

    def fetch_customer_by_page(self, limit, offset):
        """
        分页获取数据
        :param limit:
        :param offset:
        :return:
        """

    def fetch_customer_count(self):
        """
        获取所有的普通用户个数
        :return:
        """
        raise Exception()

    def exist_user(self, username):
        """
        用户是否存在
        :param username:
        :return:
        """

    def add_user(self, user_type,vip,username,password,email,last_login,ctime):
        """
        添加新用户
        :param username:
        :return:
        """

    def remove_customer(self,nid):
        """
        删除普通用户
        :return:
        """

    def update_customer(self, user_type, vip, username, password, email, last_login, ctime):
        """
        更新新用户
        :param username:
        :return:
        """
#用户登录协调


class UserService(metaclass=DIMetaClass):
    def __init__(self, user_repository):
        """
        :param user_repository: 数据仓库对象
        """
        self.userRepository = user_repository

    def check_login(self,user,email,pwd):
        if user:
            #数据仓库执行SQL后返回的字典
            #{"nid":1,username:xxx,vip:2,usertype:1}
            ret = self.userRepository.fetch_one_by_user(user,pwd)
        else:
            ret = self.userRepository.fetch_one_by_email(email,pwd)
        return ret

    def get_user_to_select(self):

        user_list = self.userRepository.fetch_user()

        return user_list

#后台获取用户所有信息
class CustomerService(metaclass=DIMetaClass):
    def __init__(self,user_repository):
        self.userRepository = user_repository

    def all_customer_info(self):
        """所有普通用户信息"""
        sub_res = self.userRepository.fetch_all_by_user_type()
        print(sub_res)
        return sub_res

    def get_customer_by_page(self, start, offset):
        """分页"""
        result = self.userRepository.fetch_customer_by_page(start, offset)
        ret = []
        for item in result:
            temp = {'nid': item.nid,
                    'username': item.username,
                    'email': item.email,
                    'password': item.password,
                    'user_type': item.user_type_obj.caption,
                    'vip': item.vip_type_obj.caption,
                    }
            ret.append(temp)
        return ret

    def get_customer_count(self):
        """数据总数"""
        count = self.userRepository.fetch_customer_count()
        return count

    def create_customer(self,username,email,password,user_type,vip):
        exist = self.userRepository.exist_user(username)
        if not exist:
            self.userRepository.add_user(user_type,vip,username,password,email,last_login=None,ctime=None)
            return True

    def delete_customer(self,nid):
        self.userRepository.remove_customer(nid)

    def modify_Customer(self, nid, username, email, password, user_type, vip):
        exist = self.userRepository.exist_user(username)
        if not exist:
            self.userRepository.update_customer(nid, username, email, password, user_type, vip,last_login=None,ctime=None)
            return True