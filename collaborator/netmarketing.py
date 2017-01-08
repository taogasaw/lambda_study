# -*- coding: utf-8 -*-
import csv
import sys

from library.csv_container import CsvContainer
from library.app_log import AppLog


def data_import(csv_path):
    reload(sys)
    sys.setdefaultencoding("utf-8")

    AppLog.save('変換開始', csv_path)

    with open(csv_path) as f:
        reader = csv.reader(f)
        next(reader)  # ヘッダーを読み飛ばす場合

        arr_csv_cnt = []
        # 一行ずつ処理
        for i, row in enumerate(reader):  # indexつきで処理
            # index = i + 1
            # CSVフォーマットのクラスへ保持する
            csv_cnt = CsvContainer()
            csv_cnt.name = 'test_name_' + str(i)
            csv_cnt.telephone = 'test_tel_' + str(i)
            # …ホントは続く

            arr_csv_cnt.append(csv_cnt)

    return arr_csv_cnt
