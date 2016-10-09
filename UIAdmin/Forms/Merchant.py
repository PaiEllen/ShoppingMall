#!/usr/bin/env python
# -*- coding:utf-8 -*-

from Infrastructure.Form.Forms import BaseForm
from Infrastructure.Form.Fields import StringField
from Infrastructure.Form.Fields import IntegerField
from Infrastructure.Form.Fields import EmailField
from Infrastructure.Form import Widget

from Model.User import UserService
from Repository.Admin.UserRepository import UserRepository


class MerchantForm(BaseForm):

    def __init__(self):
        self.nid = IntegerField(required=False, widget=Widget.InputText(attributes={'class': 'hide'}))

        self.name = StringField()
        self.domain = StringField()

        self.business_mobile = StringField()
        self.business_phone = StringField()
        self.qq = StringField()
        self.address = StringField(widget=Widget.TextArea(attributes={'class': 'address'}))
        self.backend_mobile = StringField()
        self.backend_phone = StringField()

        self.user_id = IntegerField(
            widget=Widget.Select(attributes={}, choices=UserService(UserRepository()).get_user_to_select()))

        self.province_id = IntegerField(
            widget=Widget.Select(attributes={'id': 'province'}, choices=[{'value': 0, 'text': '请选择省份'}]))
        self.city_id = IntegerField(
            widget=Widget.Select(attributes={'id': 'city'}, choices=[{'value': 0, 'text': '请选择市'}]))
        self.county_id = IntegerField(
            widget=Widget.Select(attributes={'id': 'county'}, choices=[{'value': 0, 'text': '请选择县（区）'}]))

        super(MerchantForm, self).__init__()