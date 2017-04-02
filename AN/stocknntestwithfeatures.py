import csv
import os

import numpy as np
from click._compat import raw_input

np.random.seed(1337)
from keras.models import Sequential
from keras.layers import Dense


# from textblob import TextBlob
# from IPython.display import SVG

# theano.config.device = 'gpu'
# theano.config.floatX = 'float32'



def stock_prediction():
    print("File ::: ")
    FILE_NAME = "tempdataset/temp.csv"
    print("into stock prediction")
    # dataset = []
    # with open(FILE_NAME) as f:
    #     for n, line in enumerate(f):
    #         if n != 0:
    #             dataset.append(float(line.split(',')[4]))
    #
    # dataset = np.array(dataset)
    # print len(dataset)
    # print dataset
    #
    # def create_dataset(dataset):
    #     dataX = [dataset[n + 1] for n in range(len(dataset) - 2)]
    #
    #     return np.array(dataX), dataset[2:]
    dataset = np.loadtxt(FILE_NAME, delimiter=',')
    print(len(dataset))

    trainX = dataset[:, 0:4]
    print(len(trainX))
    trainY = dataset[:, 3]
    print(trainX)
    print(trainY)
    model = Sequential()
    model.add(Dense(20, input_dim=4, init='uniform', activation='relu'))
    # model.add(normalization.BatchNormalization())
    model.add(Dense(40))
    # model.add(normalization.BatchNormalization())
    model.add(Dense(40))
    # model.add(normalization.BatchNormalization())
    model.add(Dense(20))
    # model.add(normalization.BatchNormalization())
    # model.add(Dense(16))
    #
    # model.add(Dense(16))
    model.add(Dense(1, activation='relu'))
    # model.add(normalization.BatchNormalization())
    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
    model.summary()
    model.fit(trainX, trainY, nb_epoch=200, batch_size=128, verbose=2)
    # model.add(LSTM(input_dim=1, output_dim=50,return_sequences=True))
    # model.add(Dropout(0.2))
    # model.add(LSTM(100,return_sequences=False))
    # model.add(Dense(1))
    # model.add(Activation('relu'))
    # model.compile(loss='mean_squared_error', optimizer='rmsprop')
    # model.fit(trainX, trainY, nb_epoch=200, batch_size=512, verbose=2,validation_split=0.05)

    prediction = model.predict(trainX)
    evaluation = model.evaluate(trainX, trainY)
    model.save('model.hdf5')
    # model.summary()
    print("Evaluation ::: ")
    print(evaluation)
    print("Accuracy ::: ")
    print(evaluation * 100)
    print(len(prediction))
    print(prediction)
    dataset = np.append(dataset, [prediction[0][0]])
    print(dataset)
    # dataset.append(prediction[0][0].astype(float))

    # SVG(model_to_dot(model).create(prog='dot', format='svg'))
    # plot(model, to_file='model.png')
    os.remove("tempdataset/temp.csv")
    return prediction[0][0].astype(float)


def evaluate(file):
    print("into evaluate")
    remove_header_and_date(file)

    print(stock_prediction())
    # for i in range(7):
    #     price = stock_prediction()
    #     close_list.append(price)
    # print close_list


def remove_header_and_date(filename):
    with open(filename, "rb") as readFile:
        csvReader = csv.reader(readFile)
        next(csvReader)
        with open("tempdataset/temp.csv", "wb") as writeFile:
            csvWrite = csv.writer(writeFile)
            flag = False
            for row in csvReader:
                del row[0]

                #	if flag==False:
                #		next(csvReader)
                #		flag=True

                csvWrite.writerow(row)


if __name__ == "__main__":
    file = (raw_input("Enter File Name").upper())
    evaluate(file)
