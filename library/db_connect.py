# -*- coding: utf-8 -*-
from library.settings import Settings

# lambda環境では、依存を解決するModuleを流用
# https://github.com/Miserlou/lambda-packages/
# pip2 install lambda-packages
# pip2 install psycopg2
import psycopg2


class DBConnect(object):

    @classmethod
    def get_connection(cls):
        u"このツール用のDBへの接続"
        con_str = "host=%s port=5432 dbname=%s user=%s password=%s" % (
            Settings.get_db_host(), Settings.get_db_name(),
            Settings.get_db_user(), Settings.get_db_pass()
        )
        con = psycopg2.connect(con_str)
        # withブロックで呼ばれる場合、自動的にcommitされるんだけど一応
        con.autocommit = True
        return con

    @classmethod
    def get_connection_web(cls):
        u"Web本体DBへのコネクション"
        con_str = "host=%s port=5432 dbname=%s user=%s password=%s" % (
            Settings.get_db_web_host(), Settings.get_db_web_name(),
            Settings.get_db_web_user(), Settings.get_db_web_pass()
        )
        con = psycopg2.connect(con_str)
        # withブロックで呼ばれる場合、自動的にcommitされるんだけど一応
        con.autocommit = True
        return con
