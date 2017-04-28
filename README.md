### macへのmecabの導入方法
- Python3からMeCabを使う http://qiita.com/taroc/items/b9afd914432da08dafc8
    - pip → pip3にする

### 学習済みモデル
- 以下のqiitaから感謝しながら利用しました
    - http://qiita.com/Hironsan/items/513b9f93752ecee9e670

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
    
### 進捗
変換時の判定にmecabを使う箇所で難航中
