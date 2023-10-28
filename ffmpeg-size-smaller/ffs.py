import tkinter as tk
from tkinter import filedialog
import subprocess

def compress_video():
    input_file = filedialog.askopenfilename(title="选择视频文件")
    output_file = filedialog.asksaveasfilename(title="保存压缩后的视频文件", defaultextension=".mp4")
    
    # 使用FFmpeg进行视频压缩
    command = f'ffmpeg -i "{input_file}" -vf "scale=1280:-1" -b:v 1M "{output_file}"'
    subprocess.call(command, shell=True)
    
    # 显示完成提示
    tk.messagebox.showinfo("完成", "视频压缩完成！")

# 创建GUI窗口
window = tk.Tk()
window.title("视频压缩工具")

# 添加按钮
compress_button = tk.Button(window, text="选择视频文件并压缩", command=compress_video)
compress_button.pack(pady=20)

# 运行主循环
window.mainloop()

