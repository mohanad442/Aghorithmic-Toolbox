# Uses python3
import sys

def get_change(money):
  denominations = [1,3,4]
  min_coins = [1]*money
  for i in range(1,money):
    best = []
    for k in range(len(denominations)):
      if i+1 == denominations[k]:
        best.append(1)
        break
      best.append(1+ min_coins[(i) - denominations[k]])
    min_coins[i] = min(best)
  return min_coins[money - 1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
