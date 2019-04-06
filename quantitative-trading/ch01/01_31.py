import pandas as pd

투자액 = 10000000000            # 100억

#  등략률
df = pd.read_excel("./change/200206-200306.xls", index_col=0, usecols=[0, 1, 5])
code = df.index
cond = code.str[-1] == '0'          # 보통주
보통주_등락률 = df[cond]
등락률 = 보통주_등락률['등락률']

# 우선주 제외
df = pd.read_excel("./data/2002-06-03.xls", index_col=0, usecols=[0, 1])
code = df.index
cond = code.str[-1] == '0'          # 보통주
ordinary_shares = df[cond].copy()
ordinary_shares["투자액"] = 투자액/len(ordinary_shares)

# 평가금액 계산
ordinary_shares['등락률'] = 등락률
ordinary_shares['평가액'] = ordinary_shares['투자액'] * (1 + (ordinary_shares['등락률'] * 0.01))

print('투자액: ', 투자액)
print('평가액: ', ordinary_shares['평가액'].sum())

