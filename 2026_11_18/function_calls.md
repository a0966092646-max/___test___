# Python 函式呼叫與參數傳遞完全指南

> 本講義專為 Python 學習者設計，重點解析**如何正確呼叫函式**，以及函式定義與呼叫中常見的特殊符號：`/`、`*`、`**` 與**引數名稱**的使用規則。

---

## 目錄
1. [核心觀念：參數 (Parameter) 與引數 (Argument)](#1-核心觀念參數-parameter-與引數-argument)
2. [基礎呼叫：位置引數 vs. 關鍵字引數](#2-基礎呼叫位置引數-vs-關鍵字引數)
3. [特殊符號 `/`：僅限位置引數 (Positional-Only)](#3-特殊符號--僅限位置引數-positional-only)
4. [特殊符號 `*`：關鍵字限定與引數打包/解包](#4-特殊符號-關鍵字限定與引數打包解包)
   - [用法 1：單獨的 `*`（僅限關鍵字引數 Keyword-Only）](#用法-1單獨的--僅限關鍵字引數-keyword-only)
   - [用法 2：`*args`（收集多餘的位置引數為 Tuple）](#用法-2args收集多餘的位置引數為-tuple)
   - [用法 3：呼叫端的 `*` 解包 (Unpacking)](#用法-3呼叫端的--解包-unpacking)
5. [特殊符號 `**`：字典打包與解包](#5-特殊符號-字典打包與解包)
   - [用法 1：`**kwargs`（收集多餘的關鍵字引數為 Dict）](#用法-1kwargs收集多餘的關鍵字引數為-dict)
   - [用法 2：呼叫端的 `**` 解包 (Unpacking)](#用法-2呼叫端的--解包-unpacking)
6. [大一統全貌：參數順序規則與速查表](#6-大一統全貌參數順序規則與速查表)
7. [常見錯誤與除錯指南 (TypeError 解析)](#7-常見錯誤與除錯指南-typeerror-解析)
8. [隨堂實戰練習與解答](#8-隨堂實戰練習與解答)

---

## 1. 核心觀念：參數 (Parameter) 與引數 (Argument)

在寫程式時，大家常把「參數」與「引數」混著叫，但釐清兩者差異對於理解呼叫規則至關重要：

- **參數 (Parameter)**：**定義**函式時宣告的變數名稱（佔位符）。
- **引數 (Argument)**：**呼叫**函式時實際傳遞進去的具體數值或物件。

```python
# 定義函式時：name 與 greeting 是「參數 (Parameters)」
def say_hello(name, greeting):
    return f"{greeting}, {name}!"

# 呼叫函式時："Alice" 與 "早安" 是「引數 (Arguments)」
msg = say_hello("Alice", "早安")
print(msg)  # 輸出: 早安, Alice!
```

---

## 2. 基礎呼叫：位置引數 vs. 關鍵字引數

在呼叫函式時，主要有兩種傳入引數的方式：

### 2.1 位置引數 (Positional Arguments)
依照參數在函式定義中的**前後順序**依序傳入值。

```python
def create_user(username, age):
    print(f"使用者: {username}, 年齡: {age}")

# 依順序傳入：username="小明", age=18
create_user("小明", 18)

# 順序調換會產生邏輯錯誤或型別錯誤！
create_user(18, "小明")  # 使用者: 18, 年齡: 小明（語意混亂）
```

### 2.2 關鍵字引數 (Keyword Arguments / 指名引數)
在呼叫時**明確寫出參數名稱**（`參數名=值`）。

**優點：**
1. **可讀性極佳**：不用查文件也能一眼看出傳入的值代表什麼。
2. **順序可任意對調**：只要有名稱，順序無所謂。

```python
# 接續上例的 create_user(username, age) 定義：
# 明確指定參數名稱，順序調換也完全沒問題
create_user(age=18, username="小明")
# 輸出: 使用者: 小明, 年齡: 18
```

### 2.3 混用規則：位置引數在前，關鍵字引數在後！

> [!CAUTION]
> **鐵律**：如果混用位置引數與關鍵字引數，**位置引數必須全部放在關鍵字引數的前面**！

```python
# 合法：位置引數在前，關鍵字引數在後
create_user("小明", age=18)
# 輸出: 使用者: 小明, 年齡: 18

# 非法！Python 會直接拋出語法錯誤：
# create_user(username="小明", 18)
# SyntaxError: positional argument follows keyword argument
```

---

## 3. 特殊符號 `/`：僅限位置引數 (Positional-Only)

從 Python 3.8 開始，引入了斜線符號 `/`。

### 3.1 語法意義
在函式定義中，**出現在 `/` 左側的所有參數，呼叫時「只能使用位置引數」傳遞，絕對不能寫出參數名稱！**

```python
def calculate_bmi(weight, height, /):
    return weight / ((height / 100) ** 2)

# 正確呼叫（純位置引數）
print(calculate_bmi(70, 175))

# 錯誤呼叫！使用了參數名稱
# calculate_bmi(weight=70, height=175)
# 會觸發 TypeError: calculate_bmi() got some positional-only arguments passed as keyword arguments: 'weight, height'
```

### 3.2 為什麼需要 `/`？
1. **API 設計安全**：作者未來重構程式碼想把參數名 `weight` 改成 `w_kg`，只要呼叫端不能用引數名稱呼叫，就不會破壞使用者的舊程式。
2. **參數名稱不具語意價值時**：例如 Python 內建函式 `abs(-5)` 或 `len([1, 2, 3])`，若寫成 `abs(x=-5)` 反而多餘。
3. **與 C 語言撰寫的高效底層模組介面保持一致**。

---

## 4. 特殊符號 `*`：關鍵字限定與引數打包/解包

星號 `*` 在函式中扮演了三種強大的角色：

### 用法 1：單獨的 `*`（僅限關鍵字引數 Keyword-Only）
在函式定義中，單獨放置一個 `*` 作為分隔符。
**出現在 `*` 右側的所有參數，呼叫時「必須使用關鍵字引數」傳遞，不能只傳位置！**

```python
def send_email(to, content, *, urgent=False, retry=3):
    print(f"寄送給 {to} | 緊急: {urgent} | 重試次數: {retry}")

# 正確呼叫：
send_email("boss@example.com", "報告已送達", urgent=True, retry=5)
send_email("boss@example.com", "會議提醒")  # urgent 與 retry 有預設值

# 錯誤呼叫！
# send_email("boss@example.com", "報告已送達", True, 5)
# 會觸發 TypeError: send_email() takes 2 positional arguments but 4 were given
```

> [!TIP]
> **教學設計意圖**：
> 為什麼要用單獨的 `*`？
> 想像如果寫 `send_email("boss@example.com", "報告", True, 5)`，讀程式碼的人根本猜不出 `True` 和 `5` 是什麼意思。
> 強制加上 `urgent=True, retry=5` 能大幅提升程式碼維護性，杜絕「神秘布林值 (Boolean Flag Trap)」。

---

### 用法 2：`*args`（收集多餘的位置引數為 Tuple）
當你不知道呼叫者會傳入幾個位置引數時，在參數名稱前加上單星號 `*`（慣用名稱為 `args`，全名 arguments）。
Python 會把所有多出來的位置引數**打包成一個 Tuple**。

```python
def calculate_sum(*numbers):
    print("收到的 numbers 型態:", type(numbers), "內容:", numbers)
    return sum(numbers)

print(calculate_sum(1, 2, 3))        # numbers 是 (1, 2, 3)，回傳 6
print(calculate_sum(10, 20, 30, 40)) # numbers 是 (10, 20, 30, 40)，回傳 100
print(calculate_sum())               # numbers 是 ()，回傳 0
```

---

### 用法 3：呼叫端的 `*` 解包 (Unpacking)
如果在**呼叫函式**時，你手上有一個串列 (list) 或元組 (tuple)，想要把裡面的元素一個一個拆開傳給函式的各個參數，只要在呼叫時加上 `*`：

```python
def point_3d(x, y, z):
    print(f"X={x}, Y={y}, Z={z}")

coords = [10, 20, 30]

# 一般寫法：繁瑣
point_3d(coords[0], coords[1], coords[2])

# 解包寫法：優雅簡潔！
point_3d(*coords)  # 等同於 point_3d(10, 20, 30)
```

---

## 5. 特殊符號 `**`：字典打包與解包

雙星號 `**` 專門用來處理**鍵值對 (Key-Value) / 字典 (Dictionary)**。

### 用法 1：`**kwargs`（收集多餘的關鍵字引數為 Dict）
在函式定義的參數名前加上 `**`（慣用名稱為 `kwargs`，全名 keyword arguments）。
Python 會把未預先宣告的所有關鍵字引數**打包成一個 Dictionary**。

```python
def student_profile(name, **details):
    print(f"學生: {name}")
    print("額外資訊型態:", type(details))
    for key, value in details.items():
        print(f"  - {key}: {value}")

student_profile("小華", age=16, city="台北", hobby="吉他")
# 輸出:
# 學生: 小華
# 額外資訊型態: <class 'dict'>
#   - age: 16
#   - city: 台北
#   - hobby: 吉他
```

---

### 用法 2：呼叫端的 `**` 解包 (Unpacking)
當你手上有一個字典，想把裡面的 key-value 拆成 `key=value` 的關鍵字引數傳給函式時，在呼叫時加上 `**`：

```python
def render_button(text, color, size):
    print(f"按鈕文字: {text}, 顏色: {color}, 大小: {size}")

config = {
    "text": "確認送出",
    "color": "藍色",
    "size": "大"
}

# 呼叫時解包字典：
render_button(**config)
# 等同於: render_button(text="確認送出", color="藍色", size="大")
```

---

## 6. 大一統全貌：參數順序規則與速查表

Python 允許在同一個函式中結合這些語法，但**順序不可顛倒**！

### 6.1 函式定義的終極順序

```text
def func(pos_only, /, standard, *args, kw_only, **kwargs):
          ^^^^^^^^     ^^^^^^^^  ^^^^^  ^^^^^^^  ^^^^^^^^
             1            2        3       4        5
```

| 順序 | 區域名稱 | 定義語法 | 呼叫時的限制 |
| :--- | :--- | :--- | :--- |
| **1** | **僅限位置參數** (Positional-Only) | 在 `/` 之前 | **只能**用位置傳入，不可使用引數名稱。 |
| **2** | **標準位置或關鍵字參數** | `/` 與 `*` 之間 | 既可用位置傳入，也可以用關鍵字傳入。 |
| **3** | **可變長度位置參數** | `*args` | 接收任意數量多出來的位置引數（存為 tuple）。 |
| **4** | **僅限關鍵字參數** (Keyword-Only) | 在 `*` 或 `*args` 之後 | **必須**使用關鍵字傳入 (`name=value`)。 |
| **5** | **可變長度關鍵字參數** | `**kwargs` | 接收任意數量多出來的關鍵字引數（存為 dict）。 |

### 6.2 綜合範例示範

```python
def order_coffee(size, /, sweet="正常", *extras, temperature, **custom_notes):
    print(f"容量: {size}")
    print(f"甜度: {sweet}")
    print(f"額外加料 (*extras): {extras}")
    print(f"溫度 (僅限關鍵字): {temperature}")
    print(f"客製化備註 (**custom_notes): {custom_notes}")

# 合法呼叫範例：
order_coffee(
    "大杯",                   # size（/ 之前，只能位置）
    "半糖",                   # sweet（標準參數，位置傳入）
    "珍珠", "椰果",          # *extras（打包為 ('珍珠', '椰果')）
    temperature="少冰",       # temperature（* 之後，必須關鍵字）
    takeaway=True, cup="環保杯" # **custom_notes（打包為 dict）
)
```

---

## 7. 常見錯誤與除錯指南 (TypeError 解析)

學生在呼叫函式時最常遇到的錯誤訊息，請教導學生如何看懂並修正：

### 錯誤 1：位置引數放在關鍵字引數後面
```python
def add(a, b):
    return a + b

# add(a=1, 2)
# 語法錯誤: SyntaxError: positional argument follows keyword argument
```
> **修正**：將所有位置引數全部移到前面，例如 `add(1, b=2)`。

---

### 錯誤 2：同一個參數被重複給值
```python
def greet(name, msg="你好"):
    print(f"{name}: {msg}")

# greet("小明", "早安", name="小美")
# 錯誤訊息: TypeError: greet() got multiple values for argument 'name'
```
> **原因**：第一個位置引數已經把 `"小明"` 給了 `name`，後面又傳了 `name="小美"`。

---

### 錯誤 3：對 `/` 之前的參數使用關鍵字傳值
```python
def square(x, /):
    return x ** 2

# square(x=5)
# 錯誤訊息: TypeError: square() got some positional-only arguments passed as keyword arguments: 'x'
```
> **修正**：直接呼叫 `square(5)`，不可指定參數名稱。

---

### 錯誤 4：漏掉 `*` 之後必須指定的關鍵字引數
```python
def alert(*, code, message):
    print(f"[{code}] {message}")

# alert(404, "Not Found")
# 錯誤訊息: TypeError: alert() takes 0 positional arguments but 2 were given
```
> **修正**：必須指定名稱：`alert(code=404, message="Not Found")`。

---

## 8. 隨堂實戰練習與解答

### 練習 1：基礎觀察題
請預測下列程式碼的執行結果，若會報錯，請指出原因：
```python
def calc(a, b, /, c, *, d):
    return a + b + c + d

# 呼叫 A
result_a = calc(1, 2, 3, d=4)
print("呼叫 A 結果:", result_a)

# 呼叫 B（思考：若取消註解執行，會發生什麼事？）
# calc(a=1, b=2, c=3, d=4)

# 呼叫 C（思考：若取消註解執行，會發生什麼事？）
# calc(1, 2, c=3, 4)
```

<details>
<summary>點擊展開看解答</summary>

- **呼叫 A**：成功執行，回傳 `10`。
  - `a=1, b=2` 符合 `/` 之前的僅限位置規則。
  - `c=3` 為標準參數（此處以位置引數傳入，合法）。
  - `d=4` 為 `*` 之後的關鍵字限定參數，合法。
- **呼叫 B**：報錯 `TypeError`。
  - 因為 `a` 和 `b` 位於 `/` 之前，不得使用 `a=1, b=2`。
- **呼叫 C**：報錯 `SyntaxError`（或 `TypeError`）。
  - 因為 `4` 為位置引數，不能放在關鍵字引數 `c=3` 後面；且 `d` 為關鍵字限定參數，必須寫 `d=4`。
</details>

---

### 練習 2：動手設計題 —— API 守門員
**題目需求**：
請定義一個建立資料庫連線的函式 `connect_db`：
1. 第一個參數 `host` 必須是**僅限位置引數**。
2. 第二個參數 `port` 為預設 `3306` 的標準參數。
3. 後面兩個參數 `username` 與 `password` 必須是**僅限關鍵字引數**。

<details>
<summary>點擊展開看解答</summary>

```python
def connect_db(host, /, port=3306, *, username, password):
    print(f"連線至 {host}:{port}，使用者: {username}")

# 測試正確呼叫方式：
connect_db("localhost", 3306, username="admin", password="secret_password")
connect_db("127.0.0.1", username="root", password="123")  # 使用 port 預設值
```
</details>

---

### 練習 3：萬用印表機 —— 打包與解包綜合練習
**題目需求**：
請撰寫一個日誌記錄函式 `smart_logger`：
1. 第一個參數為 `level`（如 `"INFO"`, `"ERROR"`）。
2. 接下來可傳入任意數量的訊息物件（使用 `*args` 收集）。
3. 最後可傳入任意數量的標籤 metadata（使用 `**kwargs` 收集）。
4. 函式須將 level、訊息、與 key-value 標籤格式化輸出。

<details>
<summary>點擊展開看解答</summary>

```python
def smart_logger(level, *messages, **metadata):
    msg_body = " ".join(str(m) for m in messages)
    print(f"[{level.upper()}] {msg_body}")
    if metadata:
        print("  中繼資料:")
        for k, v in metadata.items():
            print(f"    - {k}: {v}")

# 測試呼叫：
smart_logger("INFO", "系統啟動完成", "耗時 0.42 秒", user="admin", ip="192.168.1.1")
```
</details>
