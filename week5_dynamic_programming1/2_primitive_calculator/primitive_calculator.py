# Uses python3
import sys


def optimal_sequence(n):
    parameters = [3, 2, 1]
    num_operation = [0]
    output = [[1]] * n
    if n == 1:
        return output[n-1]
    for i in range(1, n):
        op = []
        num = []
        if (i == 1) | (i == 2):
            num_operation.append(1)
            output[i] = [1, i + 1]
            continue
        for k in range(len(parameters)):
            if parameters[k] == 1:
                op.append(output[i - parameters[k]] + [output[i - parameters[k]][-1] + parameters[k]])
                num.append(1 + num_operation[i - parameters[k]])
            else:
                if (i + 1) % parameters[k] == 0:
                    op.append(output[int((i + 1) / parameters[k]) - 1] + [i + 1])
                    num.append(1 + num_operation[int((i + 1) / parameters[k]) - 1])
        minimum = min(num)
        inx = num.index(minimum)
        num_operation.append(minimum)
        output[i] = op[inx]
    return output[n - 1]


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
