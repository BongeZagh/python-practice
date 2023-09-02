# 这段程序是在colab 中检查不同folder文件，得到的灵感，colab中对比不同文件夹文件很麻烦用这个方式方便观察，尤其是处理srt文件的时候
import os

folder1 = "/content/drive/MyDrive/BPAproject"
folder2 = "/content/drive/MyDrive/Colab Notebooks/Whisper Youtube"

files1 = os.listdir(folder1)
files2 = os.listdir(folder2)

common_prefixes = set()

# 获取文件名前缀相同的集合
for file1 in files1:
    prefix = os.path.splitext(file1)[0]
    common_prefixes.add(prefix)

# 比较文件名前缀相同但后缀不同的文件
for file2 in files2:
    prefix = os.path.splitext(file2)[0]
    if prefix in common_prefixes:
        extension1 = os.path.splitext(file1)[1]
        extension2 = os.path.splitext(file2)[1]
        if extension1 != extension2:
            file1_path = os.path.join(folder1, file1)
            file2_path = os.path.join(folder2, file2)
            print(f"相同前缀但后缀不同的文件：{file1_path} 和 {file2_path}")
            common_prefixes.remove(prefix)  # 移除已经匹配过的前缀

# 列出只有一个后缀存在的文件
for prefix in common_prefixes:
    file1_path = os.path.join(folder1, f"{prefix}.mp4")
    file2_path = os.path.join(folder2, f"{prefix}.srt")
    if os.path.exists(file1_path) and not os.path.exists(file2_path):
        print(f"只有一个后缀存在的文件：{file1_path}")


