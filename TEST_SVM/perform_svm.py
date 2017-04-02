import csv

from sklearn import svm
from sklearn.svm import SVC


def __svm_train__(__x__, __d_list__, __list__):
    _X_ = __x__
    _Y_ = __d_list__
    clf = svm.SVC()
    clf.fit(_X_, _Y_)
    SVC(C=100, gamma='auto', kernel='poly')

    return clf.predict([__list__])[0]


def __svm__(__symbol_name__, __interval__, __r__):
    __result_list__ = []

    open_list = []
    high_list = []
    low_list = []
    close_list = []
    prev_close_list = []
    volume_list = []
    momentum_list = []
    volatility_list = []
    day1_list = []
    day2_list = []
    day3_list = []
    day4_list = []
    day5_list = []

    __file_name__ = "F:/JAIMIN/sem_8/Stock Market Prediction/FEATURES/features/" + str(
        __interval__) + "_" + __symbol_name__ + ".csv"
    with open(__file_name__) as __csv_file__:
        _reader_ = csv.DictReader(__csv_file__)
        for row in _reader_:
            open_list.append(float(row['Open']))
            high_list.append(float(row['High']))
            low_list.append(float(row['Low']))
            close_list.append(float(row['Close Price']))
            prev_close_list.append(float(row['Prev Close Price']))
            volume_list.append(int(row['Volume']))
            momentum_list.append(float(row['Momentum of Close Price']))
            volatility_list.append(float(row['Volatility of Close Price']))

            day1_list.append(int(row['Day1']))
            day2_list.append(int(row['Day1']))
            day3_list.append(int(row['Day3']))
            day4_list.append(int(row['Day4']))
            day5_list.append(int(row['Day5']))

    del day1_list[:__r__]
    del day2_list[:__r__]
    del day3_list[:__r__]
    del day4_list[:__r__]
    del day5_list[:__r__]
    day_list = [day1_list, day2_list, day3_list, day4_list, day5_list]
    x = [list(a) for a in
         zip(volume_list, momentum_list,
             volatility_list)]
    _list_ = x[__r__ - 5]
    del x[: __r__]

    for _d_list_ in day_list:
        __result_list__.append(__svm_train__(x, _d_list_, _list_))

    return __result_list__
