import time


def recursive_count_down(num):
    if num == 0:
        return
    else:
        print(num)
        time.sleep(1)
        recursive_count_down(num - 1)


recursive_count_down(10)
