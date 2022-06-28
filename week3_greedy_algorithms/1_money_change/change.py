# Uses python3
import sys


def get_change(m):
    Money = m
    change = [10, 5, 1]
    n = 0
    i = 0
    num_of_coins = 0
    remain = m
    while n < m:
        if remain >= change[i]:
            n += change[i]
            remain -= change[i]
            i = i - 1
            num_of_coins += 1

        i = i + 1
    return num_of_coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
