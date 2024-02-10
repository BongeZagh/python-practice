import os

directory_path = "./pages"

for filename in os.listdir(directory_path):
    if filename.startswith("https%3A"):
        new_filename = filename.replace("https%3A", "")
        old_filepath = os.path.join(directory_path, filename)
        new_filepath = os.path.join(directory_path, new_filename)
        os.rename(old_filepath, new_filepath)

