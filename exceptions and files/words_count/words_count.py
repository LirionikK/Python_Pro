def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            print("The number of words in the file", filename, ":", word_count)
    except FileNotFoundError:
        print("File not found")


filename = "text.txt"
count_words_in_file(filename)
