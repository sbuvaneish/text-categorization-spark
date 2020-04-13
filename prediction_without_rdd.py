import os
import json
import keras
import pickle
import numpy as np
from collections import OrderedDict
from keras.models import model_from_json

import dense_model

DATA_DIR = 'data'
INPUT_DIR = 'data/input'
TOKENIZER_FILE = 'tokenizer.pickle'
MODEL_WEIGHTS = 'dense_model_weights.h5'
LABEL_ENCODING = 'label_encoding.json'

with open('/'.join([DATA_DIR, TOKENIZER_FILE]), 'rb') as handle:
    tokenizer = pickle.load(handle)

text_list = OrderedDict()

for file in os.listdir(INPUT_DIR):
	with open('/'.join([INPUT_DIR, file]), 'r') as f:
		text_list[file] = f.read().lower()

features = tokenizer.texts_to_matrix(list(text_list.values()))

vocab_size = len(tokenizer.word_index) + 1

model = dense_model.create_dense_model(vocab_size=vocab_size)
model.load_weights('/'.join([DATA_DIR, MODEL_WEIGHTS]))

predictions = np.argmax(model.predict(features), axis=1)

with open(LABEL_ENCODING, 'r') as f:
	label_codes = json.load(f)
label_codes = {int(key): value for key, value in label_codes.items()}

results = {}

for file, prediction in zip(text_list, predictions):
	results[file] = label_codes.get(prediction, 0)

print(results)

