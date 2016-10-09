#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Model.Merchant import IMerchantRepository
from Repository.Admin.DbConnection import DbConnection

class MerchantRepository(IMerchantRepository):

    def __init__(self):
        self.db_conn = DbConnection()

    def fetch_merchant_count(self):
        cursor = self.db_conn.connect()
        sql = """select count(1) as count  from merchant """
        cursor.execute(sql)
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']

    def fetch_merchant_by_page(self, start, rows):
        cursor = self.db_conn.connect()
        sql = """select nid,name,domain from merchant order by nid desc limit %s offset %s"""
        cursor.execute(sql, (rows,start,))
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def fetch_merchant_detail_by_nid(self, nid):
        cursor = self.db_conn.connect()
        sql = """   select
                        merchant.nid as nid,
                        name,
                        domain,
                        business_phone,
                        business_mobile,
                        qq,
                        backend_phone,
                        backend_mobile,
                        address,
                        user_id,
                        county_id,
                        county.caption as county_caption
                    from
                        merchant
                    left join userinfo on merchant.user_id = userinfo.nid
                    left join county on merchant.county_id = county.nid
                    where merchant.nid=%s"""
        cursor.execute(sql, (nid,))
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result

    def add_merchant(self, **kwargs):
        cursor = self.db_conn.connect()
        sql = """insert into merchant(%s) values(%s)"""
        key_list = []
        value_list = []
        for k, v in kwargs.items():
            key_list.append(k)
            value_list.append('%%(%s)s' % k)
        sql = sql % (','.join(key_list), ','.join(value_list))
        cursor.execute(sql, kwargs)
        self.db_conn.close()

    def update_merchant(self, nid, **kwargs):
        cursor = self.db_conn.connect()
        sql = """update merchant set %s where nid=%s"""
        value_list = []
        for k, v in kwargs.items():
            value_list.append('%s=%%(%s)s' % (k, k))
        sql = sql % (','.join(value_list), nid )

        cursor.execute(sql, kwargs)
        self.db_conn.close()
