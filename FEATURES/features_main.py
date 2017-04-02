import FEATURES.features

if __name__ == '__main__':

    symbol_list = ["AAPL", "GOOGL", "INTC", "FB", "TSLA", "NFLX", "YHOO", "AMZN", "MSFT"]
    interval = [5, 10, 30, 90, 270]
    print('Generating features...')
    for s in symbol_list:
        __symbol__ = s
        __company_file__ = "data/"+s+".csv"
        __nasdaq_file__ = "data/NASDAQ.csv"
        for __interval__ in interval:
            FEATURES.features.__create_feature__(__interval__, __symbol__, __company_file__)
    print('Features generate successfully.')
