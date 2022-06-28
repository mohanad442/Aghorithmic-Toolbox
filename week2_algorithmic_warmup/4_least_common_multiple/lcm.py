# Uses python3
import sys

def lcm_naive(a, b):
  a=int(a)
  b = int(b)
  for l in range(1, b + 1):
    l = l*a
    if l % a == 0 and l % b == 0:
        return l

  return a*b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

