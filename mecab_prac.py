import MeCab

mecab = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

text = 'むかしむかし、あるところに、おじいさんとおばあさんが住んでいました。おじいさんは山へしばかりに、おばあさんは川へせんたくに行きました。おばあさんが川でせんたくをしていると、ドンブラコ、ドンブラコと、大きな桃が流れてきました。'
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
