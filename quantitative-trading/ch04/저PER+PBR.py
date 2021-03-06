from pykrx import stock
import pandas as pd
import time

def 월간수익률(파일, 투자종목):
    df = pd.read_excel(파일, index_col="티커")
    필터 = df.index.isin(투자종목)    
    수익률 = df.loc[필터]['등락률']       
    
    상폐 = df['종가'] == 0
    if (len(df.loc[필터&상폐]) > 0):
        print(df.loc[필터&상폐])
    return 1 + (수익률.sum() / len(투자종목) / 100)

def 종목선정(파일, 투자종목수, tickers):
    df = pd.read_excel(파일, converters={'티커':str,})
    df = df.set_index('티커')
    
    소형주 = df.index.isin(tickers)
    
    df['PBR'] = df['PER'] * df['EPS'] / df['BPS']
    PBR조건 = (df['BPS'] != 0)&(df['PBR'] >= 0.2)
    PER조건 = df['PER'] > 0
    df = df[PBR조건&PER조건]
    
    df['RANK-PBR'] = df['PBR'].rank(ascending=True)
    df['RANK-PER'] = df['PER'].rank(ascending=True)
    df['RANK'] = df['RANK-PBR'] + df['RANK-PER']
    
    정렬 = df.sort_values(["RANK"])
    투자종목 = 정렬.iloc[:투자종목수]
    return 투자종목.index.tolist()

tickers = stock.get_index_portfolio_deposit_file("20181228", "코스피 소형주")

누적투자월 = 0
누적수익률 = 1
for year in range(2000, 2019):
    for month in range(1, 13):
        name = "{}{:02d}".format(year, month)
        종목 = 종목선정("data/PERPBR_{}.xlsx".format(name), 20, tickers)
        if len(종목) > 0:
            수익률 = 월간수익률("data/PRICEC_{}.xlsx".format(name), 종목)
            누적수익률 *= 수익률        
            print(name, "투자 {}".format(len(종목)), "{:2.2f}".format(수익률), "/ 누적수익 :", "{:2.2f}".format(누적수익률))
            누적투자월 += 1
        else:
            print(name, "투자 X")
        
print("CAGR", 누적수익률 ** (12/누적투자월))

#for year in range(2000, 2019):
#    for month in range(1, 13):
#        business_days = stock.get_business_days(year, month)
#        print(business_days[0])
#        df = stock.get_market_fundamental_by_ticker(business_days[0], "KOSPI")        
#        df.to_excel("PERPBR_{}{:02d}.xlsx".format(year, month))
#        time.sleep(1)

#for year in range(2000, 2019):
#    for month in range(1, 13):        
#        strt = "{}{:02d}01".format(year, month)
#        last = "{}{:02d}31".format(year, month)
#        print(strt, last)
#        df = stock.get_market_price_change_by_ticker(strt, last)        
#        df.to_excel("PRICEC_{}{:02d}.xlsx".format(year, month))
#        time.sleep(1)
