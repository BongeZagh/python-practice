import tkinter as tk
from tkinter import filedialog
import subprocess

def convert_to_mp4():
    input_file = filedialog.askopenfilename(title="选择WebM文件", filetypes=[("WebM 文件", "*.webm")])
    output_file = filedialog.asksaveasfilename(title="保存转换后的MP4文件", defaultextension=".mp4")
    
    # 使用FFmpeg进行格式转换
    command = f'ffmpeg -i "{input_file}" "{output_file}"'
    subprocess.call(command, shell=True)
    
    # 显示完成提示
    tk.messagebox.showinfo("完成", "格式转换完成！")

# 创建GUI窗口
window = tk.Tk()
window.title("WebM转换为MP4工具")

# 添加按钮
convert_button = tk.Button(window, text="选择WebM文件并转换为MP4", command=convert_to_mp4)
convert_button.pack(pady=20)

# 运行主循环
window.mainloop()

