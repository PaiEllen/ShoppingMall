#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Model.User import IUserRepository
from Model.User import UserModel
from Model.User import UserType
from Model.User import VipType
from Repository.Admin.DbConnection import DbConnection


class UserRepository(IUserRepository):

    def __init__(self):
        self.db_conn = DbConnection()

    def fetch_one_by_email(self, email, password):
        ret = None

        cursor = self.db_conn.connect()
        sql = """select nid,username,password,email,last_login,vip,user_type from userinfo where email=%s and password=%s"""
        cursor.execute(sql, (email, password))
        db_result = cursor.fetchone()
        self.db_conn.close()
        print(type(db_result), db_result)
        if db_result:
            ret = UserModel(nid=db_result['nid'],
                            username=db_result['username'],
                            password=db_result['password'],
                            email=db_result['email'],
                            last_login=db_result['last_login'],
                            user_type_obj=UserType(nid=db_result['user_type']),
                            vip_type_obj=VipType(nid=db_result['vip']),)
            return ret
        return db_result

    def fetch_one_by_user(self, username, password):
        ret = None
        cursor = self.db_conn.connect()
        sql = """select nid,username,password,email,last_login,vip,user_type from userinfo where username=%s and password=%s"""
        cursor.execute(sql, (username, password))
        db_result = cursor.fetchone()
        self.db_conn.close()

        if db_result:
            ret = UserModel(nid=db_result['nid'],
                            username=db_result['username'],
                            password=db_result['password'],
                            email=db_result['email'],
                            last_login=db_result['last_login'],
                            user_type_obj=UserType(nid=db_result['user_type']),
                            vip_type_obj=VipType(nid=db_result['vip']),)
            return ret
        return db_result

    def fetch_user(self):
        cursor = self.db_conn.connect()
        sql = """select nid as value,username as text from userinfo"""
        cursor.execute(sql)
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def fetch_all_by_user_type(self,*args,**kwargs):
        ret = None
        cursor = self.db_conn.connect()
        sql = """select nid,username,email,last_login,vip,user_type from userinfo where user_type=1"""
        cursor.execute(sql)
        db_result = cursor.fetchall()
        self.db_conn.close()

        if db_result:
            ret = UserModel(nid=db_result['nid'],
                            username=db_result['username'],
                            email=db_result['email'],
                            last_login=db_result['last_login'],
                            user_type_obj=UserType(nid=db_result['user_type']),
                            vip_type_obj=VipType(nid=db_result['vip']), )
            return ret
        return db_result

    def update_last_login_by_nid(self, nid, current_date):
        cursor = self.db_conn.connect()
        sql = """update UserInfo set last_login=%s where nid=%s"""
        cursor.execute(sql, (current_date, nid))
        self.db_conn.close()

    def fetch_customer_by_page(self, start, offset):
        ret = None
        cursor = self.db_conn.connect()
        sql = """select nid,username,email,vip,user_type,password,last_login from userinfo order by nid desc limit %s offset %s """
        cursor.execute(sql, (offset, start))
        db_result = cursor.fetchall()
        self.db_conn.close()
        customer_obj = []
        if db_result:
            for item in db_result:
                ret = UserModel(nid=item['nid'],
                                username=item['username'],
                                password=item['password'],
                                email=item['email'],
                                last_login=item['last_login'],
                                user_type_obj=UserType(nid=item['user_type']),
                                vip_type_obj=VipType(nid=item['vip']),)
                customer_obj.append(ret)
            return customer_obj
        return db_result

    def fetch_customer_count(self):
        cursor = self.db_conn.connect()
        sql = """select count(1) as count from userinfo """
        cursor.execute(sql)
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']

    def exist_user(self, nid):
        cursor = self.db_conn.connect()
        sql = """select count(1) as count from userinfo where nid=%s """
        cursor.execute(sql, (nid,))
        db_result = cursor.fetchone()
        self.db_conn.close()

        return db_result['count']

    def add_user(self, user_type,vip,username,password,email,last_login,ctime):
        cursor = self.db_conn.connect()
        sql = """insert into userinfo (user_type,vip,username,password,email,last_login,ctime) values(%s,%s,%s,%s,%s,%s,%s)"""
        effect_rows = cursor.execute(sql, (user_type,vip,username,password,email,last_login,ctime))
        self.db_conn.close()
        return effect_rows

    def remove_customer(self,nid):
        cursor = self.db_conn.connect()
        sql = """delete from userinfo where nid=%s """
        effect_rows = cursor.execute(sql, (nid,))
        self.db_conn.close()
        return effect_rows

    def update_customer(self,nid, username, email, password, user_type, vip,last_login,ctime):
        cursor = self.db_conn.connect()
        sql = """update userinfo set username=%s,email=%s,password=%s,user_type=%s,vip=%s,last_login=%s,ctime=%s where nid=%s """
        effect_rows = cursor.execute(sql, (username, email, password, user_type, vip,last_login,ctime,nid))
        self.db_conn.close()
        return effect_rows
