from pandas import Series, DataFrame



daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low' :  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}

date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'], index=date)
print(daeshin_day)
print("1---------------")
close = daeshin_day['close']
print(close)
# 오류..... 키값을 못찾는다.
#print(daeshin_day['16.02.24'])

print("2---------------")
day_data = daeshin_day.ix['16.02.24']
print(day_data)
print(type(day_data))

print("3---------------")
print(daeshin_day.columns)
print(daeshin_day.index)
# 결과
# Index(['open', 'high', 'low', 'close'], dtype='object')
# Index(['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23'], dtype='object')