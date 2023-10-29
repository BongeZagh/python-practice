import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip, SubtitlesClip, CompositeVideoClip

def merge_videos_with_subtitles():
    # 选择视频文件
    video_file = filedialog.askopenfilename(title="选择MP4文件", filetypes=[("MP4 文件", "*.mp4")])
    
    # 选择字幕文件
    subtitle_file = filedialog.askopenfilename(title="选择SRT字幕文件", filetypes=[("SRT 文件", "*.srt")])
    
    # 选择输出文件路径
    output_file = filedialog.asksaveasfilename(title="保存合并后的视频", defaultextension=".mp4")
    
    # 加载视频和字幕
    video_clip = VideoFileClip(video_file)
    subtitle_clip = SubtitlesClip(subtitle_file, fontsize=20, color='white').set_position(('center', 'bottom')).set_duration(video_clip.duration)
    
    # 合并视频和字幕
    final_clip = CompositeVideoClip([video_clip, subtitle_clip])
    
    # 导出合并后的视频
    final_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')
    
    # 显示完成提示
    tk.messagebox.showinfo("完成", "视频合并完成！")

# 创建GUI窗口
window = tk.Tk()
window.title("视频合并工具")

# 添加按钮
merge_button = tk.Button(window, text="选择MP4文件和SRT字幕文件并合并", command=merge_videos_with_subtitles)
merge_button.pack(pady=20)

# 运行主循环
window.mainloop()

