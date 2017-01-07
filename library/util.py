# -*- coding: utf-8 -*-
from datetime import datetime
import urllib


class Util(object):

    @classmethod
    def str_none_to_empty(cls, obj):
        if obj is None:
            return ''
        else:
            return str(obj)

    @classmethod
    def int_none_to_zero(cls, obj):
        if obj is None:
            return 0
        else:
            return int(obj)

    @classmethod
    def bool_none_to_false(cls, obj):
        if obj is None:
            return False
        else:
            return bool(obj)

    @classmethod
    def url_decode(cls, obj):
        return urllib.unquote(str(obj)).replace('+', ' ')

    @classmethod
    def put(cls, *args):
        put_txt = '[%s]' % datetime.now()
        for arg in args:
            put_txt += '    ' + str(arg)
        print(put_txt)
