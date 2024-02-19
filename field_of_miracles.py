import random as rn


def guess_word(word):
    result = ["*"] * len(word)
    attempts_count = int(input("Enter number of attempts: "))
    guessed_letters = set()
    while attempts_count > 0:
        user_try = input("Enter a letter or word: ").lower()

        if len(user_try) > 1:
            if user_try == word:
                print("Вітаю, ви вгадали слово")
                return
            else:
                print("Слово не правильне. Спробуйте знову")
                attempts_count -= 1

        else:
            if user_try in word:
                guessed_letters.add(user_try)
                remaining_word = ''.join([ch if ch in guessed_letters else '*' for ch in word])
                print(remaining_word)

                if '*' not in remaining_word:
                    print("Вы угадали слово!")
                    return
            else:
                print("Такої літери немає")
                attempts_count -= 1
    print("Ви програли")


if __name__ == "__main__":
    random_words = ["apple", "banana", "grape", "lemon", "peach", "watermelon"]
    key_word = rn.choice(random_words)
    guess_word(key_word)
