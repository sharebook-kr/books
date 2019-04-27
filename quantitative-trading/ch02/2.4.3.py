import pandas as pd

df = pd.read_excel("./data/20020617.xls",
                   usecols = [0, 1],
                   dtype = {"종목코드": str})
df.set_index("종목코드", inplace = True)
cond = df.index.str[-1] == '0'          # 보통주 조건
common_shares = df[cond]                 # 보통주 필터
print(common_shares.head())
print(common_shares.shape)
