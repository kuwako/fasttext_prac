# coding:utf-8

import gensim

model = gensim.models.KeyedVectors.load_word2vec_format('model.vec', binary=False)

print(model.most_similar(positive=['リンゴ']))

# japaneseもtennisもなぜか判定なし
# model.most_similar(positive=['tennis'])
# model.most_similar(positive=['japanese'])
