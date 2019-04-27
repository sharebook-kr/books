import pandas as pd

# 초기 투자액
SEED_MONEY = 10000000000

# 상장종목
df = pd.read_excel("./data/20020617.xls",
                   usecols = [0, 1],
                   dtype = {"종목코드": str})
df.set_index("종목코드", inplace = True)
cond = df.index.str[-1] == '0'
상장종목 = df[cond].copy()
상장종목.to_excel("data1.xlsx")

# 등락률 컬럼 추출
df = pd.read_excel("./fluctuation/20020617-20030616.xls",
                   usecols = [0, 1, 5],
                   dtype = {"종목코드": str})
df.set_index("종목코드", inplace = True)
cond = df.index.str[-1] == '0'
등락률 = df[cond]['등락률']
등락률.to_excel("data2.xlsx")

# 등락률 컬럼 추가
상장종목['등락률'] = 등락률

# 투자액 (동일비중) 설정
상장종목['투자액'] = SEED_MONEY / len(상장종목)

# 평가액 계산
상장종목['평가액(세전)'] = 상장종목['투자액'] * (1 + (상장종목['등락률'] * 0.01))
세금 = 상장종목['평가액(세전)'] * 0.3 * 0.01
상장종목['평가액(세후)'] = 상장종목['평가액(세전)'] - 세금

# 수익률 계산
print("2002년 투자금액: ", SEED_MONEY)
print("2003년 평가금액: ", 상장종목['평가액(세후)'].sum())
상장종목.to_excel("data3.xlsx")


