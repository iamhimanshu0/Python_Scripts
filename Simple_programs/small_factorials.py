'''
Input
An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, each containing a single integer n, 1<=n<=100.

Output
For each integer n given at input, display a line with the value of n!'''


def fac(n):
    if n < 1:
        return 1
    else:
        return n * fac(n - 1)


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t = t - 1
        n = int(input())
        print(fac(n))
