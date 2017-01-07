# -*- coding: utf-8 -*-
import random
from library.db_connect import DBConnect
import sys


class CollaboratorMaster(object):

    def __init__(self):
        self._id = 0
        self._name = ''
        self._url = ''
        self._code = ''

        reload(sys)
        sys.setdefaultencoding("utf-8")

    @property  # プロパティ ゲッター
    def id(self):  # 自分自身が一つ目の引数に入るらしい
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def url(self):
        return self._url

    @property
    def code(self):
        return self._code

    def set_by_s3_folder(self, bucket_name):
        u"S3がトリガだった場合、フォルダをキーにして情報を取得する"
        row = []
        # AppLog.info_save('set_by_s3_folder', bucket_name)
        with DBConnect.get_connection() as con:
            with con.cursor() as cur:
                sql = """
                    select id,name,code
                    from collaborators
                    where is_valid = true and s3_bucket = %s"""
                cur.execute(sql, (str(bucket_name),))
                row = cur.fetchone()

        self._id = row[0]
        self._name = row[1]
        self._code = row[2]

    def set_operational(self):
        u"稼働できる取り組み先を一つ取得、自身に設定する"
        arr_collaborator = []
        with DBConnect.get_connection() as con:
            with con.cursor() as cur:
                cur.execute("""
                    select id,name,url,code
                    from collaborators
                    where is_valid = true and next_import_at < now()
                    order by next_import_at
                    limit 3
                """)
                arr_collaborator = cur.fetchall()

        random.shuffle(arr_collaborator)
        self._id = arr_collaborator[0][0]
        self._name = arr_collaborator[0][1]
        self._url = arr_collaborator[0][2]
        self._code = arr_collaborator[0][3]
