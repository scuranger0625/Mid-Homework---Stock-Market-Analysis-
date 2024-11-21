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

# 計算 Tesla、Ford 和 GM 的日百分比變動
tesla['returns'] = tesla['Close'].pct_change()
ford['returns'] = ford['Close'].pct_change()
general_motors['returns'] = general_motors['Close'].pct_change()

# 創建直方圖並比較不同公司的日收益率
plt.figure(figsize=(9, 9))

# 繪製 Tesla 的日收益率直方圖
tesla['returns'].hist(bins=50, alpha=0.5, label='Tesla')

# 繪製 Ford 的日收益率直方圖
ford['returns'].hist(bins=50, alpha=0.5, label='Ford')

# 繪製 GM 的日收益率直方圖
general_motors['returns'].hist(bins=50, alpha=0.5, label='GM')

# 添加圖例和標題
plt.legend()
plt.title('Daily Percentage Change Distribution (Oct 2024)')
plt.xlabel('Daily Returns')
plt.ylabel('Frequency')

# 顯示圖形
plt.tight_layout()
plt.show()

