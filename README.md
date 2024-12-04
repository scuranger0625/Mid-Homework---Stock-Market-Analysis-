
# 股票數據分析與視覺化專案 / Stock Data Analysis and Visualization Project

本專案包含四個 Python 腳本，使用 `yfinance` 套件進行股票數據擷取與分析，並以 Matplotlib 和 mplfinance 進行數據視覺化。
分析的股票為 Tesla (TSLA)、Ford (F)、General Motors (GM)，數據範圍為 2024 年 10 月 1 日至 2024 年 10 月 30 日。

This project includes four Python scripts that use the `yfinance` library to fetch and analyze stock data, with data visualization done using Matplotlib and mplfinance.
The analyzed stocks are Tesla (TSLA), Ford (F), and General Motors (GM), with data ranging from October 1, 2024, to October 30, 2024.

## 文件結構 / File Structure

1. **K線圖.py / K-line Chart.py**
   - **功能 / Functionality**: 生成特定股票的 K 線圖和成交量圖 / Generate K-line charts and volume plots for specific stocks.
   - **輸入 / Input**: 股票代碼及時間範圍 / Stock symbols and time range.
   - **輸出 / Output**: K 線圖和成交量圖的視覺化圖表 / Visualized K-line and volume charts.
   - **使用套件 / Libraries Used**: `matplotlib.pyplot`, `mplfinance`, `yfinance`.

2. **日百分比變動直方圖.py / Daily Percentage Change Histogram.py**
   - **功能 / Functionality**: 計算股票的日收益百分比變動並生成直方圖 / Calculate daily percentage changes and generate histograms.
   - **輸入 / Input**: 股票數據 / Stock data.
   - **輸出 / Output**: 各公司的日收益百分比變動分布圖 / Daily percentage change distribution for each company.
   - **使用套件 / Libraries Used**: `matplotlib.pyplot`, `yfinance`.

3. **日累積收益率.py / Daily Cumulative Returns.py**
   - **功能 / Functionality**: 計算股票的累積日收益率並繪製曲線圖 / Calculate cumulative daily returns and plot curves.
   - **輸入 / Input**: 股票數據 / Stock data.
   - **輸出 / Output**: 各公司的累積收益率曲線 / Cumulative returns curve for each company.
   - **使用套件 / Libraries Used**: `matplotlib.pyplot`, `yfinance`.

4. **股票數據擷取.py / Stock Data Fetch.py**
   - **功能 / Functionality**: 擷取特定時間範圍內的股票數據並顯示前 30 筆數據 / Fetch stock data for a specific time range and display the first 30 rows.
   - **輸入 / Input**: 股票代碼及時間範圍 / Stock symbols and time range.
   - **輸出 / Output**: 打印 Tesla、Ford 和 GM 的前 30 筆數據 / Print the first 30 rows of Tesla, Ford, and GM data.
   - **使用套件 / Libraries Used**: `yfinance`.

## 使用方法 / How to Use

1. 安裝必要的 Python 套件 / Install the required Python libraries:
   ```bash
   pip install yfinance matplotlib mplfinance
   ```

2. 執行腳本以獲取所需結果 / Run the scripts to obtain the desired results, e.g.:
   - 若需生成 K 線圖，執行 / To generate K-line charts, run:
     ```bash
     python K線圖.py
     ```

3. 結果將以圖表形式顯示或打印至終端 / The results will be displayed as charts or printed to the terminal.

## 注意事項 / Notes

- 請確保系統具備 Python 3.8 或更高版本 / Ensure the system has Python 3.8 or above installed.
- 此專案腳本中的時間範圍與股票代碼均可根據需求修改 / The time range and stock symbols in the scripts can be modified as needed.
- 如果遇到數據缺失，請檢查網路連線或調整時間範圍 / If data is missing, check your internet connection or adjust the time range.

## 聯絡方式 / Contact

若有任何問題或建議，請聯繫開發者 / For any questions or suggestions, please contact the developer.
