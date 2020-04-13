from keras import models, layers

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

