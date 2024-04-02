def recursive_sum(num):
    if num == 0:
        return 0
    else:
        return num % 10 + recursive_sum(num // 10)


result_with_recursion = recursive_sum(1234)
print("Результат:", result_with_recursion)
