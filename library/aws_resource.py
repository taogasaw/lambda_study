# -*- coding: utf-8 -*-

import boto3


def get_s3():
    return boto3.resource('s3')
