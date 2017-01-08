# -*- coding: utf-8 -*-
import csv
import zipfile
import traceback
import sys

from library.util import Util
from library.app_log import AppLog
from library.settings import Settings
from library.db_connect import DBConnect
import library.aws_resource as AwsResources


class CsvController(object):

    reload(sys)
    sys.setdefaultencoding("utf-8")

    @classmethod
    def save(cls, org_file_name, arr_csv_container, str_collaborator):
        u"csv_containerの配列をもらって、ファイルに保存、S3にUP、そのパスを返す"
        tmp_csv_file_name = org_file_name.replace('_org.', '.')
        tmp_csv_zip_file_name = tmp_csv_file_name.replace('.csv', '.zip')
        tmp_csv_file_path = '/tmp/' + tmp_csv_file_name
        tmp_csv_zip_file_path = tmp_csv_file_path.replace('.csv', '.zip')

        with open(tmp_csv_file_path, 'ab') as f:  # aでファイルが無ければ作る
            # 改行やカンマ、コーテーションなどのCSVフォーマットを崩す文字列がある場合だけ、ダブルコーテーションでくくられる
            csv_writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
            # ヘッダーを書く
            header_row_data = []
            header_row_data.append('店舗名')
            header_row_data.append('店舗電話番号')
            csv_writer.writerow(header_row_data)

            for i, csv_container in enumerate(arr_csv_container):  # indexつきで処理
                try:
                    row_data = []
                    row_data.append(Util.str_none_to_empty(csv_container.name))
                    row_data.append(csv_container.telephone)
                    csv_writer.writerow(row_data)

                except:
                    AppLog.save('CsvController.save', traceback.format_exc())

        with zipfile.ZipFile(tmp_csv_zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipFile:
            zipFile.write(tmp_csv_file_path, tmp_csv_file_name)

        s3 = AwsResources.get_s3()
        bucket = s3.Bucket(Settings.get_s3_bucket())
        # 変換結果をバックアップの意味でUP
        with open(tmp_csv_zip_file_path, 'rb') as csv_up_data:
            bucket.put_object(
                Key=str_collaborator + '/' + tmp_csv_zip_file_name,
                Body=csv_up_data
            )

        return tmp_csv_file_name

    @classmethod
    def insert_web_tmp_db(cls, arr_csv_container, csv_file_name):
        u"ぽけWebのadvertisement_tmpsへ投げる"
        csv_controller = cls()

        # ad_tmpへインサート
        tpl_insert_val = ()
        sql_base = ''
        for i, csv_container in enumerate(arr_csv_container):  # indexつきで処理
            sql_base += csv_controller._get_sql_base()
            tpl_insert_val += (
                i + 1,  # import_source_index
                csv_container.name,  # name
                csv_container.telephone  # telephone
            )

            if i % 100 == 0 and i > 0:  # 大量だとexecuteでエラーになりそうなので、適度にクエリを発行しておく
                csv_controller._save_web_tmp_db(sql_base, tpl_insert_val)
                tpl_insert_val = ()
                sql_base = ''

        csv_controller._save_web_tmp_db(sql_base, tpl_insert_val)

    def _get_sql_base(self):
        return """
        INSERT INTO advertisement_tmps (import_source_index, name, telephone)
        VALUES(%s,%s,%s);
        """

    def _save_web_tmp_db(self, sql, tpl):
        try:
            with DBConnect.get_connection() as con:
                with con.cursor() as cur:
                    cur.execute(sql, tpl)

        except:
            AppLog.save('_save_web_tmp_db エラー', traceback.format_exc() + '\r\n\r\n' + sql)
