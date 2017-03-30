from sklearn import svm
from sklearn.svm import SVC
import csv


prev_close_list=[]
close_price_list=[]
momentum_list=[]
volatility_list=[]
high_price_list=[]
low_price_list=[]
average_price_list=[]
total_traded_quantity_list=[]

index_momentum_list=[]
index_volatility_list=[]

day1_list=[]
day2_list=[]
day3_list=[]
day4_list=[]
day5_list=[]


with open('features_10day_csv.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        momentum_list.append(int(row['Momentum of Close Price']))
        prev_close_list.append(float(row['Prev Close']))
        close_price_list.append(float(row['Close Price']))
        volatility_list.append(float(row['Volatility of Close Price']))
        high_price_list.append(float(row['High Price']))
        low_price_list.append(float(row['Low Price']))
        average_price_list.append(float(row['Average Price']))
        total_traded_quantity_list.append(int(row['Total Traded Quantity']))

        index_momentum_list.append(int(row['Momentum Bases on Index']))
        index_volatility_list.append(float(row['Volatility Bases on Index']))

        day1_list.append(int(row['Day1']))
        day2_list.append(int(row['Day1']))
        day3_list.append(int(row['Day3']))
        day4_list.append(int(row['Day4']))
        day5_list.append(int(row['Day5']))

# x=[list(a) for a in zip(prev_close_list, close_price_list,momentum_list,volatility_list,high_price_list,low_price_list,average_price_list,total_traded_quantity_list,index_momentum_list,index_volatility_list)]
# y=[list(b) for b in zip(day1_list,day2_list)]
x=[list(a) for a in zip(prev_close_list, close_price_list,volatility_list,high_price_list,low_price_list,average_price_list,total_traded_quantity_list,index_momentum_list,index_volatility_list)]
X = x
Y = momentum_list
clf = svm.SVC()
clf.fit(X, Y)
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

print (clf.predict([[2353.0, 2353.0, -0.0002571111961719646, 2378.75, 2345.05, 2364.53, 1435829, 0, 0.4926051550212077]]))
