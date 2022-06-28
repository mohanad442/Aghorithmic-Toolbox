def binary_search(a,x):
  low = 0
  high = len(a)-1
  while (low <= high):
    mid = low + int((high - low) / 2)
    if a[mid] == x:
      if (mid-1 >= 0) & (a[mid-1] == x) :
        high = mid-1
        continue
      return mid
    elif x < a[mid]:
      high = mid-1
    elif x > a[mid]:
      low = mid+1
  return -1


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
