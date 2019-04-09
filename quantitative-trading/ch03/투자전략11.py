from pykrx import stock

# 투자전략11 P.297
# 1) 과거 12개월의 수익률의 표준 편차를 계산함
# 2) 주식 비중은 = 목표 변동성 / 실제 변동성

목표 = 0.04
df = stock.get_index_kospi_ohlcv_by_date("19950101", "20180631", "코스피 200", "m")
df['변동'] = df['고가'] / df['시가'] - 1
df['편차'] = df['변동'].rolling(12).std().shift(1)
df['비중'] = 목표 / df['편차']
df['수익률'] = 1 + (df['종가'] - df['시가']) / df['시가'] * df['비중']
df['누적수익률'] = df['수익률'].cumprod()
print(df['누적수익률'].iloc[-1])

# 책에는 8배의 기간 수익이라고 돼있지만 실제로 1배.....
# GG