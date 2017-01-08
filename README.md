# 主旨
部内でAWS lambda(python)を使うための勉強会資料です。  
既存サービス環境/メンバーを前提にするので、やや偏り気味の内容になります。  
基本環境はMac(他の環境なら適宜読み替え)だとして進行します。

## 事前準備・参加要件
1. 5〜6回、各1.5〜2時間程度参加する時間の確保
1. ノートPC、それぞれAdmin/root/sudo権限が使えるネットワークに繋がる端末
1. 使用するプラットフォームに、python2.7系/pyenv/pyenv-virtualenvまたはvirtualenv/pipをインストールしておく  
本当はここもやりたいけど、環境によってインストールの手間がだいぶ違いそうなので、事前準備とします  
ググってインストールしといてください (^v^;)
1. お気に入りのエディタ、できればpythonサポート機能を入れておく
1. postgresとgit、それを自由にいじれる権限
1. プライベートAWSアカウント、管理者権限

## 勉強会概要
1. 環境設定  
  * pyenvとpyenv-virtualenvの使い方
  * AWS lambdaの基本的な使い方と、今回の開発概要の理解
  * psycopg2とlambda-packagesのインストール
1. 開発1_基本構成の設定
  * libraryディレクトリ以下のpyファイル作成
  * lambda_function.pyの作成
  * s3_main.pyの作成
1. 開発2_主要機能の実装  
  * s3からCSVのDL、解析
  * オリジナルと変更後のCSVをs3へUP
  * DBへ保存
1. 開発3_AWS環境設定とデプロイ  
  * AWSにlambda/DBの環境構築
  * zip_for_deploy.pyの開発
  * デプロイして挙動確認
