import csv
import datetime
import os

from SVM.perform_svm import __svm__

if __name__ == '__main__':

    _symbol_list_ = []
    _price_list_ = []

    __interval__ = 270
    symbol_list = ["AAPL", "INTC", "FB", "TSLA", "NKE", "YHOO", "AMZN", "TCS", "MSFT"]

    for __symbol_name__ in symbol_list:
        print("Process " + __symbol_name__ + "...")
        __list__ = []
        __list__ = __svm__(__symbol_name__, __interval__)
        print(__symbol_name__)
        _symbol_list_.append(__symbol_name__)
        print(__interval__)
        print(__list__)
        _price_list_.append(__list__)
        print("Complete " + __symbol_name__ + ".")

    __log_file__ = "Log/" + str(datetime.date.today()) + "_log.csv"
    with open(__log_file__, 'w') as __csv_file_Write__:
        fieldnames = ['Symbol', 'Price Prediction']
        writer = csv.DictWriter(__csv_file_Write__, fieldnames=fieldnames)
        writer.writeheader()
        count = 0
        for i in range(0, len(_price_list_)):
            writer.writerow(
                {
                    'Symbol': _symbol_list_[i],
                    'Price Prediction': _price_list_[i]
                }
            )
os.remove("temp.csv")
