#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
from Infrastructure.Core.HttpRequest import BaseRequestHandler
from Model.Merchant import MerchantService
from Repository.Admin.MerchantRepository import MerchantRepository

from UIAdmin.Forms.Merchant import MerchantForm
from pymysql.err import IntegrityError


class MerchantManagerHandler(BaseRequestHandler):

    def get(self, *args, **kwargs):
        # 打开页面，显示所有的省
        self.render('Admin/Merchant/MerchantManager.html')


class MerchantHandler(BaseRequestHandler):

    def get(self, *args, **kwargs):

        req_type = self.get_argument('type', None)
        if req_type == 'pagination':
            ret = {'status': False, 'message': '', 'total': 0, 'rows': []}
            try:
                page = int(self.get_argument('page', 1))
                rows = int(self.get_argument('rows', 10))
                start = (page-1) * rows
                service = MerchantService(MerchantRepository())
                ret['total'], ret['rows'] = service.get_merchant_by_page(start, rows)
                ret['status'] = True
            except Exception as e:
                ret['message'] = str(e)
            self.write(json.dumps(ret))
            return
        self.render('Admin/Merchant/MerchantManager.html')


class MerchantEditHandler(BaseRequestHandler):

    def get(self, *args, **kwargs):
        error_summary = ''
        merchant_id = self.get_argument('nid', None)
        if not merchant_id:
            crumbs = "添加商户"
            form = MerchantForm()
            method = 'POST'
        else:
            crumbs = "编辑商户"
            form = MerchantForm()
            # 根据ID获取用户信息，
            service = MerchantService(MerchantRepository())

            detail = service.get_merchant_detail_by_nid(merchant_id)

            county_caption = detail.pop('county_caption')
            county_id = detail.get('county_id')
            form.county_id.widget.choices.append({'value': county_id, 'text': county_caption})

            method = 'PUT'
            form.init_value(detail)

        self.render('Admin/Merchant/MerchantEdit.html', form=form, crumbs=crumbs, method=method, summary=error_summary, nid=merchant_id)

    def post(self, *args, **kwargs):
        """
        创建商户
        :param args:
        :param kwargs:
        :return:
        """
        method = self.get_argument('_method', None)

        if method == 'PUT':
            return self.put(self, *args, **kwargs)

        error_summary = ""
        form = MerchantForm()
        try:
            is_valid = form.valid(self)
            if is_valid:
                if form._value_dict['county_id'] == '0':
                    form._error_dict['county_id'] = '请选择县(区)ID'
                else:
                    del form._value_dict['nid']
                    del form._value_dict['city_id']
                    del form._value_dict['province_id']
                    print(form._value_dict)
                    # 添加到数据库
                    service = MerchantService(MerchantRepository())
                    service.create_merchant_by_kwargs(**form._value_dict)
                    self.redirect('/MerchantManager.html')
                    return
            else:
                form.init_value(form._value_dict)
        except IntegrityError as e:
            error_summary = '商户名称或登陆用户必须唯一'
        except Exception as e:
            error_summary = str(e)

        self.render('Admin/Merchant/MerchantEdit.html', form=form, crumbs='添加商户', method='POST', summary=error_summary,nid=None)

    def put(self, *args, **kwargs):
        """
        修改商户
        :param args:
        :param kwargs:
        :return:
        """
        error_summary = ""
        form = MerchantForm()
        merchant_id = self.get_argument('nid', None)
        try:
            is_valid = form.valid(self)

            if is_valid:
                if form._value_dict['county_id'] == '0':
                    form._error_dict['county_id'] = '请选择县(区)ID'
                else:
                    nid = form._value_dict.pop('nid')
                    del form._value_dict['city_id']
                    del form._value_dict['province_id']

                    # 添加到数据库
                    service = MerchantService(MerchantRepository())
                    service.update_merchant_by_kwargs(nid, **form._value_dict)
                    self.redirect('/MerchantManager.html')
                    return
            else:
                form.init_value(form._value_dict)

        except Exception as e:
            error_summary = str(e)

        service = MerchantService(MerchantRepository())
        detail = service.get_merchant_detail_by_nid(merchant_id)
        county_caption = detail.pop('county_caption')
        county_id = detail.get('county_id')
        form.county_id.widget.choices.append({'value': county_id, 'text': county_caption})

        self.render('Admin/Merchant/MerchantEdit.html', form=form, crumbs='编辑商户', method='PUT',summary=error_summary, nid=merchant_id)