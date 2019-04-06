import pandas as pd

investment = 10000000000            # 100억

#  등략률
df = pd.read_excel("./change/200206-200306.xls", index_col=0, usecols=[0, 1, 5])
code = df.index
cond = code.str[-1] == '0'          # 보통주
ordinary_shares_fluctuation = df[cond].copy()
fluctuation = ordinary_shares_fluctuation['등락률']

# 우선주 제외
df = pd.read_excel("./data/2002-06-03.xls", index_col=0, usecols=[0, 1])
code = df.index
cond = code.str[-1] == '0'          # 보통주
ordinary_shares = df[cond].copy()
ordinary_shares.insert(1, "투자금", investment/ordinary_shares.shape[0])

# 평가금액 계산
condition = ordinary_shares.index.isin(ordinary_shares_fluctuation.index)
ordinary_shares.insert(2, '등락률', fluctuation)
ordinary_shares.insert(3, '평가액', ordinary_shares['투자금'] * (1 + (ordinary_shares['등락률'] * 0.01)))
ordinary_shares['평가액'] = ordinary_shares['평가액'].fillna(0)

print('투자금: ', investment)
print('평가액: ', ordinary_shares['평가액'].sum())

