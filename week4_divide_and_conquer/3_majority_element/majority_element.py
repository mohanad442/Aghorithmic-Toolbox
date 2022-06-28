# Uses python3
import sys
import math


def get_majority_element(a):
    d = {}
    for num in a:
      d[num] = d.get(num,0) +1
    m = max(d , key = lambda x:d[x])
    majority = (int(len(a) / 2) +1)
    if d[m] >= majority:
      return 1
    else:
      return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) == 1:
        print(1)
    else:
        print(0)
