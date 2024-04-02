def recursive_reverse(word):
    if len(word) == 1:
        return word
    else:
        n = len(word)
        return word[-1] + recursive_reverse(word[:n-1])


result = recursive_reverse("hello")
print(result)
