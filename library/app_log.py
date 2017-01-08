# -*- coding: utf-8 -*-
from library.db_connect import DBConnect
import sys

from library.util import Util


class AppLog(object):
    def __init__(self):
        self._title = ''
        self._message = ''
        # ホントはもう少しあるけど

        reload(sys)
        sys.setdefaultencoding("utf-8")

    @property  # プロパティ ゲッター
    def title(self):  # 自分自身が一つ目の引数に入るらしい
        return self._title

    @title.setter  # セッター
    def title(self, val):
        self._title = str(val)

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, val):
        self._message = str(val)

    @classmethod
    def save(cls, title, message):
        app_log = cls()
        app_log.title = title
        app_log.message = message
        app_log.__save()

    def __save(self):
        if self._title == '':
            raise Exception('タイトルは必須です')

        # 本来はエラーとInfoを切り分けて処理する
        try:
            with DBConnect.get_connection() as con:
                with con.cursor() as cur:
                    cur.execute("""
                        INSERT INTO app_logs (title, message)
                        VALUES (%s, %s)""", (self._title, self._message))
        except Exception as e:
            Util.put('AppLog.save エラー',e)

        Util.put(u'■■■ AppLog ■■■', self._title, self._message)
