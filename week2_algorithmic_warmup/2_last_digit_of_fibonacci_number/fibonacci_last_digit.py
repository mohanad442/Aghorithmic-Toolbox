import numpy as np
def get_fibonacci_last_digit_naive(n):
    if n <= 1:
      return n

    F = np.zeros((n+1))
    F[1] = 1
    for i in range(2,n+1):
        F[i] = F[i-1]%10 + F[i-2]%10

    return int(F[i]%10)


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
