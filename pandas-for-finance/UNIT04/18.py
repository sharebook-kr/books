from pandas import Series, DataFrame

data = [
    [112000, 112500, 109500, 110500],
    [114000, 114500, 110500, 111000],
    [113000, 115000, 112000, 115000],
    [111500, 112500, 110000, 111500],
    [111000, 114000, 109500, 112000],
]

columns = ["시가", "고가", "저가", "종가"]
index = ["2019-06-05", "2019-06-04", "2019-06-03", "2019-05-31", "2019-05-30"]
df = DataFrame(data=data, index=index, columns=columns)

df.drop("2019-05-30", axis=0, inplace=True)
print(df)

