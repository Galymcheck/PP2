file = open("example.txt", "w")
file.write("This is a test file\n")
file.write("Hello from test file")
file.close()     #Closing a file will free up the resources that are tied to the file

x=False
#x=True
if x:
    with open("example.txt", "a") as f:
        f.write("\nNew line")