from pandas import Series

index = ["2019-05-31", "2019-05-30", "2019-05-29", "2019-05-28", "2019-05-27"]
data = [42500, 42550, 41800, 42550, 42650]

s = Series(data=data, index=index)
print(s)