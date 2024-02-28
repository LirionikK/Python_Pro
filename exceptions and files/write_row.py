def write_file(text, file_path):
    try:
        with open(file_path, 'a+') as f:
            f.write(text)
        print("Success")
    except Exception as e:
        print(f"Error: {e}")


file_path = "file.txt"
user_input = input("Enter text: ")

write_file(user_input, file_path)
