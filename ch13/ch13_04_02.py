import pandas as pd
import pandas_datareader.data as web

#2) Pandas를 이용한 주가이동평균 계산
#https://wikidocs.net/4374
# 신기한거 투성이네... ㄷㄷ;;;

gs = web.DataReader("078930.KS", "yahoo", "2017-01-01", "2017-10-06")


print(gs.tail())


ma5 = gs['Adj Close'].rolling(window=5).mean()
print("1--------------")
print(type(ma5))
print("2--------------")
# => pandas.core.series.Series
print(ma5.tail(10))

print("3--------------")
#  신기한 구분..... 왜 Volume 값 전체를 비교해서 bool 값을 주냐... 이것도 개신기네..
# print(gs['Volume'] != 0)
#Date
#2016-01-04     True
#2016-01-05     True
#2016-01-06     True
#2016-01-07     True

print("4--------------")
new_gs = gs[gs['Volume'] !=0]
print(ma5.tail(15))

print("5--------------")
ma5 = new_gs['Adj Close'].rolling(window=5).mean()
new_gs.insert(len(new_gs.columns), "MA5", ma5)
print(new_gs.tail(5))


print("6--------------")
ma20 = new_gs['Adj Close'].rolling(window=20).mean()
new_gs.insert(len(new_gs.columns), "MA20", ma20)
print(new_gs.tail(5))

print("7--------------")
ma60 = new_gs['Adj Close'].rolling(window=60).mean()
new_gs.insert(len(new_gs.columns), "MA60", ma60)
print(new_gs.tail(5))

print("8--------------")
ma120 = new_gs['Adj Close'].rolling(window=120).mean()
new_gs.insert(len(new_gs.columns), "MA120", ma120)
print(new_gs.tail(5))