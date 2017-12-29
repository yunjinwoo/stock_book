from pandas import Series, DataFrame
import pandas_datareader.data as web
import datetime


start = datetime.datetime(2016, 2, 19)
end = datetime.datetime(2016, 3, 4)
#gs = web.DataReader("078930.KS", "yahoo", start, end)
gs = web.DataReader("078930.KS", "yahoo")

#print(gs)
print(gs.info())

import matplotlib.pyplot as plt

plt.plot(gs['Adj Close'])
plt.show()