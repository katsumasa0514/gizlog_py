# 日報　〜gizlozをflaskで作成〜 9/27

## PDCAのplan

- 9/27 ... 新規登録機能と詳細画面、削除機能の実装
- 9/28 ... 一覧画面の実装
- 9/29 ... テスト
- 9/30 ... レビュー

### 本日のplan詳細

- 新規作成機能にて、postで送信したデータをviewで取得するところまではできていたので、データベースへの登録を行う。
- 一覧表示でデータベースから全件取得し、jinja2にて表示。
- 詳細表示でフィルターをかけたデータをデータベースから取得し、jinja2にて表示。
- 削除機能の追加で、理論削除をできるようにする。

### 9/28のplan詳細

- 削除機能の追加で、理論削除をできるようにする。（所要時間目安：2時間）
- 一覧ページの検索機能を実装する。（所要時間目安：5時間）
- テストの前に一通り確認（所要時間目安：1時間）

## PDCAのdo

基本的にplan通りに進めることができました。

削除機能まで追加したかったのですが、時間が間に合わず明日に実装いたします。

## PDCAのcheck

本日の反省点ですが、cssが読み込まれないとのことで、すぐにレビューをお願いしてしまいましたが、絶対パスと相対パスの違いでした。

簡単なことでしたが、コンソールをみるという基本的なことを怠ったことで、時間をかけてしまいました。

今まで学んだことを生かして引き続き取り組みたいと思います。

## PDCAのaction
引き続きアプリを作る中でわからない点を調べて学習しながら進める方針で取り組んでいこうと思います。

起きている事象に対して、どこにエラーが出るのかを意識することが重要だと感じました。

今後は意識した上で実装していきたいと思います。

## 参考記事

[Flask-SQLAlchemyの使い方](https://qiita.com/msrks/items/673c083ca91f000d3ed1)

[flask + python の print が docker logs で表示されない場合の対処方法](https://hawksnowlog.blogspot.com/2020/11/how-to-print-debug-messages-to-stdout-on-docker-logs.html)

[Pythonのselfはなぜ必要なのかをじっくり考察してみた](https://qiita.com/free_jinji2020/items/93a45102995648ad06f1)

[FlaskでURLマッピング（ルーティング）詳細、パラメータをURLに応じて動的に渡すから様々なHTTPメソッドを使う方法まで](https://www.nblog09.com/w/2020/11/26/flask-routing/)

[flask-SQLAlchemy で良く使うクエリーコマンド一覧](https://mycodingjp.blogspot.com/2019/07/flask-sqlalchemy.html)

[pythonのためのテンプレートエンジン「Jinja2」便利な機能](https://qiita.com/kotamatsuoka/items/a95faf6655c0e775ee22)

