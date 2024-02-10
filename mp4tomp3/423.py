import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog

def convert_to_mp3(input_file):
    video = mp.VideoFileClip(input_file)
    audio = video.audio
    output_file = input_file.replace(".mp4", ".mp3")
    audio.write_audiofile(output_file)
    print("Conversion completed successfully!")

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("MP4 Files", "*.mp4")])
    if file_path:
        convert_to_mp3(file_path)

select_file()

