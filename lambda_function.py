# -*- coding: utf-8 -*-
from library.util import Util
import sys


# イベントハンドラ
def lambda_handler(event, context):
    reload(sys)
    sys.setdefaultencoding("utf-8")

    Util.put('lambda_handler', str(event))

    # イベントで振る舞いを変える
    for event_record in event['Records']:
        if 's3' in event_record:  # S3イベントの場合
            key = Util.url_decode(event_record['s3']['object']['key'])
            Util.put('key', key)
            import s3_main
            s3_main.data_import(key)
        else:  # cronイベントの場合
            pass
