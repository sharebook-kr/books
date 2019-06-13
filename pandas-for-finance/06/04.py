from pykrx import stock
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"
samsung_df = stock.get_market_ohlcv_by_date("20180101", "20190531", "005930")
lge_df = stock.get_market_ohlcv_by_date("20180101", "20190531", "066570")

plt.plot(samsung_df['종가'])
plt.plot(lge_df['종가'])
plt.show()
