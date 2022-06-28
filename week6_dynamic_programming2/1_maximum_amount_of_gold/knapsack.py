# Uses python3
import sys

import numpy as np
def optimal_weight(knapsak_capacity , weights):
  mat = np.zeros((len(weights)+1, knapsak_capacity + 1))
  for i in range(1, len(weights)+1):
    for j in range(1, knapsak_capacity + 1):
      if j < weights[i-1]:
        mat[i,j] = mat[i-1 , j]
      else:
        mat[i,j] = max(weights[i-1] + mat[i-1, j - weights[i-1]],mat[i-1 , j])
  return int(mat[-1,-1])

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
