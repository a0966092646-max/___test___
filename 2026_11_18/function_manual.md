# `function.ipynb` 程式碼說明書：Python 函式參數與引數完整指南

本說明書針對 [`2026_11_18/function.ipynb`](file:///C:/Users/User/Documents/暫存資料夾/git00/2026_11_18/function.ipynb) 筆記本內容進行詳細剖析與教學說明，涵蓋 Python 函式從基礎傳參到進階參數限定與打包技巧。

---

## 目錄
1. [基礎函式定義與呼叫](#1-基礎函式定義與呼叫)
2. [引數傳遞方式：位置 vs. 名稱](#2-引數傳遞方式位置-vs-名稱)
3. [混用規則與引數預設值](#3-混用規則與引數預設值)
4. [特殊限定符號：`/` 與 `*`](#4-特殊限定符號--與-)
5. [任意數量引數打包：`*args` 與 `**kwargs`](#5-任意數量引數打包-args-與-kwargs)
6. [Python 內建函式應用範例](#6-python-內建函式應用範例)
7. [常見錯誤與除錯對照表](#7-常見錯誤與除錯對照表)

---

## 1. 基礎函式定義與呼叫

### 程式碼範例
```python
def greet(name):
    print(f"Hello, {name}!")

greet("小明")
```

### 解析說明
- **定義函式 (`def`)**：宣告名為 `greet` 的函式，並設定一個參數 `name`。
- **呼叫函式**：傳入字串 `"小明"` 作為引數，函式內部使用 f-string 格式化輸出。
- **執行結果**：`Hello, 小明!`

---

## 2. 引數傳遞方式：位置 vs. 名稱

### 2.1 位置引數 (Positional Arguments)
```python
def describe_pet(animal, name):
    print(f"我養了一隻{animal}，牠叫做{name}。")

# 呼叫
describe_pet("貓", "小橘")  # 輸出: 我養了一隻貓，牠叫做小橘。
describe_pet("小橘", "貓")  # 輸出: 我養了一隻小橘，牠叫做貓。
```
- **核心概念**：依據參數在定義時的**前後順序**對應傳入。
- **注意事項**：若順序調換，可能造成語意顛倒或邏輯錯誤。引數數量必須與定義完全一致。

### 2.2 關鍵字引數 (Keyword Arguments)
```python
describe_pet(animal="貓", name="小橘")
describe_pet(name="小橘", animal="貓")
```
- **核心概念**：呼叫時明確指定 `參數名=值`。
- **優點**：**順序可自由調換**，且大幅增加程式碼的可讀性。

---

## 3. 混用規則與引數預設值

### 3.1 混用鐵律：位置引數必須在關鍵字引數前面
```python
# 正確：先傳位置引數，再傳關鍵字引數
describe_pet("狗", name="旺財")

# 錯誤語法（會引發 SyntaxError）：
# describe_pet(animal="狗", "旺財")
```

### 3.2 參數預設值 (Default Arguments)
```python
def order_drink(drink, ice="正常冰", sugar="半糖"):
    print(f"點餐：{drink}（{ice} / {sugar}）")

order_drink("紅茶")                       # 點餐：紅茶（正常冰 / 半糖）
order_drink("紅茶", "去冰")               # 點餐：紅茶（去冰 / 半糖）
order_drink("紅茶", sugar="無糖")         # 點餐：紅茶（正常冰 / 無糖）
order_drink("綠茶", sugar="微糖", ice="少冰")  # 點餐：綠茶（少冰 / 微糖）
```
- **核心概念**：有預設值的參數若未在呼叫時傳值，則自動採用預設值。
- **跳過中間參數**：若想保留 `ice` 預設值並僅更動 `sugar`，可直接使用關鍵字引數 `sugar="無糖"`。

---

## 4. 特殊限定符號：`/` 與 `*`

Python 提供了 `/` 與 `*` 語法，可在函式定義中嚴格限制呼叫端傳入引數的方式：

```text
def 函式名稱( 僅限位置參數 , / , 位置或名稱皆可 , * , 僅限關鍵字參數 ):
```

### 4.1 `/` 符號：僅限位置引數 (Positional-Only)
出現在 `/` **左側**的參數，呼叫時**只能用位置傳入**，不能寫出參數名稱。

```python
def calc_bmi(weight, height, /):
    bmi = weight / (height ** 2)
    print(f"BMI 為：{bmi:.1f}")

calc_bmi(65, 1.75)                  # 正確
# calc_bmi(weight=65, height=1.75)  # 錯誤: TypeError
```

### 4.2 `*` 符號：僅限關鍵字引數 (Keyword-Only)
出現在獨立 `*` **右側**的參數，呼叫時**必須使用關鍵字名稱傳入**，不能只靠位置傳入。

```python
def send_email(to, *, subject, urgent=False):
    print(f"寄給：{to}｜主旨：{subject}｜急件：{urgent}")

send_email("student@example.com", subject="課堂通知", urgent=True)  # 正確
send_email("student@example.com", subject="作業提醒")               # 正確 (urgent 採用預設值)
# send_email("student@example.com", "課堂通知", True)                # 錯誤: TypeError
```

### 4.3 綜合應用範例 (`register`)
```python
def register(id_no, /, name, *, role="student"):
    print(f"編號：{id_no}｜姓名：{name}｜身分：{role}")

# 合法呼叫
register("A01", "小明", role="leader")       # id_no 用位置；name 用位置；role 用名稱
register("A01", name="小明", role="leader")  # id_no 用位置；name 用名稱；role 用名稱
register("A01", "小明")                      # role 使用預設值

# 非法呼叫 (觸發 TypeError)
# register(id_no="A01", name="小明")         # 錯誤：id_no 不能用名稱
# register("A01", "小明", "leader")          # 錯誤：role 必須具名傳遞
```

---

## 5. 任意數量引數打包：`*args` 與 `**kwargs`

當事先無法預期會傳入多少引數時，使用打包語法可彈性接收任意數量的資料：

### 5.1 `*args`：打包多餘的「位置引數」為 `tuple`
```python
def sum_scores(*scores):
    print("收到的資料：", scores, type(scores))
    return sum(scores)

print(sum_scores(80, 90, 85))  # 資料: (80, 90, 85)，總和: 255
print(sum_scores(100))         # 資料: (100,)，總和: 100
print(sum_scores())            # 資料: ()，總和: 0
```

### 5.2 `**kwargs`：打包多餘的「關鍵字引數」為 `dict`
```python
def build_profile(name, **info):
    print("姓名：", name)
    print("其他資料：", info, type(info))

build_profile("小華", city="台北", course="Python")
# 輸出:
# 姓名： 小華
# 其他資料： {'city': '台北', 'course': 'Python'} <class 'dict'>
```

---

## 6. Python 內建函式應用範例

筆記本最後展示了標準函式庫如何運用上述的設計手法：

### 6.1 `print()` 函式
```python
# 函式原型：print(*objects, sep=' ', end='\n', file=None, flush=False)

print('a', 'b', '1', '67', '89')               # 使用預設分隔符號（空白）
print('a', 'b', '1', '67', '89', sep='-')      # 指定 sep: 'a-b-1-67-89'
print('a', 'b', '1', '67', '89', end='讚啦!\n') # 指定結尾字元 end
```
- `*objects`：利用 `*args` 機制接收任意多個要輸出的物件。
- `sep` 與 `end`：關鍵字引數，具有預設值，可按需覆蓋。

### 6.2 `sorted()` 函式
```python
# 函式原型：sorted(iterable, *, key=None, reverse=False)

sorted([5, 2, 9, 1, 7], reverse=True)
# 輸出: [9, 7, 5, 2, 1]
```
- `*` 之後的 `key` 與 `reverse` 為 Keyword-Only 參數，強制呼叫者必須寫出參數名稱（例如 `reverse=True`），避免因布林值隨意擺放造成語意混淆。

---

## 7. 常見錯誤與除錯對照表

| 錯誤類型 | 原因範例 | 說明與修正方法 |
| :--- | :--- | :--- |
| `SyntaxError: positional argument follows keyword argument` | `func(a=1, 2)` | 位置引數排在關鍵字引數之後。修正：位置引數必須放最前。 |
| `TypeError: func() missing 1 required positional argument` | `describe_pet("貓")` | 少傳了必填參數。修正：依定義補足引數量。 |
| `TypeError: func() takes 2 positional arguments but 3 were given` | `describe_pet("貓", "狗", "鳥")` | 傳入過多位置引數且無 `*args`。修正：確認參數個數。 |
| `TypeError: func() got some positional-only arguments passed as keyword arguments` | `calc_bmi(weight=60, height=1.7)` | 試圖用名稱傳遞 `/` 左邊的 Positional-Only 參數。修正：僅用位置傳值。 |
| `TypeError: func() takes 1 positional argument but 2 were given` | `send_email("a@b.com", "主旨")` | 試圖用位置傳遞 `*` 右邊的 Keyword-Only 參數。修正：必須以 `subject="主旨"` 具名傳遞。 |
