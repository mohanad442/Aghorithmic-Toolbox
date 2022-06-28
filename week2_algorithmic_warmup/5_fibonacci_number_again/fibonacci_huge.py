# Uses python3
import sys


def get_fibonacci_huge(n, m):
    n = int(n)
    m = int(m)
    mod_seq = []
    mod_seq.append(0)
    mod_seq.append(1)
    mod_seq.append(1)
    p = 2
    while not (mod_seq[p - 1] == 0 and mod_seq[p] == 1):
        mod_seq.append((mod_seq[p] + mod_seq[p - 1]) % m)
        p = p + 1
    l = n % (p - 1)
    return (mod_seq[l])


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
