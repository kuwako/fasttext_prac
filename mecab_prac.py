import MeCab

mecab = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

text = 'むかしむかし、あるところに、おじいさんとおばあさんが住んでいました。おじいさんは山へしばかりに、おばあさんは川へせんたくに行きました。おばあさんが川でせんたくをしていると、ドンブラコ、ドンブラコと、大きな桃が流れてきました。'

# text = '滲み出す混濁の紋章 不遜なる狂気の器 湧き上がり・否定し・痺れ・瞬き 眠りを妨げる 爬行する鉄の王女 絶えず自壊する泥の人形 結合せよ 反発せよ 地に満ち己の無力を知れ 破道の九十 「黒棺」'

mecab.parse('')#文字列がGCされるのを防ぐ
node = mecab.parseToNode(text)
while node:
    #単語を取得
    word = node.surface
    #品詞を取得
    pos = node.feature.split(",")[1]
    print('{0} , {1}'.format(word, pos))
    #次の単語に進める
    node = node.next
