file1_path = "file1.txt"
file2_path = "file2.txt"

with open(file1_path, "r") as file1, open(file2_path, "r") as file2:
    lines1 = file1.readlines()
    lines2 = file2.readlines()

print("Рядки, які є у першому файлі, але відсутні у другому:")
for line in lines1:
    if line not in lines2:
        print(line.strip())
