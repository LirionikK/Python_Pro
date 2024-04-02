def recursive_dec_to_bin_converter(num):
    if num < 2:
        return str(num)
    else:
        return recursive_dec_to_bin_converter(num//2) + str(num % 2)


result = recursive_dec_to_bin_converter(12)
print(result)
