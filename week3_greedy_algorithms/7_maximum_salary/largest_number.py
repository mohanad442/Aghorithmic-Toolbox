#Uses python3

import sys
import numpy as np

def largest_number(a):
    res = []

    matrix = []
    L = [len(str(x)) for x in a]
    for i in range(len(a)):
        matrix.append(a[i] * (10 ** (max(L) - L[i])))
    for i in range(len(a)):
        max_num = np.argmax(matrix)
        res.append(str(a[max_num]))
        a.pop(max_num)
        matrix.pop(max_num)
    res = "".join(res)
    return int(res)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
