#!/usr/bin/env python
# -*- coding:utf-8 -*-


class InputText:

    def __init__(self, attributes):
        """
        :param attributes: {'id': '123'}
        :return:
        """
        self.attributes = attributes

    def __str__(self):
        template = "<input type='text' %s />"
        attr_list = []
        for k, v in self.attributes.items():
            temp = "%s='%s' " % (k,v,)
            attr_list.append(temp)
        tag = template % (''.join(attr_list))
        return tag


class TextArea:

    def __init__(self, attributes):
        """
        :param attributes: {'id': '123'}
        :return:
        """
        self.attributes = attributes

    def __str__(self):
        template = "<textarea %s />%s</textarea>"
        attr_list = []
        val = ""
        for k, v in self.attributes.items():
            if k == 'value':
                val = v
            else:
                temp = "%s='%s' " % (k,v,)
                attr_list.append(temp)
        tag = template % (''.join(attr_list), val)
        return tag

class PasswordText:

    def __init__(self, attributes):
        self.attributes = attributes

    def __str__(self):
        template = "<input type='password' %s />"
        attr_list = []
        for k, v in self.attributes.items():
            temp = "%s='%s' " % (k,v,)
            attr_list.append(temp)
        tag = template % (''.join(attr_list))
        return tag


class Select:

    def __init__(self, attributes, choices, selected_value=None, selected_text=None):
        """

        :param attributes:{'id': 'i1', 'name':'n'}
        :param choices: [{'value':'1','text':'内容'},{'value':'2','text':'内容'}] 或者 [(1,'内容'),(1,'内容')]
        :param selected_value:
        :param selected_text:
        :return:
        """
        self.attributes = attributes
        self.choices = choices
        self.selected_value = selected_value
        self.selected_text = selected_text

    def __str__(self):
        template = "<select %s />%s</select>"

        attr_list = []

        for k, v in self.attributes.items():
            temp = "%s='%s' " % (k, v,)
            attr_list.append(temp)

        body_list = []
        for choice in self.choices:
            if isinstance(choice, dict):
                value = choice['value']
                text = choice['text']
            elif isinstance(choice, tuple) or isinstance(choice, list):
                value = choice[0]
                text = choice[1]
            else:
                raise Exception('选项参数错误')

            if value == self.selected_value or text == self.selected_text:
                option = "<option selected='selected' value='%s'>%s</option>" % (value, text,)
            else:
                option = "<option value='%s'>%s</option>" % (value, text,)
            body_list.append(option)

        tag = template % ("".join(attr_list), ''.join(body_list))

        return tag




