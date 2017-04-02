import csv


def __create_feature__(__interval__, __symbol__, __stock_company_file__):

    __out_stock_company_file__ = "features/"+str(__interval__)+"_"+__symbol__+".csv"

    date_list = []
    open_price_list = []
    high_price_list = []
    low_price_list = []
    close_price_list = []
    prev_close_list = []
    volume_list = []

    with open(__stock_company_file__) as __csv_file__:
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

    for i in range(0, len(date_list)-__interval__):
        result = 0
        for j in range(i+1, i+__interval__+1):
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

    for i in range(0, len(date_list)-__interval__):
        result = 0
        for j in range(i+1, i + __interval__ + 1):
            result = result + flag_list[j]
        momentum_list.append(int(result / __interval__))

    day1 = []
    day2 = []
    day3 = []
    day4 = []
    day5 = []

    for i in range(5, len(date_list)):

         count = 0
         __diff__ = 0.50

         result = close_price_list[i - 1 - count] - close_price_list[i]
         if -__diff__ <= result <= __diff__:
             day1.append(0)
         if result > __diff__:
             day1.append(1)
         if result < -__diff__:
             day1.append(-1)
         count += 1

         result = close_price_list[i - 1 - count] - close_price_list[i]
         if -__diff__ <= result <= __diff__:
             day2.append(0)
         if result > __diff__:
             day2.append(1)
         if result < -__diff__:
             day2.append(-1)
         count += 1

         result = close_price_list[i - 1 - count] - close_price_list[i]
         if -__diff__ <= result <= __diff__:
             day3.append(0)
         if result > __diff__:
             day3.append(1)
         if result < -__diff__:
             day3.append(-1)
         count += 1

         result = close_price_list[i - 1 - count] - close_price_list[i]
         if -__diff__ <= result <= __diff__:
             day4.append(0)
         if result > __diff__:
             day4.append(1)
         if result < -__diff__:
             day4.append(-1)
         count += 1

         result = close_price_list[i - 1 - count] - close_price_list[i]
         if -__diff__ <= result <= __diff__:
             day5.append(0)
         if result > __diff__:
             day5.append(1)
         if result < -__diff__:
             day5.append(-1)

    del date_list[:5]
    del prev_close_list[:5]
    del open_price_list[:5]
    del high_price_list[:5]
    del low_price_list[:5]
    del close_price_list[:5]
    del momentum_list[:5]
    del volatility_list[:5]

    temp = len(day1)-__interval__

    day1 = day1[:temp]
    day2 = day2[:temp]
    day3 = day3[:temp]
    day4 = day4[:temp]
    day5 = day5[:temp]
    date_list = date_list[:temp]
    prev_close_list = prev_close_list[:temp]
    open_price_list = open_price_list[:temp]
    high_price_list = high_price_list[:temp]
    low_price_list = low_price_list[:temp]
    close_price_list = close_price_list[:temp]

    with open(__out_stock_company_file__, 'w') as __csv_file_Write__:
        fieldnames = ['Id', 'Date', 'Open', 'High', 'Low', 'Close Price', 'Prev Close Price', 'Volume',
                      'Momentum of Close Price', 'Volatility of Close Price', 'Day1', 'Day2', 'Day3', 'Day4', 'Day5']
        writer = csv.DictWriter(__csv_file_Write__, fieldnames=fieldnames)
        writer.writeheader()
        count = 0
        for i in range(0, len(date_list)):

            writer.writerow(
                {
                    'Id': count,
                    'Date': date_list[i],
                    'Open': open_price_list[i],
                    'High': high_price_list[i],
                    'Low': low_price_list[i],
                    'Close Price': close_price_list[i],
                    'Prev Close Price': prev_close_list[i],
                    'Volume': volume_list[i],
                    'Momentum of Close Price': momentum_list[i],
                    'Volatility of Close Price': volatility_list[i],
                    'Day1': day1[i],
                    'Day2': day2[i],
                    'Day3': day3[i],
                    'Day4': day4[i],
                    'Day5': day5[i],
                }
            )

            count += 1

