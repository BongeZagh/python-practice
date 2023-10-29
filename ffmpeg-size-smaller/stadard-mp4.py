# workable, but slow on mac, but convinent though
import tkinter as tk
from tkinter import filedialog
import ffmpeg

def convert_to_h264_aac(input_file, output_file):
    try:
        ffmpeg.input(input_file).output(output_file, vcodec='libx264', acodec='aac').run()
        return "转换成功"
    except ffmpeg.Error as e:
        return f"转换失败: {e.stderr.decode()}"

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP4 Files", "*.mp4")])
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(tk.END, file_path)

def convert_button_click():
    input_file = input_entry.get()
    if not input_file:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "请选择要转换的文件")
        return
    
    output_file = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 Files", "*.mp4")])
    if not output_file:
        return
    
    result = convert_to_h264_aac(input_file, output_file)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

# 创建窗口
window = tk.Tk()
window.title("MP4格式转换")
window.geometry("400x200")

# 创建选择文件按钮
select_button = tk.Button(window, text="选择文件", command=select_file)
select_button.pack(pady=10)

# 创建输入框
input_entry = tk.Entry(window, width=40)
input_entry.pack()

# 创建转换按钮
convert_button = tk.Button(window, text="转换为H.264/AAC", command=convert_button_click)
convert_button.pack(pady=10)

# 创建结果文本框
result_text = tk.Text(window, width=40, height=5)
result_text.pack()

# 运行窗口主循环
window.mainloop()

