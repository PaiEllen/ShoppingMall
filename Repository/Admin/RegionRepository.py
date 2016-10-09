#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Model.Region import IRegionRepository
from Repository.Admin.DbConnection import DbConnection

class RegionRepository(IRegionRepository):

    def __init__(self):
        self.db_conn = DbConnection()

    def fetch_province(self):
        cursor = self.db_conn.connect()
        sql = """select nid,caption from province order by nid desc """
        cursor.execute(sql)
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result


    def fetch_province_by_page(self, start, offset):
        ret = None
        cursor = self.db_conn.connect()
        sql = """select nid,caption from province order by nid desc limit %s offset %s """
        cursor.execute(sql, (offset, start))
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def exist_province(self, caption):
        cursor = self.db_conn.connect()
        sql = """select count(1) as count from province where caption=%s """
        cursor.execute(sql, (caption,))
        db_result = cursor.fetchone()
        self.db_conn.close()

        return db_result['count']

    def add_province(self, caption):
        cursor = self.db_conn.connect()
        sql = """insert into province (caption) values(%s)"""
        effect_rows = cursor.execute(sql, (caption,))
        self.db_conn.close()
        return effect_rows

    def update_province(self, nid, caption):
        cursor = self.db_conn.connect()
        sql = """update province set caption=%s where nid=%s """
        effect_rows = cursor.execute(sql, (caption, nid,))
        self.db_conn.close()
        return effect_rows

    def remove_province(self, nid):
        cursor = self.db_conn.connect()
        sql = """delete from province where nid=%s """
        effect_rows = cursor.execute(sql, (nid,))
        self.db_conn.close()
        return effect_rows

    def fetch_province_count(self):
        cursor = self.db_conn.connect()
        sql = """select count(1) as count from province """
        cursor.execute(sql)
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']


    def fetch_city_by_province(self, province_id):

        cursor = self.db_conn.connect()
        sql = """select nid, caption from city where province_id=%s order by city.nid desc """
        cursor.execute(sql, (province_id, ))
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def fetch_city_by_page(self, start, offset):

        cursor = self.db_conn.connect()
        sql = """select city.nid as nid, city.caption as caption,province.caption as province, city.province_id as province_id from city left join province on city.province_id = province.nid order by city.nid desc limit %s offset %s """
        cursor.execute(sql, (offset, start))
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def fetch_city_count(self):
        cursor = self.db_conn.connect()
        sql = """select count(1) as count from city """
        cursor.execute(sql)
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']

    def exist_city(self, province_id,caption):
        cursor = self.db_conn.connect()
        sql = """select count(1) as count from city where caption=%s and province_id=%s"""
        cursor.execute(sql, (caption,province_id,))
        db_result = cursor.fetchone()
        self.db_conn.close()

        return db_result['count']

    def add_city(self, province_id,caption):
        cursor = self.db_conn.connect()
        sql = """insert into city (caption,province_id) values(%s,%s)"""
        effect_rows = cursor.execute(sql, (caption,province_id))
        self.db_conn.close()
        return effect_rows

    def remove_city(self, nid):
        cursor = self.db_conn.connect()
        sql = """delete from city where nid=%s """
        effect_rows = cursor.execute(sql, (nid,))
        self.db_conn.close()
        return effect_rows

    def update_city(self, nid, province_id, caption):
        cursor = self.db_conn.connect()
        sql = """update city set caption=%s,province_id=%s where nid=%s """
        effect_rows = cursor.execute(sql, (caption,province_id, nid,))
        self.db_conn.close()
        return effect_rows


    def fetch_county_by_page(self, start, offset):

        cursor = self.db_conn.connect()
        sql = """select
                    county.nid as nid,
                    county.caption as caption,
                    city.caption as city,
                    county.city_id as city_id,
                    province.caption as province,
                    city.province_id as province_id
                 from
                    county
                 left join city on county.city_id = city.nid
                 left join province on city.province_id = province.nid
                 order by county.nid desc
                 limit %s offset %s """
        cursor.execute(sql, (offset, start))
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def fetch_county_count(self):
        cursor = self.db_conn.connect()
        sql = """select count(1) as count from county """
        cursor.execute(sql)
        db_result = cursor.fetchone()
        self.db_conn.close()
        return db_result['count']


    def exist_county(self, city_id,caption):
        cursor = self.db_conn.connect()
        sql = """select count(1) as count from county where caption=%s and city_id=%s"""
        cursor.execute(sql, (caption,city_id,))
        db_result = cursor.fetchone()
        self.db_conn.close()

        return db_result['count']

    def add_county(self, city_id,caption):
        cursor = self.db_conn.connect()
        sql = """insert into county (caption,city_id) values(%s,%s)"""
        effect_rows = cursor.execute(sql, (caption,city_id))
        self.db_conn.close()
        return effect_rows

    def update_county(self, nid, city_id, caption):
        cursor = self.db_conn.connect()
        sql = """update county set caption=%s,city_id=%s where nid=%s """
        effect_rows = cursor.execute(sql, (caption,city_id, nid,))
        self.db_conn.close()
        return effect_rows

    def remove_county(self, nid):
        cursor = self.db_conn.connect()
        sql = """delete from county where nid=%s """
        effect_rows = cursor.execute(sql, (nid,))
        self.db_conn.close()
        return effect_rows