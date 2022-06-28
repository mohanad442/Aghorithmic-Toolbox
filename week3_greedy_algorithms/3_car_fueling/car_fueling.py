# python3
import sys


def compute_min_refills(distance, tank, stops):
    import math
    stop = math.floor(float(distance / tank))
    return stop

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
