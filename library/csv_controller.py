# -*- coding: utf-8 -*-
import csv
from datetime import datetime
import zipfile
import traceback
import hashlib
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
    def save(cls, org_file_name, arr_csv_container, collaborator_master):
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
            header_row_data.append('最寄駅ID')
            header_row_data.append('店舗名')
            header_row_data.append('住所')
            header_row_data.append('店舗電話番号')
            header_row_data.append('企業名')
            header_row_data.append('仕事内容')
            header_row_data.append('メイン画像')
            header_row_data.append('サブ画像')
            header_row_data.append('コメント')
            header_row_data.append('掲載開始日')
            header_row_data.append('掲載終了日')
            header_row_data.append('急募開始日')
            header_row_data.append('急募終了日')
            header_row_data.append('特記事項')
            header_row_data.append('給与の下限金額')
            header_row_data.append('給与の上限金額')
            header_row_data.append('雇用形態')
            header_row_data.append('勤務期間')
            header_row_data.append('勤務時間')
            header_row_data.append('待遇')
            header_row_data.append('応募資格')
            header_row_data.append('職種')
            header_row_data.append('特徴')
            header_row_data.append('応募方法')
            header_row_data.append('企業情報')
            header_row_data.append('店舗担当者')
            header_row_data.append('担当Eメール')
            header_row_data.append('公開/非公開')
            header_row_data.append('遷移先URL')
            header_row_data.append('pokeCD')
            header_row_data.append('住所不定許可')
            header_row_data.append('住所変換不要')
            header_row_data.append('外部')
            csv_writer.writerow(header_row_data)

            for i, csv_container in enumerate(arr_csv_container):  # indexつきで処理
                try:
                    row_data = []
                    row_data.append(csv_container.station_identifier)
                    row_data.append('"' + Util.str_none_to_empty(csv_container.name) + '"')
                    row_data.append(Util.str_none_to_empty(csv_container.address + '\r\'))
                    row_data.append(csv_container.telephone)
                    row_data.append(Util.str_none_to_empty(csv_container.company_name))
                    row_data.append(csv_container.description)
                    row_data.append(Util.str_none_to_empty(csv_container.main_image_url))
                    row_data.append(Util.str_none_to_empty(csv_container.sub_image_url))
                    row_data.append(csv_container.comment)
                    row_data.append(csv_container.start_at.strftime('%Y/%m/%d'))
                    row_data.append(csv_container.end_at.strftime('%Y/%m/%d'))
                    if csv_container.express_start_at is not None:
                        row_data.append(csv_container.express_start_at.strftime('%Y/%m/%d'))
                    else:
                        row_data.append(None)

                    if csv_container.express_end_at is not None:
                        row_data.append(csv_container.express_end_at.strftime('%Y/%m/%d'))
                    else:
                        row_data.append(None)
                    row_data.append(csv_container.special_note)
                    row_data.append(csv_container.salary_min)
                    row_data.append(csv_container.salary_max)
                    row_data.append(csv_container.pattern)
                    row_data.append(csv_container.term_name)
                    row_data.append(csv_container.worktime)
                    row_data.append(csv_container.treatment)
                    row_data.append(csv_container.requirement)
                    row_data.append(csv_container.category_names)
                    row_data.append(csv_container.feature_names)
                    row_data.append(csv_container.application_method)
                    row_data.append(csv_container.company_info)
                    row_data.append(Util.str_none_to_empty(csv_container.contact_name))
                    row_data.append(Util.str_none_to_empty(csv_container.contact_email))
                    row_data.append(Util.bool_none_to_false(csv_container.dropped))
                    row_data.append(Util.str_none_to_empty(csv_container.entry_url))
                    row_data.append(Util.str_none_to_empty(csv_container.shop_identifier))
                    row_data.append(Util.bool_none_to_false(csv_container.allow_not_addressable))
                    row_data.append(Util.bool_none_to_false(csv_container.no_geocoding))
                    row_data.append(Util.bool_none_to_false(csv_container.outside))

                    csv_writer.writerow(row_data)

                except Exception as e:
                    Util.put('CsvController.save', e)
                    app_log = AppLog()
                    app_log.title = 'CSV保存エラー'
                    app_log.message = traceback.format_exc()
                    app_log.status = 99
                    app_log.level = 2
                    app_log.save_error()

        with zipfile.ZipFile(tmp_csv_zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipFile:
            zipFile.write(tmp_csv_file_path, tmp_csv_file_name)

        s3 = AwsResources.get_s3()
        bucket = s3.Bucket(Settings.get_s3_bucket())
        # 変換結果をバックアップの意味でUP
        with open(tmp_csv_zip_file_path, 'rb') as csv_up_data:
            bucket.put_object(
                Key=collaborator_master.code + '/' + tmp_csv_zip_file_name,
                Body=csv_up_data
            )

        return tmp_csv_file_name

    @classmethod
    def insert_web_tmp_db(cls, arr_csv_container, csv_file_name):
        u"ぽけWebのadvertisement_tmpsとcst_import_statusへ投げる"
        csv_controller = cls()
        # csv_import_statusへインサート
        csv_created_at = datetime.now()
        sql_csv_imp_sts = """
            INSERT INTO csv_import_statuses(total,state,file_name,created_at,updated_at)
            VALUES(%s, %s, %s, %s, %s)
        """
        tpl = (
            len(arr_csv_container),  # total,
            'validating',   # state,
            csv_file_name,  # file_name,
            csv_created_at,  # created_at,
            csv_created_at  # updated_at
        )
        with DBConnect.get_connection_poke_web() as con:
            with con.cursor() as cur:
                cur.execute(sql_csv_imp_sts, tpl)

        # ad_tmpへインサート
        tpl_insert_val = ()
        sql_base = ''
        for i, csv_container in enumerate(arr_csv_container):  # indexつきで処理
            sql_base += csv_controller._get_sql_base()
            tpl_insert_val += (
                i + 1,  # import_source_index
                csv_container.station_identifier,  # station_identifier
                csv_container.name,  # name
                csv_container.address,  # address
                csv_container.telephone,  # telephone
                csv_container.company_name,  # company_name
                csv_container.description,  # description
                csv_container.main_image_url,  # main_image_url
                csv_container.sub_image_url,  # sub_image_url
                csv_container.comment,  # comment
                csv_container.start_at,  # start_at
                csv_container.end_at,  # end_at
                csv_container.express_start_at,  # express_start_at
                csv_container.express_end_at,  # express_end_at
                csv_container.special_note,  # special_note
                csv_container.salary_min,  # salary_min
                csv_container.salary_max,  # salary_max
                csv_container.pattern,  # pattern
                csv_container.term_name,  # term_name
                csv_container.worktime,  # worktime
                csv_container.treatment,  # treatment
                csv_container.requirement,  # requirement
                csv_container.category_names,  # category_names
                csv_container.feature_names,  # feature_names
                csv_container.application_method,  # application_method
                csv_container.company_info,  # company_info
                csv_container.contact_name,  # contact_name
                csv_container.contact_email,  # contact_email
                csv_container.dropped,  # dropped
                csv_container.entry_url,  # entry_url
                csv_container.shop_identifier,  # shop_identifier
                csv_container.allow_not_addressable,  # allow_not_addressable
                csv_container.no_geocoding,  # no_geocoding
                csv_container.outside,  # outside
                csv_file_name,  # import_source
                csv_created_at,  # import_created_at
                datetime.now(),  # created_at
                datetime.now()  # updated_at
            )

            if i % 100 == 0 and i > 0:  # 大量だとexecuteでエラーになりそうなので、適度にクエリを発行しておく
                csv_controller._save_web_tmp_db(sql_base, tpl_insert_val)
                tpl_insert_val = ()
                sql_base = ''

        csv_controller._save_web_tmp_db(sql_base, tpl_insert_val)

    def _get_sql_base(self):
        return """
        INSERT INTO advertisement_tmps (
            import_source_index,
            station_identifier,
            name,
            address,
            telephone,
            company_name,
            description,
            main_image_url,
            sub_image_url,
            comment,
            start_at,
            end_at,
            express_start_at,
            express_end_at,
            special_note,
            salary_min,
            salary_max,
            pattern,
            term_name,
            worktime,
            treatment,
            requirement,
            category_names,
            feature_names,
            application_method,
            company_info,
            contact_name,
            contact_email,
            dropped,
            entry_url,
            shop_identifier,
            allow_not_addressable,
            no_geocoding,
            outside,
            import_source,
            import_created_at,
            created_at,
            updated_at)
        VALUES(
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s);
        """

    def _save_web_tmp_db(self, sql, tpl):
        try:
            with DBConnect.get_connection_poke_web() as con:
                with con.cursor() as cur:
                    cur.execute(sql, tpl)

        except Exception as e:
            Util.put('_save_web_tmp_db Error', e)
            app_log = AppLog()
            app_log.title = '_save_web_tmp_db エラー'
            app_log.message = traceback.format_exc() + '\r\n\r\n' + sql
            app_log.status = 99
            app_log.level = 3
            app_log.save_error()
