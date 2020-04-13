import os
import numpy as np
import pandas as pd
import nltk.tokenize
import keras
import keras.models
from keras import layers
from keras.preprocessing.sequence import pad_sequences
from keras.layers import concatenate, Input, Dense, GlobalAveragePooling1D, Embedding, Dropout

DATA_DIR = 'data'
INPUT_DIR = 'data/input'
DATA_FILE = 'bbc-text.csv'
VOCAB_FILE = 'vocab.npy'
MODEL_PATH = 'data/ensemble_model.h5'
ARTICLE_COUNT = 10
MAX_SEQUENCE_LENGTH = 200

# articles = pd.read_csv('/'.join([DATA_DIR, DATA_FILE])).head(ARTICLE_COUNT)['text'].values.tolist()
#
# for article, index in zip(articles, range(1, ARTICLE_COUNT+1)):
# 	with open('/'.join([INPUT_DIR, f'article_{index}.txt']), 'w') as f:
# 		f.write(article)

vocabulary = np.load('/'.join([DATA_DIR, VOCAB_FILE]), allow_pickle=True).item()

features_list = []

for file in os.listdir(INPUT_DIR):
	with open('/'.join([INPUT_DIR, file]), 'r') as f:
		text = f.read()
	text = text.lower()
	word_list = nltk.tokenize.word_tokenize(text)
	feature = [vocabulary[word] if word in vocabulary else 0 for word in word_list]
	features_list.append(feature)

padded_features = pad_sequences(features_list, maxlen=MAX_SEQUENCE_LENGTH)

modelEns = keras.models.load_model(MODEL_PATH)





