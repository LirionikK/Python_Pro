import random as rn


def guess_word(word):
    result = ["*"] * len(word)
    attempts_count = int(input("Enter number of attempts: "))
    count = 0
    while count < attempts_count:
        user_try = input("Enter a letter or word: ")

        if len(user_try) > 1:
            if user_try == word:
                print("Вітаю, ви вгадали слово")
                return
            else:
                print("Слово не правильне. Спробуйте знову")
                count += 1
        else:
            if user_try in word:
                char_index = word.find(user_try)
                result[char_index] = user_try
                print(''.join(result))
            else:
                print("Такої літери немає")
                count += 1
                continue
    print("Ви програли")


if __name__ == "__main__":
    random_words = ["apple", "banana", "grape", "lemon", "peach", "watermelon"]
    key_word = rn.choice(random_words)
    guess_word(key_word)
