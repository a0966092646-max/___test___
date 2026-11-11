from pathlib import Path


folder = Path(__file__).parent
sample_path = folder / "readFile_sample.txt"
output_path = folder / "readFile_output.txt"

# 讀取整份文字檔
with open(sample_path, "r", encoding="utf-8") as file:
    content = file.read()

print("=== 整份檔案 ===")
print(content)

# 逐行讀取並移除行尾換行
print("=== 逐行讀取 ===")
with open(sample_path, "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# 寫入模式會建立檔案，或清除已存在檔案的內容
with open(output_path, "w", encoding="utf-8") as file:
    file.write("購物清單副本：\n")
    file.write(content)

print(f"已寫入：{output_path.name}")

# 追加模式會保留原內容，並在檔案末尾新增文字
with open(output_path, "a", encoding="utf-8") as file:
    file.write("這一行是追加的備註。\n")

print(f"已追加一行備註到：{output_path.name}")