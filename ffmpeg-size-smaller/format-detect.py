import tkinter as tk
import ffmpeg

def detect_video_format(filepath):
    try:
        probe = ffmpeg.probe(filepath)
        
        video_streams = [stream for stream in probe['streams'] if stream['codec_type'] == 'video']
        audio_streams = [stream for stream in probe['streams'] if stream['codec_type'] == 'audio']
        
        result = ""
        
        if video_streams:
            result += "视频格式:\n"
            for stream in video_streams:
                video_format = stream['codec_name']
                result += f"{video_format}\n"
        
        if audio_streams:
            result += "音频格式:\n"
            for stream in audio_streams:
                audio_format = stream['codec_name']
                result += f"{audio_format}\n"
        
        if not video_streams and not audio_streams:
            result += "无法检测到视频或音频流"
        
        return result
    
    except ffmpeg.Error as e:
        return f"发生错误: {e.stderr.decode()}"

def detect_button_click():
    filepath = entry.get()
    result = detect_video_format(filepath)
    text.delete(1.0, tk.END)
    text.insert(tk.END, result)

# 创建窗口
window = tk.Tk()
window.title("视频格式检测")
window.geometry("400x300")

# 创建输入框
entry = tk.Entry(window, width=40)
entry.pack(pady=10)

# 创建按钮
button = tk.Button(window, text="检测格式", command=detect_button_click)
button.pack(pady=10)

# 创建文本框
text = tk.Text(window, width=40, height=10)
text.pack()

# 运行窗口主循环
window.mainloop()

