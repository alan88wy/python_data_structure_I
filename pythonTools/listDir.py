import os

# Lists contents of the root directory of the C: drive
path = "C:\\aToRead\\C_CPP\\ToRead\\Advanced\\Documents"
# path = r"C:\aToRead\C_CPP\ToRead\Advanced\Documents"

try:
    contents = os.listdir(path)
    print(f"Contents of {path}:", contents)
except FileNotFoundError:
    print(f"Error: The directory '{path}' was not found.")