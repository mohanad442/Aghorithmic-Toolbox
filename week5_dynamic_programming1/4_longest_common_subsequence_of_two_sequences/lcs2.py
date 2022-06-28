#Uses python3

import sys

#Dynamic Programming
import numpy as np
def lcs2(pattern_1, pattern_2):
  m = len(pattern_1)
  n = len(pattern_2)
# dp will store solutions as the iteration goes on
  dp = np.zeros((m+1,n+1))
  for i in range(1,m+1):
    for j in range(1,n+1):
      insertion = dp[i-1,j]
      deletion = dp[i,j-1]
      previous_lcs = dp[i-1 , j-1]
      if pattern_1[i-1] == pattern_2[j-1]:
        dp[i,j] = previous_lcs + 1
      else:
        dp[i,j] = max(insertion , deletion, previous_lcs)
  return int(dp[-1,-1])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
