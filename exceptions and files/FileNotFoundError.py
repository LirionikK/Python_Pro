try:
    file = open("example.txt", "r")
    content = file.read()
    file.close()
    print("File content:", content)
except FileNotFoundError:
    print("File not found")
