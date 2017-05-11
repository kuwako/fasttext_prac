import MeCab

mecab = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
mecabSub = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

# text = 'むかしむかし、あるところに、おじいさんとおばあさんが住んでいました。おじいさんは山へしばかりに、おばあさんは川へせんたくに行きました。おばあさんが川でせんたくをしていると、ドンブラコ、ドンブラコと、大きな桃が流れてきました。'
text = '吾輩は猫である。名前はまだ無い。どこで生れたかとんと見当がつかぬ。何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。吾輩はここで始めて人間というものを見た。しかもあとで聞くとそれは書生という人間中で一番獰悪な種族であったそうだ。この書生というのは時々我々を捕つかまえて煮にて食うという話である。'

# text = '滲み出す混濁の紋章 不遜なる狂気の器 湧き上がり・否定し・痺れ・瞬き 眠りを妨げる 爬行する鉄の王女 絶えず自壊する泥の人形 結合せよ 反発せよ 地に満ち己の無力を知れ 破道の九十 「黒棺」'

mecab.parse('')#文字列がGCされるのを防ぐ
node = mecab.parseToNode(text)
while node:
    #単語を取得
    word = node.surface
    #品詞を取得
    # pos = node.feature.split(",")
    pos = mecabSub.parseToNode(word).feature.split(",")
    hinshi = mecabSub.parse(word).split("\t")
    if hinshi[1:]:
        hinshiList = hinshi[1].split(",")
        print(node.feature.split(","))
        print(hinshiList)
        print("")

    #次の単語に進める
    node = node.next
