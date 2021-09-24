# 日報　〜gizlozをflaskで作成〜 9/24

## PDCAのplan

- 9/24 ... 新規登録機能の実装
- 9/27 ... 詳細画面と削除機能の実装
- 9/28 ... 一覧画面の実装
- 9/29 ... テスト
- 9/30 ... レビュー

### 本日のplan詳細

- 画面部分を表示できるようtemplate部分とルートを設定
- データのやりとりができるようmodel部分を記述
- view部分を記述

### 9/27のplan詳細

引き続き新規登録機能の実装を行いたいと思います。

## PDCAのdo

◯本日は新規作成機能に取り組みました。

◯新規作成ページを表示できるようにtemplate部分を作成しルートの処理を行いました。

◯送られたformデータをviewで受け取りデータを保存する処理の記述を行いました。

## PDCAのcheck

基本的にプラン通りに作業を進めることができました。

昨日の反省点を生かし、確認を行いながら作業を進めることで、タイムロスを削減できました。

しかし、確認をするため「print」を行ったのですが、docker desktopに表示されず詰まってしまいました。

調べると「flush=True」でコンテナ内のログでprintを確認できるようになりました。

## PDCAのaction
引き続きアプリを作る中でわからない点を調べて学習しながら進める方針で取り組んでいこうと思います。

本日の反省点に関しましては特に見当たらないので、引き続き進めていきたいと思います。

## 参考記事

[Flask-SQLAlchemyの使い方](https://qiita.com/msrks/items/673c083ca91f000d3ed1)

[flask + python の print が docker logs で表示されない場合の対処方法](https://hawksnowlog.blogspot.com/2020/11/how-to-print-debug-messages-to-stdout-on-docker-logs.html)

[ターミナルを使ったFlaskの常時実行と停止方法](https://kita-note.com/flask-always-run-and-stop)
