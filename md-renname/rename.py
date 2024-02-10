import os

def process_md_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r") as file:
                content = file.read()
            
            if "project:: contacts" in content:
                new_filename = "contacts." + filename
                new_filepath = os.path.join(directory, new_filename)
                os.rename(filepath, new_filepath)
                print(f"Modified file: {filename} -> {new_filename}")

# 指定包含 Markdown 文件的目录路径
directory_path = "/Users/zaghyang/Documents/pythonCode/md-renname/pages"
process_md_files(directory_path)

