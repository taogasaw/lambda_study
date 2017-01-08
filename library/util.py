# -*- coding: utf-8 -*-
from datetime import datetime
import urllib
import logging


class Util(object):

    @classmethod
    def url_decode(cls, obj):
        return urllib.unquote(str(obj)).replace('+', ' ')

    @classmethod
    def bp(cls):
        import pdb
        pdb.set_trace()

    @classmethod
    def put(cls, *args):
        put_txt = '[%s]' % datetime.now()
        for arg in args:
            put_txt += '    ' + str(arg)
        print(put_txt)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.info(put_txt)
