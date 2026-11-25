# Boost 範例

## 使用者輸入

```
/boost 幫我寫一個 Python 爬蟲抓取新聞標題
```

---

## 階段一：Boosted Prompt

## 🚀 Boosted Prompt

**目標（Goal）**
建立一個 Python 爬蟲程式，自動抓取指定新聞網站的最新標題清單。

**背景與情境（Context）**
使用者希望定期取得新聞標題，用於資料蒐集或內容追蹤。開發環境為 Python，使用 `uv` 管理套件。

**具體需求（Requirements）**
- 能抓取指定 URL 的新聞標題（`<h1>`、`<h2>` 或特定 CSS class）
- 將結果以清單形式印出，並附上對應連結
- 支援指定抓取數量（預設 10 筆）
- 處理網路錯誤與解析失敗的例外狀況
- 結果可選擇性儲存為 `.txt` 或 `.csv` 檔

**輸出格式（Output Format）**
Python 腳本（`news_scraper.py`），附上使用說明註解。

**限制條件（Constraints）**
- 不使用 Selenium，僅用 `requests` + `BeautifulSoup`
- 遵守網站的 `robots.txt`，加入適當的 `User-Agent` header

**成功標準（Success Criteria）**
- 執行後能成功印出至少 5 筆新聞標題與連結
- 遇到錯誤時顯示友善提示，不直接 crash

---

## 階段二：執行計畫

1. 安裝必要套件（`requests`、`beautifulsoup4`）
2. 建立爬蟲主體函式
3. 新增例外處理與參數設定
4. 測試執行並驗證輸出
5. 整理程式碼與加入說明註解

---

## 階段三：開始實作

（此處依計畫逐步執行）
