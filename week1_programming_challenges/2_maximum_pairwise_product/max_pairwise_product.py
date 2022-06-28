# python3

def max_pairwise_product(numbers):
    numbers = sorted(numbers)
    i = numbers[-1]
    j = numbers[-2]
    max_product = i*j
    return max_product



if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
