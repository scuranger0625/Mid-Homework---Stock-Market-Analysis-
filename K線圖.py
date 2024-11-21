import matplotlib.pyplot as plt
import yfinance as yf
import datetime
import mplfinance as mpf 

# 設定時間範圍
start = datetime.datetime(2024, 10, 1)
end = datetime.datetime(2024, 10, 30)

# 擷取股票數據
tesla = yf.download("TSLA", start=start, end=end)
ford = yf.download("F", start=start, end=end)
general_motors = yf.download("GM", start=start, end=end)

# 創建一個3行2列的子圖佈局
fig, ax = plt.subplots(3, 2, figsize=(9, 9))

# 繪製 Tesla 的 K 線圖和成交量圖
mpf.plot(tesla, type='candle', style='charles', ax=ax[0, 0], volume=ax[0, 1], show_nontrading=True)
ax[0, 0].set_title('Tesla K-line, Oct 2024')

# 繪製 Ford 的 K 線圖和成交量圖
mpf.plot(ford, type='candle', style='charles', ax=ax[1, 0], volume=ax[1, 1], show_nontrading=True)
ax[1, 0].set_title('Ford K-line, Oct 2024')

# 繪製 GM 的 K 線圖和成交量圖
mpf.plot(general_motors, type='candle', style='charles', ax=ax[2, 0], volume=ax[2, 1], show_nontrading=True)
ax[2, 0].set_title('GM K-line, Oct 2024')

# 調整佈局並顯示圖形
plt.tight_layout()
plt.show()
