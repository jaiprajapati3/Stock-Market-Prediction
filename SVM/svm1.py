from sklearn import svm
from sklearn.svm import SVC
import csv

symbol_list=[]
momentum_list=[]
prev_close_list=[]
close_price_list=[]
volatility_list=[]

with open('features_10day_csv.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        symbol_list.append(row['Symbol'])
        momentum_list.append(row['Momentum of Close Price'])
        prev_close_list.append(float(row['Prev Close']))
        close_price_list.append(float(row['Close Price']))
        volatility_list.append(row['Volatility of Close Price'])

close_list=[list(a) for a in zip(prev_close_list, close_price_list,volatility_list)]

X = close_list
y = momentum_list
clf = svm.SVC()
clf.fit(X, y)
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

print (clf.predict([[2275.55,2315.85,.006329388037294266]]))