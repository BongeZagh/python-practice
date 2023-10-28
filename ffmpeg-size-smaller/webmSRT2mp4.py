import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from moviepy.editor import VideoFileClip
from moviepy.editor import TextClip
from moviepy.editor import CompositeVideoClip
import subprocess

def merge_video_with_subtitles():
    video_file = filedialog.askopenfilename(title="选择WebM视频文件", filetypes=[("WebM 文件", "*.webm")])
    subtitle_file = filedialog.askopenfilename(title="选择SRT字幕文件", filetypes=[("SRT 文件", "*.srt")])
    output_file = filedialog.asksaveasfilename(title="保存合并后的视频文件", defaultextension=".mp4")

    try:
        # 加载视频和字幕文件
        video_clip = VideoFileClip(video_file)
        subtitle_clip = TextClip(subtitle_file, fontsize=20, color='white').set_position(('center', 'bottom')).set_duration(video_clip.duration)

        # 合并视频和字幕
        final_clip = CompositeVideoClip([video_clip, subtitle_clip])

        # 保存合并后的视频文件
        final_clip.write_videofile(output_file, codec='libx264')

        # 使用FFmpeg将WebM转换为MP4
        mp4_output_file = output_file.replace(".webm", ".mp4")
        command = f'ffmpeg -i "{output_file}" "{mp4_output_file}"'
        subprocess.call(command, shell=True)

        messagebox.showinfo("完成", "视频与字幕合并并转换为MP4完成！")
    except Exception as e:
        messagebox.showerror("错误", str(e))

# 创建GUI窗口
window = tk.Tk()
window.title("视频与字幕合并工具")

# 添加按钮
merge_button = tk.Button(window, text="选择视频和字幕并合并", command=merge_video_with_subtitles)
merge_button.pack(pady=20)

# 运行主循环
window.mainloop()

