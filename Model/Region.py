#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Infrastructure.DI.Meta import DIMetaClass

class IRegionRepository:

    def fetch_province_count(self):
        """
        获取所有的省份个数
        :return:
        """
        raise Exception()

    def fetch_province_by_page(self, limit, offset):
        """
        分页获取数据
        :param limit:
        :param offset:
        :return:
        """

    def exist_province(self, caption):
        """
        省份是否存在
        :param caption:
        :return:
        """
    def add_province(self, caption):
        """
        创建省份
        :param caption:
        :return:
        """
    def update_province(self, nid, caption):
        """
        更新省份
        :param nid:
        :param caption:
        :return:
        """
    def remove_province(self, nid):
        """
        删除省份
        :param nid:
        :return:
        """

    def fetch_city_by(self, province_id):
        """
        获取所有的省份
        :return:
        """
        raise Exception()

    def fetch_county_by(self, city_id):
        """
        获取所有的省份
        :return:
        """
        raise Exception()


class Region:

    def __init__(self, count, item_list):
        self.count = count
        self.itemList = item_list


class RegionService(metaclass=DIMetaClass):
    def __init__(self, region_repository):
        self.regionRepository = region_repository

    def get_province_count(self):
        count = self.regionRepository.fetch_province_count()
        return count

    def get_province_by_page(self, start, offset):

        result = self.regionRepository.fetch_province_by_page(start, offset)
        return result

    def get_province(self):
        return self.regionRepository.fetch_province()

    def create_province(self, caption):
        exist = self.regionRepository.exist_province(caption)
        if not exist:
             self.regionRepository.add_province(caption)
             return True

    def modify_province(self, nid, caption):
        exist = self.regionRepository.exist_province(caption)
        if not exist:
             self.regionRepository.update_province(nid, caption)
             return True

    def delete_province(self, nid):

        self.regionRepository.remove_province(nid)

    def get_city_by_province(self, province_id):
        rows = self.regionRepository.fetch_city_by_province(province_id)
        return rows

    def get_city_count(self):
        count = self.regionRepository.fetch_city_count()
        return count

    def get_city_by_page(self, start, offset):

        result = self.regionRepository.fetch_city_by_page(start, offset)
        return result

    def create_city(self, province_id, caption):
        exist = self.regionRepository.exist_city(province_id, caption)
        if not exist:
             self.regionRepository.add_city(province_id, caption)
             return True

    def delete_city(self, nid):

        self.regionRepository.remove_city(nid)

    def modify_city(self, nid, province_id, caption):
        exist = self.regionRepository.exist_city(province_id, caption)
        if not exist:
             self.regionRepository.update_city(nid, province_id, caption)
             return True

    def get_county_count(self):
        count = self.regionRepository.fetch_county_count()
        return count

    def get_county_by_page(self, start, offset):

        result = self.regionRepository.fetch_county_by_page(start, offset)
        return result

    def create_county(self, city_id, caption):
        exist = self.regionRepository.exist_county(city_id, caption)
        if not exist:
             self.regionRepository.add_county(city_id, caption)
             return True

    def delete_county(self, nid):

        self.regionRepository.remove_county(nid)

    def modify_county(self, nid, city_id, caption):
        exist = self.regionRepository.exist_county(city_id, caption)
        if not exist:
             self.regionRepository.update_county(nid, city_id, caption)
             return True


