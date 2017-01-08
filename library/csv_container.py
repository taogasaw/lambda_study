# -*- coding: utf-8 -*-
import sys


# 本来はもっと大量にあるけど、いったん2カラムだけ
class CsvContainer(object):
    u"CSVの定形フォーマットで保持するクラス"
    def __init__(self):
        self._name = ''
        self._telephone = None

        reload(sys)
        sys.setdefaultencoding("utf-8")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = str(val)

    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, val):
        self._telephone = val
