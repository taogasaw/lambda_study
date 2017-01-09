# -*- coding: utf-8 -*-
from library.util import Util
from library.csv_controller import CsvController
from library.settings import Settings
import sys
# lambdaには入っているが、開発環境には要インストール
# pip install boto3
import boto3

from datetime import datetime
import zipfile
import hashlib


def data_import(key):
    u'S3トリガのメイン関数'
    try:
        reload(sys)
        sys.setdefaultencoding("utf-8")

        Util.put('s3_main.data_import 開始', key)

        # S3からDL 別名で保存
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(Settings.get_s3_bucket())
        code = 'netmarketing'  # とりあえず決め打ち 本来は判別する
        org_csv_file_name = '{cd}_{dt}_{hs}_org.csv'.format(
          cd=code,
          dt=datetime.now().strftime('%Y%m%d_%H%M%S'),
          hs=hashlib.sha224(key).hexdigest()[0:10]  # 複数ファイル更新時にも被らないように
        )
        org_csv_file_path = '/tmp/' + org_csv_file_name
        bucket.download_file(key, org_csv_file_path)

        # CSVを各提供元の仕様に則って変換、CSVデータの配列を返す
        arr_csv_container = []
        import collaborator.netmarketing as collabo  # 本来は提携先によって取得処理を違わせる
        arr_csv_container = collabo.data_import(org_csv_file_path)

        # S3にCSVファイルとしてUP、ファイル名を返す
        csv_file = CsvController.save(org_csv_file_name, arr_csv_container, code)

        # データをサービス用DBに保存
        CsvController.insert_web_tmp_db(arr_csv_container, csv_file)

        # S3のファイルをバックアップしてから削除
        org_zip_file_name = org_csv_file_name.replace('.csv', '.zip')
        org_zip_file_path = org_csv_file_path.replace('.csv', '.zip')
        with zipfile.ZipFile(org_zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipFile:
            zipFile.write(org_csv_file_path, org_csv_file_name)

        with open(org_zip_file_path, 'rb') as org_up_data:
            bucket.put_object(Key=code + '/' + org_zip_file_name, Body=org_up_data)
        s3.Object(Settings.get_s3_bucket(), key).delete()

        Util.put('s3_main.data_import 終了', '[name] : ' + code)

    except:
        # エラー書き込み
        import traceback
        Util.put('s3_main.data_import エラー', traceback.format_exc())


# デバックが地味に手間なので、
# 事前に仮想環境を選択、s3にcsvをUPし、下記をターミナルにコピペ
#
# pythpn
# import s3_main
# s3_main.data_import('up/sample.csv')
# exit()
