from pykrx import stock
import pandas as pd

def 월간수익률(파일, 투자종목):
    df = pd.read_excel(파일, index_col="티커")
    필터 = df.index.isin(투자종목)    
    수익률 = df.loc[필터]['등락률']        
    return 1 + (수익률.sum() / len(투자종목) / 100)

def 종목선정(파일, 투자종목수, tickers):
    df = pd.read_excel(파일, converters={'티커':str,})
    df = df.set_index('티커')
        
    소형주 = df.index.isin(tickers)
    PER_N0 = df['PER'] != 0
    정렬 = df[소형주&PER_N0].sort_values(["PER"])
    투자종목 = 정렬.iloc[:투자종목수]
    return 투자종목.index.to_list()
    
business_days = stock.get_business_days(2000, 1)
tickers = stock.get_index_portfolio_deposit_file(business_days[0], "코스피 소형주")

누적수익률 = 1
for year in range(2000, 2019):
    for month in range(1, 13):
        name = "{}{:02d}".format(year, month)
        종목 = 종목선정("data/PERPBR_{}.xlsx".format(name), 20)
        수익률 = 월간수익률("data/PRICEC_{}.xlsx".format(name), 종목)
        누적수익률 *= 수익률        
        print("{:2.2f}".format(수익률), "/ 누적수익 :", "{:2.2f}".format(누적수익률))

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
