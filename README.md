### macへのmecabの導入方法
- Python3からMeCabを使う http://qiita.com/taroc/items/b9afd914432da08dafc8
    - pip → pip3にする

### 学習済みモデル
- 以下のqiitaから感謝しながら利用しました
    - http://qiita.com/Hironsan/items/513b9f93752ecee9e670
- word2vecの学習済み日本語モデルを公開します | カメリオ開発者ブログ
    - http://aial.shiroyagi.co.jp/2017/02/japanese-word2vec-model-builder/
- pixiv小説で機械学習したらどうなるのっと【学習済みモデルデータ配布あり】 - pixiv inside
    - http://inside.pixiv.net/entry/2016/09/13/161454

### mecab-python
- リファレンス的なもの
    - https://taku910.github.io/mecab/bindings.html

### doc2vec
- word2vecより文脈理解が優秀らしい
    - 学習済みデータと利用法
        - https://github.com/pixiv/pixivnovel2vec/releases

### 実行方法
- python3 exec.py
    - python exec.pyだとmac標準のpython2.6系が使われ、日本語がうまく扱えない
