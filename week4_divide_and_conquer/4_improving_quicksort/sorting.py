# Uses python3
import sys
import random

def quick_sort(sequence):
  if len(sequence) <= 1:
    return sequence
  else:
    pivot = sequence.pop()
  item_greater = []
  item_lower = []
  item_between = [pivot]
  for item in sequence:
    if item > pivot:
      item_greater.append(item)
    elif item < pivot:
      item_lower.append(item)
    else:
      item_between.append(item)
  return quick_sort(item_lower) + item_between + quick_sort(item_greater)

if __name__ == '__main__':
    num_keys = int(input())
    a = list(map(int, input().split()))
    assert len(a) == num_keys
    print(get_number_of_inversions(a))