# -*- coding: utf-8 -*-
import os


class Settings(object):

    @classmethod
    def get_db_host(cls):
        return os.environ.get('POKE_IMPORTER_DB_HOST')

    @classmethod
    def get_db_user(cls):
        return os.environ.get('POKE_IMPORTER_DB_USER')

    @classmethod
    def get_db_pass(cls):
        return os.environ.get('POKE_IMPORTER_DB_PASS')

    @classmethod
    def get_db_name(cls):
        return os.environ.get('POKE_IMPORTER_DB_NAME')

    @classmethod
    def get_db_web_host(cls):
        return os.environ.get('POKE_WEB_DB_HOST')

    @classmethod
    def get_db_web_user(cls):
        return os.environ.get('POKE_WEB_DB_USER')

    @classmethod
    def get_db_web_pass(cls):
        return os.environ.get('POKE_WEB_DB_PASS')

    @classmethod
    def get_db_web_name(cls):
        return os.environ.get('POKE_WEB_DB_NAME')

    @classmethod
    def get_s3_bucket(cls):
        return os.environ.get('POKE_IMPORTER_S3_BUCKET')
