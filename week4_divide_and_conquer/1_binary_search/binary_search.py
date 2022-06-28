# itreative method

def binary_search(a, x):
    left, right = 0, len(a) - 1

    while mid != x:
        mid = left + int((right - left) / 2)
        if right < left:
            return -1

        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid - 1
        elif x > a[mid]:
            left = mid + 1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
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
