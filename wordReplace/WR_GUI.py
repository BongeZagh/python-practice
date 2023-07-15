import os
import tkinter as tk
import re

def read_rules():
    rules = []
    with open('rules.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):  # 忽略空行和注释
                continue
            if '->' not in line:  # 如果没有箭头，则跳过该行并打印警告消息
                print(f'Warning: Invalid rule format: {line}')
                continue
            pattern, replacement = line.split('->')
            # 将 \b 转义为 \\b
            pattern = pattern.replace(r'\b', r'\\b')
            rules.append((pattern.strip(), replacement.strip()))
    return rules

# 定义替换函数
def replace_text():
    # 获取输入文本
    input_text = input_textbox.get("1.0", "end-1c")
    # 替换指定字符串
    output_text = input_text
    for pattern, replacement in patterns:
        output_text = re.sub(pattern, replacement, output_text)
    # 显示输出文本
    output_textbox.delete("1.0", "end")
    output_textbox.insert("1.0", output_text)

# 定义编辑规则函数
def edit_rules():
    # 打开规则文件
    os.startfile('rules.txt')
    # 重新读取规则文件并初始化规则列表
    global patterns
    patterns = read_rules()

# 创建主窗口
root = tk.Tk()
root.title("Text Replacer")
root.geometry("800x600")

# 读取并初始化规则列表
patterns = read_rules()

# 创建输入文本框
input_label = tk.Label(root, text="Input Text:")
input_label.pack()
input_textbox = tk.Text(root)
input_textbox.pack(side="left", fill="both", expand=True)

# 创建输出文本框
output_label = tk.Label(root, text="Output Text:")
output_label.pack()
output_textbox = tk.Text(root)
output_textbox.pack(side="right", fill="both", expand=True)

# 创建替换按钮
replace_button = tk.Button(root, text="Replace", command=replace_text)
replace_button.pack(side="bottom", padx=10, pady=10)

# 创建编辑规则按钮
edit_button = tk.Button(root, text="Edit Rules", command=edit_rules)
edit_button.pack()

# 进入主循环
root.mainloop()

try:
    # 获取输入文本
    input_text = input_textbox.get("1.0", "end-1c")
    # 替换指定字符串
    output_text = input_text
    for pattern, replacement in patterns:
        output_text = re.sub(pattern, replacement, output_text)
    # 显示输出文本
    output_textbox.delete("1.0", "end")
    output_textbox.insert("1.0", output_text)
except Exception as e:
    # 打印错误消息
    print("An error occurred: ", str(e))