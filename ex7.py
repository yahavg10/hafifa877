import os
import shutil

def copy_directory(source: str, destination: str, extensions: list = None):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for root, dirs, files in os.walk(source):
        for file in files:
            if extensions is None or any(file.endswith(ext) for ext in extensions):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(destination, os.path.relpath(src_file, source))
                shutil.copy2(src_file, dst_file)

copy_directory(r"C:\src", r"C:\dst", [".mp3", ".json"])
#done
