from pandas import Series

index = [0, 1, 2]
data = [1000, 2000, 3000]
s = Series(data=data, index=index)

print(s[0:2])
