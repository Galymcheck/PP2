import os
import shutil

os.makedirs("project/data/files", exist_ok=True)  #create nested directory
file1 = open("project/data/files/123.txt", "w")
file1.write("Hello")
file1.close()
print(os.listdir("project"))

for file in os.listdir("project"):
    if file.endswith(".txt"):
        print("txt file:", file)
    else:
        print("'project' folder does not have txt files")

#shutil.rmtree("project")