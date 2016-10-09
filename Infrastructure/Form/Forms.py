#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Infrastructure.Form import Fields
from Infrastructure.Form import Widget


class BaseForm:

    def __init__(self):
        self._value_dict = {}
        self._error_dict = {}
        self._valid_status = True
        self.initialize()

    def initialize(self):
        for field_name, field_obj in self.__dict__.items():
            if field_name.startswith('_'):
                continue
            field_obj.name = field_name

    def init_value(self, init_dict):
        for field_name, field_obj in self.__dict__.items():
            if field_name.startswith('_'):
                continue
            if field_name not in init_dict:
                continue

            if type(field_obj.widget) == Widget.Select:

                field_obj.widget.selected_value = init_dict[field_name]
            else:
                field_obj.value = init_dict[field_name]

    def valid(self, handler):

        for field_name, field_obj in self.__dict__.items():
            if field_name.startswith('_'):
                continue

            if type(field_obj) == Fields.CheckBoxField:
                post_value = handler.get_arguments(field_name, None)

            elif type(field_obj) == Fields.FileField:
                post_value = []
                file_list = handler.request.files.get(field_name, [])
                for file_item in file_list:
                    post_value.append(file_item['filename'])
            else:
                post_value = handler.get_argument(field_name, None)

            field_obj.match(field_name, post_value)
            if field_obj.is_valid:
                self._value_dict[field_name] = field_obj.value
            else:
                self._error_dict[field_name] = field_obj.error
                self._valid_status = False
        return self._valid_status