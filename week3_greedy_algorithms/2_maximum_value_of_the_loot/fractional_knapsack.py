# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    import numpy as np
    value = 0
    n = 0
    remain = capacity
    while n < capacity:

        max_value = np.argmax(values)
        percentage = remain / weights[max_value]
        if percentage > 1:
            remain -= weights[max_value]
            n += weights[max_value]
            value += weights[max_value] * values[max_value]
            weights.pop(max_value)
            values.pop(max_value)
        else:
            n += remain
            value += values[max_value] * remain

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
