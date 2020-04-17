from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark import SparkConf
from keras import models, layers
import boto3
import os
import sys
import pickle
import json
import tempfile
import numpy as np


spark = SparkSession.builder.appName('TextCategorization').getOrCreate()
sc = spark.sparkContext

BUCKET = 'sbh-cloudproject3'
s3 = boto3.resource('s3')
bucket = s3.Bucket(BUCKET)
s3.meta.client.head_bucket(Bucket=BUCKET)

request_id = sys.argv[1]
search_string = 'input/{request_id}'.format(request_id=request_id)

key_text_list = []

for pair in bucket.objects.all():
    obj = s3.Object(BUCKET, pair.key)
    if pair.key.endswith('.txt') and search_string in pair.key:
        content = obj.get()['Body'].read()
        key_text_list.append((pair.key, content.decode('utf-8').lower()))
    elif pair.key.endswith('.pickle'):
        content = obj.get()['Body'].read()
        tokenizer = pickle.loads(content)
    elif pair.key.endswith('.h5'):
        model_weights_key = pair.key
    elif pair.key.endswith('.json'):
        label_encoding_key = pair.key



def create_dense_model(vocab_size, max_words=5000, num_classes=5, drop_ratio=0.4):
	model = models.Sequential()
	model.add(layers.Embedding(vocab_size, 32, input_length=max_words))
	model.add(layers.Flatten())
	model.add(layers.Dense(512, input_shape=(5000 * 32,)))
	model.add(layers.Activation('relu'))
	model.add(layers.Dropout(drop_ratio))
	model.add(layers.Dense(num_classes))
	model.add(layers.Activation('softmax'))

	model.compile(loss='categorical_crossentropy',
								optimizer='adam',
								metrics=['accuracy'])

	return model




vocab_size = len(tokenizer.word_index) + 1
model = create_dense_model(vocab_size=vocab_size)
model.summary()


weights_object = s3.Object(BUCKET, model_weights_key)
weights_content = weights_object.get()['Body'].read()
fp = tempfile.NamedTemporaryFile()
fp.write(weights_content)
model.load_weights(fp.name)


text_list = [text for (key, text) in key_text_list]
features = tokenizer.texts_to_matrix(text_list)

if len(features) > 0:
	predictions = np.argmax(model.predict(features), axis=1)
else:
	predictions = []

label_codes = json.loads(s3.Object(BUCKET, label_encoding_key).get()['Body'].read().decode('utf-8'))
label_codes = {int(key): value for key, value in label_codes.items()}


results = {key: label_codes.get(prediction, "") for (key, text), prediction in zip(key_text_list, predictions)}
print(results)


exit()
