# -*- coding: utf-8 -*-
import csv
from datetime import datetime
import sys

from library.csv_container import CsvContainer
from library.app_log import AppLog


def data_import(csv_path, collabo_master):

    AppLog.info_save(collabo_master.name + ' 保存開始', csv_path)
    reload(sys)
    sys.setdefaultencoding("utf-8")

    with open(csv_path) as f:
        reader = csv.reader(f)
        next(reader)  # ヘッダーを読み飛ばす場合

        arr_csv_cnt = []
        # 一行ずつ処理
        for i, row in enumerate(reader):  # indexつきで処理
            # index = i + 1
            # CSVフォーマットのレコードクラスを用意
            csv_cnt = CsvContainer()
            csv_cnt.name = 'test_' + str(i)
            csv_cnt.description = row[0]
            csv_cnt.comment = row[1]
            csv_cnt.start_at = datetime.strptime('2016/1/1', '%Y/%m/%d')
            csv_cnt.end_at = datetime.strptime('2020/1/1', '%Y/%m/%d')

            # csv_cnt.station_identifier = row[*]
            # csv_cnt.name = row[*]
            # …ホントは続く

            arr_csv_cnt.append(csv_cnt)

    return arr_csv_cnt
