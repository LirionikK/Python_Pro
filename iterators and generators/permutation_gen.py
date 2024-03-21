def permutations(num, start=0):
    if start == len(num) - 1:
        yield num[:]
    else:
        for i in range(start, len(num)):
            num[start], num[i] = num[i], num[start]
            yield from permutations(num, start + 1)
            num[start], num[i] = num[i], num[start]


for perm in permutations([1, 2, 3]):
    print(perm)
