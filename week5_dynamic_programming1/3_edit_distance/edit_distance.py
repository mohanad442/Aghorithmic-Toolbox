# Uses python3
import numpy as np


def edit_distance(a, b):
    mat = np.zeros((len(a) + 1, len(b) + 1))
    for i in range(len(a) + 1):
        mat[i, 0] = i
    for j in range(len(b) + 1):
        mat[0, j] = j

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            insertion = mat[i, j - 1] + 1
            deletion = mat[i - 1, j] + 1
            match = mat[i - 1, j - 1]
            mismatch = mat[i - 1, j - 1] + 1
            if a[i - 1] == b[j - 1]:
                mat[i, j] = min(insertion, deletion, match)
            else:
                mat[i, j] = min(insertion, deletion, mismatch)
    return int(mat[-1, -1])

if __name__ == "__main__":
    print(edit_distance(input(), input()))
