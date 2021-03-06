from pandas import DataFrame

data = [
    ["037730", "3R", 1510],
    ["036360", "3SOFT", 1790],
    ["005760", "ACTS", 1185],
]

columns = ["종목코드", "종목명", "현재가"]
df = DataFrame(data=data, columns=columns)
df = df.set_index('종목코드')
print(df)

df.columns = ['name', 'close']          # 컬럼 이름 변경
df.index.name = 'code'                  # 인덱스 name 변경
print(df)

