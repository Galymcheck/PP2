import shutil

shutil.copy("example.txt", "backup.txt")

import os

x=False
#x=True
if x:
    if os.path.exists("backup.txt"):
        os.remove("backup.txt")
    if os.path.exists("example.txt"):
        os.remove("example.txt")