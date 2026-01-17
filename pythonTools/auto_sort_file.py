import os, shutil

# BASE = "C:\\aToRead\\C_CPP\\ToRead\\Advanced\\Documents"
BASE = r"C:\aToRead\C_CPP\ToRead\Advanced\Documents"
MAP = {".pdf": "Documents", ".png": "Images", ".jpg": "Images"}

for f in os.listdir(BASE):
    ext = os.path.splitext(f)[1].lower()
    if ext in MAP:
        dest = os.path.join(BASE, MAP[ext])
        os.makedirs(dest, exist_ok=True)
        shutil.move(os.path.join(BASE, f), dest)
