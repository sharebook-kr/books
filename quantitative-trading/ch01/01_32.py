import pandas as pd
import os

TAX_RATIO = 0.3 * 0.01                          # 0.3%
INIT_INVESTMENT = 100000000000


def backtest(start, end, investment):
    # 등략률 엑셀
    fluctuation_xls_name = "./fluctuation/{}-{}.xls".format(start, end)
    df = pd.read_excel(fluctuation_xls_name, usecols=[0, 1, 5], dtype={'종목코드': str})
    df.set_index('종목코드', inplace=True)
    cond = df.index.str[-1] == '0'                          # 보통주 조건
    common_share_fluctuation = df[cond]                     # 우선주 제외
    fluctuation = common_share_fluctuation['등락률']

    # 상장종목 엑셀
    item_xls_name = "./data/{}.xls".format(start)
    df = pd.read_excel(item_xls_name, usecols=[0, 1], dtype={'종목코드': str})
    df.set_index('종목코드', inplace=True)

    cond = df.index.str[-1] == '0'                          # 보통주
    common_share_list = df[cond].copy()
    common_share_list["투자액"] = investment/len(common_share_list)

    # 평가금액 계산
    common_share_list['등락률'] = fluctuation
    transfer_price = common_share_list['투자액'] * (1 + (common_share_list['등락률'] * 0.01))
    tax = transfer_price * TAX_RATIO
    common_share_list['평가액'] = transfer_price - tax
    return common_share_list['평가액'].sum()


def main():
    date_list = [x[:8] for x in os.listdir('./data')]
    investment = INIT_INVESTMENT

    for i, start in enumerate(date_list[:-1]):
        end = date_list[i+1]
        investment = backtest(start, end, investment)
        print(start, end, investment)

    year = len(date_list) - 1
    CAGR = (investment/INIT_INVESTMENT) ** (1/year) -1

    print("초기투자금액: ", INIT_INVESTMENT)
    print("최종금액: ", investment)
    print("투자기간: {} 년".format(year))
    print("CAGR: {:.2%} ".format(CAGR))


if __name__ == "__main__":
    main()
