import subprocess
import tkinter as tk
from tkinter import filedialog

def convert_to_mp3(input_file):
    output_file = input_file.replace(".mp4", ".mp3")
    command = ["ffmpeg", "-i", input_file, "-vn", "-acodec", "libmp3lame", output_file]
    subprocess.run(command)
    print("Conversion completed successfully!")

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("MP4 Files", "*.mp4")])
    if file_path:
        convert_to_mp3(file_path)

select_file()

