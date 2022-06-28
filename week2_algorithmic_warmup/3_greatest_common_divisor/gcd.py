# Uses python3
import sys

def gcd_naive(a, b):
    a = int(a)
    b = int(b)
    reminder = a % b
    while (reminder != 0):
      a = b
      b = reminder
      reminder = a % b
    return b

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
