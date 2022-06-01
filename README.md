# なろう類似作品検索サイト
小説家になろうのapiを用いて小説データを取得し、あらすじをDoc2Vecを用いてベクトル化を行い、そのモデルを用いて類似検索を行うサイトです。

## Development

```plain
fastapi
vue3
Mysql
nginx
```

## Production

* ないもの
以下のファイルは容量の関係でgithubには上げていません
```plain
backend/doc2vec/配下のモデルファイル
db/data/配下のデータファイル
```
モデルデータ及びなろうapiからデータ取得はappコンテナで実行


* サイトの場所

http://xhayamix.com
