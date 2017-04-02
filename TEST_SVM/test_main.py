import csv
import os

from TEST_SVM.perform_svm import __svm__

if __name__ == '__main__':

    _symbol_list_ = []
    _price_list_ = []

    __interval__ = 5
    symbol_list = ["AAPL", "GOOGL", "INTC", "FB", "TSLA", "NFLX", "YHOO", "AMZN", "MSFT"]
    __r__ = int(input("Enter r : "))
    for __symbol_name__ in symbol_list:
        print("Process " + __symbol_name__ + "...")
        __list__ = []
        __list__ = __svm__(__symbol_name__, __interval__, __r__)
        print(__symbol_name__)
        _symbol_list_.append(__symbol_name__)
        print(__interval__)
        print(__list__)
        _price_list_.append(__list__)
        print("Complete " + __symbol_name__ + ".")

    __date__ = input("Enter Date ( 2017-04-04 ): ")

    __log_file__ = "Log/" + __date__ + "_log.csv"
    with open(__log_file__, 'w') as __csv_file_Write__:
        fieldnames = ['Symbol', 'Day1', 'Day2', 'Day3', 'Day4', 'Day5']
        writer = csv.DictWriter(__csv_file_Write__, fieldnames=fieldnames)
        writer.writeheader()
        count = 0
        for i in range(0, len(_price_list_)):
            writer.writerow(
                {
                    'Symbol': _symbol_list_[i],
                    'Day1': _price_list_[i][0],
                    'Day2': _price_list_[i][1],
                    'Day3': _price_list_[i][2],
                    'Day4': _price_list_[i][3],
                    'Day5': _price_list_[i][4],
                }
            )
os.remove("temp.csv")
