#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
from Infrastructure.Core.HttpRequest import BaseRequestHandler
from Model.Region import RegionService
from Repository.Admin.RegionRepository import RegionRepository

class ProvinceManagerHandler(BaseRequestHandler):

    def get(self, *args, **kwargs):
        # 打开页面，显示所有的省
        self.render('Admin/Region/ProvinceManager.html')


class ProvinceHandler(BaseRequestHandler):

    def get(self, *args, **kwargs):
        """
        获取
        :param args:
        :param kwargs:
        :return:
        """
        if self.get_argument('type', None) == 'all':
            ret = {'status': True, 'rows': "",'summary':''}
            try:
                region_service = RegionService()
                all_province_list = region_service.get_province()
                ret['rows'] = all_province_list
            except Exception as e:
                ret['status'] = False
                ret['summary'] = str(e)
            self.write(json.dumps(ret))
        else:
            ret = {'status': True,'total': 0, 'rows': [], 'summary': ''}
            try:
                rows = int(self.get_argument('rows', 10))
                page = int(self.get_argument('page', 1))
                start = (page-1)*rows

                region_service = RegionService()
                row_list = region_service.get_province_by_page(start, rows)
                row_count = region_service.get_province_count()

                ret['total'] = row_count
                ret['rows'] = row_list
            except Exception as e:
                ret['status'] = False
                ret['summary'] = str(e)

            self.write(json.dumps(ret))

    def post(self, *args, **kwargs):
        """
        添加
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status': False, 'summary': ''}
        caption = self.get_argument('caption', None)
        print(caption)
        if not caption:
            ret['summary'] = '省份不能为空'
        else:
            try:
                region_service = RegionService()
                result = region_service.create_province(caption)
                print(result)
                if not result:
                    ret['summary'] = '省份已经存在'
                else:
                    ret['status'] = True
            except Exception as e:
                ret['summary'] = str(e)

        self.write(json.dumps(ret))

    def put(self, *args, **kwargs):
        """
        更新
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status': False, 'summary': ''}
        nid = self.get_argument('nid', None)
        caption = self.get_argument('caption', None)
        if not caption or not nid:
            ret['summary'] = '省份不能为空'
        else:
            try:

                region_service = RegionService()
                result = region_service.modify_province(nid, caption)

                if not result:
                    ret['summary'] = '省份已经存在'
                else:
                    ret['status'] = True
            except Exception as e:
                ret['summary'] = str(e)
        self.write(json.dumps(ret))

    def delete(self, *args, **kwargs):
        """
        删除
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'status': False, 'summary': ''}

        nid = self.get_argument('nid', None)

        if not nid:
            ret['summary'] = '请选择要删除的省份'
        else:
            # 调用service去删除吧...
            # 如果删除失败，则显示错误信息
            try:
                region_service = RegionService()
                region_service.delete_province(nid)
                ret['status'] = True
            except Exception as e:
                ret['summary'] = str(e)
        self.write(json.dumps(ret))


class CityManagerHandler(BaseRequestHandler):

    def get(self, *args, **kwargs):
        # 打开页面，显示所有的省
        self.render('Admin/Region/CityManager.html')


class CityHandler(BaseRequestHandler):

    def get(self, *args, **kwargs):
        if self.get_argument('type', None) == 'province':
            ret = {'status': True, 'rows': "", 'summary':""}
            try:
                province_id = self.get_argument('province_id', None)

                if not province_id:
                    ret['summary'] = '请指定省份ID'
                    ret['status'] = False
                else:

                    region_service = RegionService(RegionRepository())
                    rows = region_service.get_city_by_province(province_id)
                    ret['rows'] = rows
            except Exception as e:
                ret['summary'] = str(e)
                ret['status'] = False

            self.write(json.dumps(ret))
        else:
            ret = {'status': True, 'total': 0, 'rows': [], 'summary': ''}
            try:
                rows = int(self.get_argument('rows', 10))
                page = int(self.get_argument('page', 1))
                start = (page-1)*rows

                region_service = RegionService(RegionRepository())
                row_list = region_service.get_city_by_page(start, rows)
                row_count = region_service.get_city_count()

                ret['total'] = row_count
                ret['rows'] = row_list
            except Exception as e:
                ret['summary'] = str(e)
                ret['status'] = False
            self.write(json.dumps(ret))

    def post(self, *args, **kwargs):
        ret = {'status': False, 'summary': ''}
        try:
            caption = self.get_argument('caption', None)
            province_id = self.get_argument('province_id',None)
            province_id = int(province_id)
            if not caption or not province_id:
                ret['summary'] = '市不能为空'
            else:

                region_service = RegionService(RegionRepository())
                result = region_service.create_city(province_id, caption)
                if not result:
                    ret['summary'] = '市已经存在'
                else:
                    ret['status'] = True
        except Exception as e:
                ret['summary'] = str(e)
        self.write(json.dumps(ret))

    def delete(self, *args, **kwargs):
        ret = {'status': False, 'summary': ''}
        try:
            nid = self.get_argument('nid', None)

            if not nid:
                ret['summary'] = '请选择要删除的市'
            else:
                # 调用service去删除吧...
                # 如果删除失败，则显示错误信息

                region_service = RegionService(RegionRepository())
                region_service.delete_city(nid)
                ret['status'] = True
        except Exception as e:
                ret['summary'] = str(e)
        self.write(json.dumps(ret))

    def put(self, *args, **kwargs):
        ret = {'status': False, 'summary': ''}
        try:
            nid = self.get_argument('nid', None)
            caption = self.get_argument('caption', None)
            province_id = self.get_argument('province_id',None)
            if not caption or not province_id or not nid:
                ret['summary'] = '选择错误'
            else:
                from Model.Region import RegionService
                from Repository.RegionRepository import RegionRepository

                region_service = RegionService(RegionRepository())
                result = region_service.modify_city(nid, province_id, caption)
                if not result:
                    ret['summary'] = '市已经存在'
                else:
                    ret['status'] = True
        except Exception as e:
                ret['summary'] = str(e)
        self.write(json.dumps(ret))


class CountyManagerHandler(BaseRequestHandler):

    def get(self, *args, **kwargs):
        # 打开页面，显示所有的省
        self.render('Admin/Region/CountyManager.html')


class CountyHandler(BaseRequestHandler):

    def get(self, *args, **kwargs):
        if self.get_argument('type', None) == 'all':
            pass
        else:
            ret = {'total': 0, 'rows': [],'status':True, 'summary': ''}
            try:
                rows = int(self.get_argument('rows', 10))
                page = int(self.get_argument('page', 1))
                start = (page-1)*rows

                region_service = RegionService(RegionRepository())
                row_list = region_service.get_county_by_page(start, rows)
                row_count = region_service.get_county_count()

                ret['total'] = row_count
                ret['rows'] = row_list
            except Exception as e:
                ret['summary'] = str(e)
                ret['status'] = False
            self.write(json.dumps(ret))

    def post(self, *args, **kwargs):
        ret = {'status': False, 'summary': ''}
        try:
            caption = self.get_argument('caption', None)
            city_id = self.get_argument('city_id', None)
            city_id = int(city_id)
            if not caption or not city_id:
                ret['summary'] = '县（区）不能为空'
            else:

                region_service = RegionService(RegionRepository())
                result = region_service.create_county(city_id, caption)
                if not result:
                    ret['summary'] = '县（区）已经存在'
                else:
                    ret['status'] = True

        except Exception as e:
            ret['summary'] = str(e)

        self.write(json.dumps(ret))

    def put(self, *args, **kwargs):

        ret = {'status': False, 'summary': ''}
        try:
            nid = self.get_argument('nid', None)
            caption = self.get_argument('caption', None)
            city_id = self.get_argument('city_id',None)

            if not caption or not city_id or not nid:
                ret['summary'] = '选择错误'
            else:

                region_service = RegionService(RegionRepository())
                result = region_service.modify_county(nid, city_id, caption)
                if not result:
                    ret['summary'] = '县已经存在'
                else:
                    ret['status'] = True
        except Exception as e:
            ret['summary'] = str(e)
        self.write(json.dumps(ret))

    def delete(self, *args, **kwargs):
        ret = {'status': False, 'summary': ''}
        try:
            nid = self.get_argument('nid', None)

            if not nid:
                ret['summary'] = '请选择要删除的市'
            else:
                # 调用service去删除吧...
                # 如果删除失败，则显示错误信息

                region_service = RegionService(RegionRepository())
                region_service.delete_county(nid)
                ret['status'] = True
        except Exception as e:
            ret['summary'] = str(e)
        self.write(json.dumps(ret))