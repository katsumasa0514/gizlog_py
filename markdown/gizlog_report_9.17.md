# 日報　〜gizlozをflaskで作成〜 9/17

### 作業内容

- dockerで仮想環境を立ち上げ、その際に同時にpython環境を構築できるようファイルを編集。
- flaskでのマイグレーション方法の学習。
- プロジェクト先の学習資料の学習とスプレットシートへのまとめ。

### 学んだこと

- dockerfileをbuildする際にキャッシュが残っていたようで、ビルドに「--no-cache」をつけることでキャッシュを消すことができること学びました。

### まとめ

本日はdockerで仮想環境を立ち上げ、その際に同時にpython環境を構築できるように作業を行っていましたが、エラーをあまり解決できず、阿部さんにレビューしていただいて解決できました。しかし、「pipenv install」をビルドの際に行っても反映されないので、ビルド後にこのコマンドのだけ打たないといけない状況です。日数がなくなってきましたので、明日はマイグレーションに入っていきたいと思います。

### 参考記事

[Flask + SQLAlchemyプロジェクトを始める手順](https://qiita.com/shirakiya/items/0114d51e9c189658002e#%E3%82%A2%E3%83%97%E3%83%AA%E5%88%9D%E6%9C%9F%E6%A7%8B%E7%AF%89)

[Pipenvを使ったPython開発まとめ](https://qiita.com/y-tsutsu/items/54c10e0b2c6b565c887a)

[Pipenv と Docker を使った開発環境のベストプラクティス](https://qiita.com/kawasin73/items/3e58fc8a14af66ab7204)

### スプレットシート

[スプレットシート](https://docs.google.com/spreadsheets/d/1RBv3eIIbe45y8auqOI7i8l35aVuW3bUBWOc7x60rUpw/edit#gid=0)