'''Approximate pi

Eurler famously came up with the formula:
pi ^ 2 / 6 := sigma (1/k^2) for k = 1 to inf'''

import math

def approx(iterations):
    '''approximating'''
    tmp = 0.0
    for i in range(1, iterations + 1):
        tmp += 1.0 / (i ** 2.0)
    return math.sqrt(6 * tmp)

def main():
    '''Main function'''
    iterations = int(input('Iteration?'))
    pi_approximated = approx(iterations)
    print("Pi is approximated as")
    print(pi_approximated)

if __name__ == '__main__':
    main()
