def copy_file(file1_path, file2_path):
    try:
        with open(file1_path, 'r') as source, open(file2_path, 'w') as destination:
            destination.write(source.read())
        print("The contents of the file were copied successfully.")
    except FileNotFoundError:
        print("One of the files was not found.")
    except Exception as e:
        print(f"Error: {e}")


file1_path = "file1.txt"
file2_path = "file2.txt"

copy_file(file1_path, file2_path)
