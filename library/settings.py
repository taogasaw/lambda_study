# -*- coding: utf-8 -*-
import os


class Settings(object):

    @classmethod
    def get_db_host(cls):
        return os.environ.get('IMPORTER_DB_HOST')

    @classmethod
    def get_db_user(cls):
        return os.environ.get('IMPORTER_DB_USER')

    @classmethod
    def get_db_pass(cls):
        return os.environ.get('IMPORTER_DB_PASS')

    @classmethod
    def get_db_name(cls):
        return os.environ.get('IMPORTER_DB_NAME')

    @classmethod
    def get_s3_bucket(cls):
        return os.environ.get('IMPORTER_S3_BUCKET')
