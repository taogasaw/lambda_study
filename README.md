# 主旨
部内でAWS lambda(python)を使うための勉強会資料です。  
既存サービス環境/メンバーを前提にするので、やや偏り気味の内容になります。  
基本は部内のMac使い(他の環境なら適宜読み替え)としてハンズオンを想定していますが、  
なれていないと辛いので、実際のlambdaの挙動/開発フローを見たい、というスタンスでもOKです。

## 事前準備・参加要件
1. 6回程度(?)、各1.5〜2時間程度参加する時間の確保
1. 以前シェアしたpython入門の範囲のおおよその理解(本会は文法には深く触れません)
1. ノートPC、それぞれAdmin/root/sudo権限が使えてネットワークに繋がる端末
1. 使用するプラットフォームに、python2.7系(できればpyenvやpyenv-virtualenvまたはvirtualenvも)とpipが入っている
1. お気に入りのエディタ、できればpythonサポート機能を入れておく
1. postgresとgit、それを自由にいじれる権限
1. プライベートAWSアカウント、管理者権限

## 勉強会概要
1. 環境設定  
  * AWS lambdaの基本的な使い方と、今回の開発概要の理解
  * (補足)pyenvとpyenv-virtualenvの使い方
  * psycopg2とlambda-packagesのインストール
  * 開発環境にDB作成、S3にバケット用意、.bash_profileにAWS keyの指定
1. 開発1_基本構成の設定
  * library以下のdb_connect・settings・utilの開発
  * lambda_function.pyの作成
1. 開発2_主要機能(s3_main)の実装  
  * s3からCSVのDL、解析(collaboratorの開発)
  * オリジナルと変更後のCSVをs3へUP(csv_controllerの開発1)
  * DBへ保存(csv_controllerの開発2)
1. 開発3_AWS環境設定とデプロイ  
  * AWSにlambda/DBの環境構築
  * zip_for_deploy.pyの開発
  * デプロイして挙動確認
