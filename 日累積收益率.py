import matplotlib.pyplot as plt
import yfinance as yf
import datetime


# 設定時間範圍
start = datetime.datetime(2024, 10, 1)
end = datetime.datetime(2024, 10, 30)

# 擷取股票數據
tesla = yf.download("TSLA", start=start, end=end)
ford = yf.download("F", start=start, end=end)
general_motors = yf.download("GM", start=start, end=end)

# 計算日百分比變動
tesla['returns'] = tesla['Close'].pct_change()
ford['returns'] = ford['Close'].pct_change()
general_motors['returns'] = general_motors['Close'].pct_change()

# 計算累積日收益率
tesla['cumulative_returns'] = (1 + tesla['returns']).cumprod()
ford['cumulative_returns'] = (1 + ford['returns']).cumprod()
general_motors['cumulative_returns'] = (1 + general_motors['returns']).cumprod()

# 繪製累積日收益率曲線
plt.figure(figsize=(10, 8))

plt.plot(tesla.index, tesla['cumulative_returns'], label='Tesla')
plt.plot(ford.index, ford['cumulative_returns'], label='Ford')
plt.plot(general_motors.index, general_motors['cumulative_returns'], label='GM')

plt.title('Cumulative Daily Returns (Oct 2024)')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()

plt.tight_layout()
plt.show()
