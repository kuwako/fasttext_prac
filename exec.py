# coding:utf-8

import gensim
import time
import MeCab

start = time.time()
mecab = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
mecabSub = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

text = 'むかしむかし、あるところに、おじいさんとおばあさんが住んでいました。おじいさんは山へ芝刈りに、おばあさんは川へ洗濯に行きました。おばあさんが川で洗濯をしていると、ドンブラコ、ドンブラコと、大きな桃が流れてきました。'

# text = '吾輩は猫である。名前はまだ無い。どこで生れたかとんと見当がつかぬ。何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。吾輩はここで始めて人間というものを見た。しかもあとで聞くとそれは書生という人間中で一番獰悪な種族であったそうだ。この書生というのは時々我々を捕つかまえて煮にて食うという話である。'

model = gensim.models.KeyedVectors.load_word2vec_format('model.vec', binary=False)
mecab.parse('')#文字列がGCされるのを防ぐ
node = mecab.parseToNode(text)
strCat = ''
exceptionIndex = 0

# 弾かない文法リスト
whiteList = [
    '副詞可能',
    '一般',
    '自立',
    '固有名詞',
    '形容動詞語幹'
]

elapsed_time = time.time() - start
print(("elapsed_time:{0}".format(elapsed_time)) + "[sec]")

print('loop start')
while node:
    print('.')
    #単語を取得
    word = node.surface
    #品詞を取得
    feature = node.feature.split(",")

    # featureの種類によって変換の実行、非実行を管理
    if feature[1] in whiteList:
        # 弾かない文法なら、word2vecで判定する
        try:
            # similarの中身は(’単語’, 類似率) ex: ('夏目漱石', 0.6646738052368164)
            similarList = model.most_similar(positive=[word], topn=10)
            for similar in similarList:
                similarFeatures = mecabSub.parse(similar[0]).split("\t")
                if similarFeatures[1:]:
                    similarFeatures = similarFeatures[1].split(",")
                if feature[0] == similarFeatures[0] \
                and feature[1] == similarFeatures[1] \
                and feature[4] == similarFeatures[4] \
                and feature[5] == similarFeatures[5]:
                    word = similar[0]
                    break
        except:
            exceptionIndex += 1
            print(str(exceptionIndex))

    strCat += word
    #次の単語に進める
    node = node.next
# print(model.most_similar(positive=['麻婆豆腐'], topn=1))

print(strCat)
print(str(exceptionIndex) + ' times exceptions occured.')
elapsed_time = time.time() - start
print(("elapsed_time:{0}".format(elapsed_time)) + "[sec]")

# 桃太郎の変換後
# むかしむかし、あるところに、おばあさんとばあさんが移り住んでいました。おばあさんは麓へダート刈りに、ばあさんは支流へ洗濯に行きました。ばあさんが支流で洗濯をしていると、ドンブラコ、ドンブラコと、大きな梨が流れてきました。

# 我輩は猫であるの返還後
# 夏目漱石。名はまだない。どこで産まれたかとんと見当が付かぬ。何でも暗いじめじめしない所でニャーニャー泣いていたことだけは記憶している。吾輩はここで続けて生き物というものをみた。しかも最後で聴くとそれは良家という生き物中でいちばん獰悪な地球人であったそうだ。この良家というのはたまに我々を掠追いかけて茹でにて食らうという話である。

# 日本人: [('韓国人', 0.7338133454322815), ('中国人', 0.717720627784729), ('アメリカ人', 0.6725355982780457), ('日本人女性', 0.6723321676254272), ('外国人', 0.6420464515686035), ('フィリピン人', 0.6264426708221436), ('欧米人', 0.621786892414093), ('アジア人', 0.6192302703857422), ('台湾人', 0.6034690141677856), ('日系人', 0.5906497240066528)]
# [('ポケモンXY', 0.8050551414489746), ('ポケモンXD', 0.7923538684844971), ('ポケモントレーナー', 0.7631847262382507), ('ピカチュウ', 0.7623766660690308), ('ポケモン図鑑', 0.75491863489151), ('ポケットモンスター', 0.7538669109344482), ('ポケモンキッズ', 0.7482787370681763), ('ポケモンBW', 0.7361546754837036), ('サトシのポケモン', 0.7307371497154236), ('ポケモンファン', 0.7289283871650696)]
# japaneseもtennisもなぜか判定なし
# model.most_similar(positive=['tennis'])
# model.most_similar(positive=['japanese'])
