import FEATURES.features

if __name__ == '__main__':

    symbol_list = ["INTC", "FB", "TSLA", "NKE", "YHOO", "AMZN", "TCS", "MSFT"]
    __interval__  = int(input('Enter an interval from 5,10,30,90,270: '))
    for s in symbol_list:
        __symbol__ = s
        __company_file__ = "data/"+s+".csv"
        __nasdaq_file__ = "data/NASDAQ.csv"

        FEATURES.features.__create_feature__(__interval__, __symbol__, __company_file__, __nasdaq_file__)
