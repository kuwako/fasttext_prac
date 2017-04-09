# coding:utf-8

import gensim

model = gensim.models.KeyedVectors.load_word2vec_format('model.vec', binary=False)

model.most_similar(positive=['tennis'])
# japaneseはなぜか判定なし
# model.most_similar(positive=['japanese'])
