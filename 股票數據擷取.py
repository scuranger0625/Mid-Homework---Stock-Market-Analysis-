import yfinance as yf
import datetime

# 設定起始和結束日期
start = datetime.datetime(2024, 10, 1)
end = datetime.datetime(2024, 10, 30)

# 使用 yfinance 獲取 Tesla 的歷史數據
tesla = yf.download("TSLA", start=start, end=end)
ford = yf.download("F", start=start, end=end)
general_motors = yf.download("GM", start=start, end=end)

# 顯示前五行數據
print(tesla.head(30))
print(ford.head(30))
print(general_motors.head(30))