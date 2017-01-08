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
        # 余計なディレクトリはスキップ
        if re.match(r'^\./db.*|^\./\.git.*', dir_path) is not None:
            continue

        # ディレクトリに中にファイルがなかった場合も一応入れる
        if not filenames:
            zip_file.write(dir_path + "/")

        for filename in filenames:
            # 余計なファイルはスキップ
            if re.match(r'.+\.csv|.+\.zip|^\..+|.+\.md', filename) is not None:
                continue
            filepath = os.path.join(dir_path, filename)
            zip_file.write(filepath)

os.rename("./psycopg2", "./_for_lambda_psycopg2")
