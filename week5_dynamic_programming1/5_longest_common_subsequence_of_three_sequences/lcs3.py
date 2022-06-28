#Uses python3
import numpy as np
import sys

def lcs3(pattern_1, pattern_2,pattern_3):
  m = len(pattern_1)
  n = len(pattern_2)
  k = len(pattern_3)
  dp = np.zeros((m+1,n+1,k+1))
  for i in range(1,m+1):
    for j in range(1,n+1):
      for k in range(1,k+1):
        previous_lcs = dp[i-1, j-1, k-1]
        a = dp[i-1 , j, k]
        b = dp[i , j-1, k]
        c = dp[i, j, k-1]
        if (pattern_1[i-1] == pattern_2[j-1]) and (pattern_1[i-1] == pattern_3[k-1]):
          dp[i,j,k] = previous_lcs + 1
        else:
          dp[i,j,k] = max(a, b, c, previous_lcs)
  return int(dp[-1,-1,-1])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
