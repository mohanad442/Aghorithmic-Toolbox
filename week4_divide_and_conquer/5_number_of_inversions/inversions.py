import sys
# MergeSort in Python
def get_number_of_inversions(array):
  if len(array) ==1:
    return array,0
  else:
        #  r is the point where the array is divided into two subarrays
    r = len(array)//2
    Left = array[:r]
    right = array[r:]
        # Sort the two halves
    Left , left_inv = get_number_of_inversions(Left)
    right , right_inv = get_number_of_inversions(right)
    arr_sorted = []
    i = j = 0
    inversions = 0 + left_inv + right_inv
    while i < len(Left) and j < len(right):
      if Left[i] <= right[j]:
        arr_sorted.append(Left[i])
        i += 1
      else:
        arr_sorted.append(right[j])
        j += 1
        inversions += len(Left)-i
  arr_sorted += Left[i:]
  arr_sorted += right[j:]
  return arr_sorted,inversions


if __name__ == '__main__':
    num_keys = int(input())
    a = list(map(int, input().split()))
    assert len(a) == num_keys
    print(get_number_of_inversions(a)[1])