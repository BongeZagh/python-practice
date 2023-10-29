#还无法正常使用
import tkinter as tk
from tkinter import filedialog
import av

def convert_to_h264_aac(input_file, output_file):
    # 转换逻辑代码，与之前提供的代码相同

    return "转换成功"

def select_input_file():
    input_file = filedialog.askopenfilename(filetypes=[("视频文件", "*.mp4")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, input_file)

def select_output_file():
    output_file = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("视频文件", "*.mp4")])
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_file)

def convert_video():
    input_file = input_entry.get()
    output_file = output_entry.get()

    if input_file and output_file:
        result = convert_to_h264_aac(input_file, output_file)
        tk.messagebox.showinfo("转换完成", result)
    else:
        tk.messagebox.showwarning("错误", "请选择输入文件和输出文件")

# 创建GUI界面
root = tk.Tk()
root.title("视频转换")
root.geometry("400x200")

# 创建选择输入文件按钮和文本框
input_button = tk.Button(root, text="选择输入文件", command=select_input_file)
input_button.pack()
input_entry = tk.Entry(root)
input_entry.pack()

# 创建选择输出文件按钮和文本框
output_button = tk.Button(root, text="选择输出文件", command=select_output_file)
output_button.pack()
output_entry = tk.Entry(root)
output_entry.pack()

# 创建转换按钮
convert_button = tk.Button(root, text="开始转换", command=convert_video)
convert_button.pack()

root.mainloop()

