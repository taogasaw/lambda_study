# -*- coding: utf-8 -*-
import zipfile
import os
import re

os.rename("./_for_lambda_psycopg2", "./psycopg2")

dir_path = '.'
zip_name = 'lambda_deploy.zip'

if os.path.exists(zip_name):
    os.remove(zip_name)

with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zip_file:
    for dir_path, dirnames, filenames in os.walk(dir_path):
        # ディレクトリに中にファイルがなかった場合
        if not filenames:
            zip_file.write(dir_path + "/")
        for filename in filenames:
            filepath = os.path.join(dir_path, filename)

            # 必要なsourceだけzip内に書き込む
            if dir_path in ['db']:
                continue
            if re.match(r'.+\.csv', filename) is not None:
                continue

            zip_file.write(filepath)

os.rename("./psycopg2", "./_for_lambda_psycopg2")
