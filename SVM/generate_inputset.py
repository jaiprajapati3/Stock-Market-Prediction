import csv

from SVM.get_stock import get_historical


def __generate_input__(__interval__, __symbol__):
    _list_ = []

    get_historical(__symbol__)

    _file_name_ = "temp.csv"

    date_list = []
    open_price_list = []
    high_price_list = []
    low_price_list = []
    close_price_list = []
    prev_close_list = []
    volume_list = []

    with open(_file_name_) as __csv_file__:
        reader = csv.DictReader(__csv_file__)
        for row in reader:
            date_list.append(row['Date'])
            open_price_list.append(float(row['Open']))
            high_price_list.append(float(row['High']))
            low_price_list.append(float(row['Low']))
            close_price_list.append(float(row['Close Price']))
            prev_close_list.append(float(row['Prev Close Price']))
            volume_list.append(int(row['Volume']))

    close_list = [prev_close_list, close_price_list]

    volatility_list = []

    result = 0
    for j in range(1, __interval__ + 1):
        result = result + (close_list[0][j] - close_list[1][j]) / close_list[1][j]
    volatility = result / __interval__
    volatility_list.append(volatility)

    flag_list = []
    for k in range(0, len(date_list)):
        temp = close_list[1][k] - close_list[0][k]
        if temp < 0:
            flag_list.append(-1)
        else:
            flag_list.append(1)

    momentum_list = []

    result = 0
    for j in range(1, __interval__ + 1):
        result = result + flag_list[j]
    momentum_list.append(result / __interval__)

    # _list_.append(open_price_list[0])
    # _list_.append(high_price_list[0])
    # _list_.append(low_price_list[0])
    _list_.append(close_price_list[0])
    # _list_.append(prev_close_list[0])
    # _list_.append(volume_list[0])
    _list_.append(momentum_list[0])
    _list_.append(volatility_list[0])

    return _list_
