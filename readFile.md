# Python 檔案操作：一步一步練習

這份練習會帶你讀取文字檔、逐行處理內容，以及寫入和追加文字。請先把本文件、`readFile_example.py` 和 `readFile_sample.txt` 放在同一個資料夾。

## 開始之前

1. 用 VS Code 開啟這個資料夾。
2. 打開終端機，確認目前位置是這個資料夾。
3. 執行範例程式：

   ```bash
   python readFile_example.py
   ```

   Windows 若 `python` 指令無法使用，可以試試 `py readFile_example.py`。
4. 程式會讀取 `readFile_sample.txt`，並建立或更新 `readFile_output.txt`。重複執行時，輸出檔會先被覆寫。

也可以先只看程式，依照下面步驟自己輸入和執行。每次練習都從同一個資料夾執行，這樣相對路徑才會指向正確的位置。

## 第 1 步：準備文字檔

打開 `readFile_sample.txt`。裡面有幾行簡單的購物清單：

```text
蘋果 3 顆
牛奶 1 瓶
麵包 2 個
```

檔案和程式在同一個資料夾時，可以直接用檔名當作路徑。

## 第 2 步：讀取整份檔案

```python
with open("readFile_sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

- `open(...)` 開啟檔案。
- `"r"` 代表讀取（read）。讀取是預設模式，但初學時明寫會比較清楚。
- `encoding="utf-8"` 讓 Python 正確讀取中文。
- `read()` 會取得整份檔案的內容。
- `with` 區塊結束時會自動關閉檔案，不需要自己呼叫 `close()`。

**練習：**把 `print(content)` 改成 `print(content.replace("蘋果", "香蕉"))`，看看如何替換讀取到的文字。這不會修改原始檔案。

## 第 3 步：一行一行讀取

檔案很大時，逐行處理通常更方便：

```python
with open("readFile_sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
```

每個 `line` 通常已經包含換行字元。`print()` 本身也會在結尾加換行，所以這裡用 `end=""` 避免每行之間多出空白行。

**練習：**改成 `print(line.strip())`，觀察 `strip()` 如何去除每行前後的空白和換行。

## 第 4 步：把內容寫入新檔案

```python
with open("readFile_output.txt", "w", encoding="utf-8") as file:
    file.write("今天完成了檔案讀取練習。\n")
    file.write("記得使用 with 自動關閉檔案。\n")
```

`"w"` 代表寫入（write）。如果檔案不存在，Python 會建立它；如果檔案已存在，舊內容會被清除再寫入。請特別留意這個行為。

**練習：**在 `readFile_output.txt` 加上一行你自己的文字，執行程式後用文字編輯器打開檔案確認內容。

## 第 5 步：追加內容

若要保留舊內容並在檔案末尾加上文字，使用 `"a"`（append）：

```python
with open("readFile_output.txt", "a", encoding="utf-8") as file:
    file.write("這一行是後來追加的。\n")
```

**練習：**執行這段程式兩次，再打開輸出檔，確認追加的文字出現兩次。

## 第 6 步：處理檔案不存在的情況

如果要讀取的檔名拼錯，或檔案不在指定位置，Python 會產生 `FileNotFoundError`。可以用 `try` 和 `except` 顯示較容易理解的訊息：

```python
try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("找不到檔案，請確認檔名和資料夾位置。")
```

## 第 7 步：獨立挑戰

1. 讀取 `readFile_sample.txt`，並印出檔案共有幾個字元。
2. 逐行讀取清單，只印出包含「牛奶」的那一行。
3. 用追加模式，在 `readFile_output.txt` 加上一行自己的購物備註。
4. 把範例檔案複製一份並改名，再修改程式讀取新檔名。

提示：字串可以用 `len(content)` 計算字元數；可以用 `if "牛奶" in line:` 判斷某行是否包含文字。

## 常見模式速查

| 模式 | 用途 | 注意事項 |
| --- | --- | --- |
| `"r"` | 讀取 | 檔案必須已存在 |
| `"w"` | 寫入 | 建立新檔；舊檔內容會被清除 |
| `"a"` | 追加 | 建立新檔；保留原內容並加在末尾 |

初學時可以先記得這個習慣：使用 `with open(..., encoding="utf-8") as file:` 開啟文字檔，並確認使用的模式是你真正需要的。