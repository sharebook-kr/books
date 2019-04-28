import pandas as pd
import os

# 초기 투자액
SEED_MONEY = 10000000000


def backtest(start, end, 투자금액):
    #-------------------------------------------------------------------------
    # 상장종목 엑셀
    excel_name = "./data/{}.xls".format(start)
    df = pd.read_excel(excel_name,
                       usecols = [0, 1],
                       dtype = {"종목코드": str})

    df.set_index("종목코드", inplace = True)
    cond = df.index.str[-1] == '0'
    상장종목 = df[cond].copy()

    #-------------------------------------------------------------------------
    # 등락률 엑셀
    excel_name = "./fluctuation/{}-{}.xls".format(start, end)
    df = pd.read_excel(excel_name,
                       usecols = [0, 1, 5],
                       dtype = {"종목코드": str})
    df.set_index("종목코드", inplace = True)
    cond = df.index.str[-1] == '0'
    등락률 = df[cond]['등락률']

    #-------------------------------------------------------------------------
    상장종목['등락률'] = 등락률
    상장종목['투자액'] = 투자금액 / len(상장종목)
    상장종목['평가액(세전)'] = 상장종목['투자액'] * (1 + (상장종목['등락률'] * 0.01))
    세금 = 상장종목['평가액(세전)'] * 0.3 * 0.01
    상장종목['평가액(세후)'] = 상장종목['평가액(세전)'] - 세금
    return 상장종목['평가액(세후)'].sum()


def main():
    date_list = [x[:8] for x in os.listdir('./data')]
    investment = SEED_MONEY

    for i, start in enumerate(date_list[:-1]):
        end = date_list[i+1]
        investment = backtest(start, end, investment)
        print("{} {} {:,}".format(start, end, int(investment)))

    year = len(date_list) - 1
    CAGR = (investment/SEED_MONEY) ** (1/year) -1

    print("초기투자금액: {:,}".format(SEED_MONEY))
    print("최종금액: {:,}".format(int(investment)))
    print("투자기간: {} 년".format(year))
    print("CAGR: {:.2%} ".format(CAGR))


if __name__ == "__main__":
    main()