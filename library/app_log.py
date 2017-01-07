# -*- coding: utf-8 -*-
from library.db_connect import DBConnect
import logging
import sys

from library.util import Util


class AppLog(object):
    def __init__(self):
        self._title = ''
        self._message = ''
        self._status = 0
        self._code = 90
        self._level = 1

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

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, val):
        self._status = int(val)

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, val):
        self._level = int(val)

    # DBに入れる
    def save_error(self):
        self._code = 90
        self.__save()

    # DBに入れる
    def save_info(self):
        self._code = 10
        self.__save()

    @classmethod
    def info_save(cls, title, message):
        if title == '':
            raise Exception('タイトルは必須です')

        app_log = cls()
        app_log.title = title
        app_log.message = message
        app_log.level = 1
        app_log.save_info()

    def __save(self):
        if self._title == '':
            raise Exception('タイトルは必須です')
        if self._level < 1:
            self._level = 1

        try:
            with DBConnect.get_connection() as con:
                with con.cursor() as cur:
                    cur.execute("""
                        INSERT INTO app_logs (title, message, code, status, level)
                        VALUES (%s, %s, %s, %s, %s)""", (
                            self._title, self._message, self._code, self._status, self._level
                        )
                    )
        except Exception as e:
            Util.put('AppLog.save エラー',e)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        if self._code >= 90:
            logger.setLevel(logging.ERROR)
            logger.error(self._title + '\r\n\r\n' + self._message)
            Util.put(u'■■■ Error ■■■', self._title, self._message)
        else:
            logger.info(self._title + '\r\n\r\n' + self._message)
            Util.put(self._title, self._message)
