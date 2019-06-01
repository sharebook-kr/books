import pandas as pd

df = pd.read_excel("./fluctuation/20020617-20030616.xls",
                   usecols=[0, 1, 5],
                   dtype={"종목코드": str})
df.set_index("종목코드", inplace=True)
cond = df.index.str[-1] == '0'
common_shares = df[cond]
print(common_shares.head())
print(common_shares.shape)
