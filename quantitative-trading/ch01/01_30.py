import os
import pandas as pd


def get_data_list(path):
    excel_files = [x for x in os.listdir(path) if x.endswith("xls")]
    excel_files.sort()
    return excel_files


if __name__ == "__main__":
    df2002 = pd.read_excel("./data/2002-06-03.xls", index_col=0, usecols=[0, 1, 2, 14])
    df2003 = pd.read_excel("./data/2003-06-02.xls", index_col=0, usecols=[0, 1, 2, 14])

    df2002.rename(columns={'현재가':'현재가(2002)',
                           '상장주식수(주)':'상장주식수(주)(2002)'}, inplace=True)
    df2003.rename(columns={'현재가':'현재가(2003)',
                           '상장주식수(주)':'상장주식수(주)(2003)'}, inplace=True)

    # 등략률 컬럼 추가
    change = pd.read_excel("./change/200206-200306.xls", index_col=0, usecols=[0, 1, 5])

    # 옆으로 연결하기
    df = pd.concat([df2002, df2003, change], axis=1, sort=False)
    #df = pd.merge(df2002, df2003, how='outer')


    # 우선주 제외
    print(df['종목명'])

    df.to_excel("test.xlsx")
