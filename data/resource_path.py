import os, sys

PATH = r'C:\Users\1\Desktop\Питон\pygame\Yoda_timer'

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(PATH, relative)
