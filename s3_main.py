# -*- coding: utf-8 -*-
from library.app_log import AppLog
from library.util import Util
from library.collaborator_master import CollaboratorMaster
from library.csv_controller import CsvController
from library.settings import Settings
import library.aws_resource as AwsResources
import sys

from datetime import datetime
import zipfile
import hashlib


def data_import(key):
    u'S3トリガのメイン関数'
    try:
        reload(sys)
        sys.setdefaultencoding("utf-8")

        # import pdb; pdb.set_trace()
        save_info = ''
        AppLog.info_save('s3_main.data_import 開始', key)

        # RootFolderをもとに、マスタ情報を取得する
        collabo_master = CollaboratorMaster()
        root_folder = key.split('/')[0]
        collabo_master.set_by_s3_folder(root_folder)

        # S3からDL 別名で保存
        s3 = AwsResources.get_s3()
        bucket = s3.Bucket(Settings.get_s3_bucket())
        org_csv_file_name = '{cd}_{dt}_{hs}_org.csv'.format(
          cd=collabo_master.code,
          dt=datetime.now().strftime('%Y%m%d_%H%M%S'),
          hs=hashlib.sha224(key).hexdigest()[0:10]
        )
        org_csv_file_path = '/tmp/' + org_csv_file_name
        bucket.download_file(key, org_csv_file_path)

        # CSVを各コラボレーターの仕様に則って変換、CSVデータの配列を返す
        arr_csv_container = []
        if collabo_master.id == 1:
            import collaborator.netmarketing_recruit_agent as collabo  # 提携先によって、取得処理を違わせる
            arr_csv_container = collabo.data_import(org_csv_file_path, collabo_master)

        # S3にCSVファイルとしてUP、ファイル名を返す
        csv_file = CsvController.save(org_csv_file_name, arr_csv_container, collabo_master)

        # データをぽけのtmpDBに保存
        CsvController.insert_web_tmp_db(arr_csv_container, csv_file)

        # S3のファイルをバックアップしてから削除
        org_zip_file_name = org_csv_file_name.replace('.csv', '.zip')
        org_zip_file_path = org_csv_file_path.replace('.csv', '.zip')
        with zipfile.ZipFile(org_zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipFile:
            zipFile.write(org_csv_file_path, org_csv_file_name)

        with open(org_zip_file_path, 'rb') as org_up_data:
            bucket.put_object(Key=collabo_master.code + '/' + org_zip_file_name, Body=org_up_data)
        s3.Object(Settings.get_s3_bucket(), key).delete()

        save_info = '[name] : ' + str(collabo_master.name)
        AppLog.info_save('s3_main.data_import 終了', save_info)

    except Exception as e:
        Util.put('s3_main.data_import エラー',e)
        # エラー書き込み
        import traceback
        app_log = AppLog()
        app_log.title = 's3_main.data_import エラー'
        app_log.message = traceback.format_exc()
        app_log.status = 999
        app_log.level = 3
        app_log.save_error()
