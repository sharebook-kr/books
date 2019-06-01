from pandas import Series

data = [1000, 2000, 3000]
index = ["메로나", "구구콘", "하겐다즈"]
s = Series(data=data, index=index)

print(s[[0, 2]])
print(s[["메로나", "하겐다즈"]])