with open("example.txt", "r") as f:
    data = f.read()
    print(data)
    f.seek(0)
    line = f.readlines()
    print(line)