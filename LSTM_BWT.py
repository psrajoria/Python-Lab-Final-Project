from numpy import array
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.utils import pad_sequences
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding


# source text
data = "BNIUMP$"
# prepare the tokenizer on the source text
tokenizer = Tokenizer(char_level=True)
tokenizer.fit_on_texts(list(data))
# determine the vocabulary size
print(tokenizer.word_index)
vocab_size = len(tokenizer.word_index) + 1
print('Vocabulary Size: %d' % vocab_size)
# create line-based sequences
encoded = tokenizer.texts_to_sequences(data)
# encoded = tokenizer.texts_to_sequences(data)
sequences = []
for i in range(len(encoded) - 1, -1, -1):
        encoded.insert(0, encoded.pop())
        temp = list(encoded)
        sequences.append(temp)
print(sequences)
# print('Total Sequences: %d' % len(sequences))
# # pad input sequences
max_length = max([len(seq) for seq in sequences])
sequences = pad_sequences(sequences, maxlen=max_length, padding='pre')
print('Max Sequence Length: %d' % max_length)
# split into input and output elements
sequences = array(sequences)
print(sequences.shape)
X, y = sequences[:, :-1], sequences[:, -1]
print(X.shape)
# print(X)
y = to_categorical(y, num_classes=vocab_size)
print(y.shape)
# define model
model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=max_length-1))
model.add(LSTM(50))
model.add(Dense(vocab_size, activation='softmax'))
print(model.summary())
# compile network
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit network
model.fit(X, y, epochs=100, verbose=2)

model.save('my_model.h5')
